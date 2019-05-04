#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>

#define MAX_COMMAND_LENGTH 256
#define HISTORY_SIZE 5

int shellShouldRun = 1;
int skipChildProcessWait;
int commandIsExternal;
int h_counter = 0; // history counter and tracker for the command records.. Max value is 5

char* argv[MAX_COMMAND_LENGTH];
char input[MAX_COMMAND_LENGTH];

char* copy_of_input[MAX_COMMAND_LENGTH]; //we want to copy every value of input into this all the time
char* history_Queue[HISTORY_SIZE + 1][MAX_COMMAND_LENGTH]; // multidimensional array for recording the command history

void delete_cmd(void); // function for removing a command from the history queue
void insert_cmd(void); // function for adding a command to the historiy queue

int main(void)
{
  while (shellShouldRun) {
    getInput();
    formatInputForExec();
    executeCommand();

    // only excute this if command is known to be only External cause we don't want to store commands like history into the history queue etc.
    if (commandIsExternal){
    	cacheInputToHistoryQueue();
    }

  }

  return 0;
}

void getInput() {
  printf("osh> ");
  fflush(stdout);
  fgets(input, MAX_COMMAND_LENGTH, stdin);
}

void formatInputForExec() {
  // Replace newline with null terminator
  size_t length = strlen(input);
  if (input[length - 1] == '\n') // removing the newline character
    input[length - 1] = '\0';

  // Set skipChildProcessWait, and replace '&' with null terminator if it exists
  skipChildProcessWait = input[length - 2] == '&';
  if (skipChildProcessWait) {
    input[length - 2] = '\0';
  }

  strcpy(copy_of_input, input); // copying the input into the input tracking variable

  // Delimit input space based on space characters
  char* token;
  token = strtok(input," ");
  int i = 0;
  while(token != NULL) {
      argv[i] = token;
      token = strtok(NULL," ");
      i++;
  }
  argv[i]=NULL;

}

void executeCommand() {
  executeShellLevelCommands();
  if (commandIsExternal)
    executeExternalCommand();
}

void executeExternalCommand() {
  pid_t cmd_pid = fork();
  if (cmd_pid == 0) {
    execvp(argv[0], argv);
    fprintf(stderr, "Child process could not do execvp\n");
    exit(0);
  }
  else {
    if (!skipChildProcessWait) {
      wait(cmd_pid);
    }
  }
}

// Process shell level commands.
// A command is external if it should be executed by execvp().
// A command is internal if its something like "history".
// Internal commands shouldn't be executed by execvp()
void executeShellLevelCommands() {
  // If the command is displaying history, we simply display history.
  // This command is not external
  if (!strcmp(argv[0], "history")) {
    commandIsExternal = 0;
    displayHistory();
  }
  // If the current command is "!!", we re-execute the last command
  else if (!strcmp(argv[0], "!!")) {
    strcpy(input, history_Queue[h_counter]); // history counter keeps track of the index position of the most recent command.
    formatInputForExec();
    commandIsExternal = 1;
  }
  // If the current command is "! n", we execute the nth entry in history
  else if (!strcmp(argv[0], "!")) {
    int n = atoi(argv[1]);
    // Make sure that we're not going back more than the length of historyQueue
    if (n > HISTORY_SIZE || n < 1) {
      fprintf(stderr, "Can't look back that far in history!\n");
      // We don't want the command to be executed, since we have an error
      // We can do this by treating this as an internal command where we do nothing
      commandIsExternal = 0;
    }
    // Fetch command from history, replace input string with command,
    // then reprocess input.
    else {
      strcpy(input, history_Queue[n]); // fetches the command at the nth position of the history
      formatInputForExec();
      commandIsExternal = 1;

    }
  }
  else if(!strcmp(argv[0], "quit")) {
  	commandIsExternal = 0; // quit command is treated as an internal command
  	shellShouldRun = 0;  // terminates the program when the quit is passed in the command line
  }
  else {
    commandIsExternal = 1;
  }

}

// Put current command into history queue
void cacheInputToHistoryQueue() {
  if (h_counter < HISTORY_SIZE) {
  	h_counter = h_counter + 1; // increments the history count variable by 1 meaning an extra command has been executed
  	strcpy(history_Queue[h_counter], copy_of_input);  // copies the command into the array history
  }
  else {
  	delete_cmd(); // since history has reached its max limit, we remove the oldest command
  	insert_cmd(); // insert the new comman into the most recent spot in history
  }
}

// Displays the history queue contents
void displayHistory() {
  for (int i = h_counter; i >= 1; i--){
  	printf("%d %s\n", i, history_Queue[i]); // prints the command from history with corresponding numbers
  }
}
//
void delete_cmd(void){
	for (int i=0; i<HISTORY_SIZE; i++){
		strcpy(history_Queue[i], history_Queue[i+1]);  // Swaps the ith element with (i+1)th element of history
	}
}

// copy_of_input holds the recent command to be stored into the history of commands
void insert_cmd(void){
	// since size of history is 6, we therefor insert the latest command in the 6th position of history queue which corresponds to the 5th index
	strcpy(history_Queue[HISTORY_SIZE], copy_of_input);
}
