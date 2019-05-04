#include <pthread.h>
#include <stdio.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int isCurrentlyEven = 1;

void *even_runner();
void *odd_runner();

int main(int argc, char *argv[])
{

  pthread_t even_thread_tid; /* the thread identifier */
  pthread_attr_t even_thread_attr; /* set of thread attributes */

  pthread_t odd_thread_tid; /* the thread identifier */
  pthread_attr_t odd_thread_attr; /* set of thread attributes */

  // Start the two summing threads
  pthread_attr_init(&even_thread_attr);
  pthread_create(&even_thread_tid, &even_thread_attr, even_runner, NULL);

  pthread_attr_init(&odd_thread_attr);
  pthread_create(&odd_thread_tid, &odd_thread_attr, odd_runner, NULL);

  pthread_join(even_thread_tid,NULL);
  pthread_join(odd_thread_tid,NULL);

  printf("Finished printing numbers 1-100.\n");

}

void *even_runner() {
  int value = 0;

  while (value <= 100) {
    if (isCurrentlyEven) {
      pthread_mutex_lock(&mutex);
      printf("%d\n", value);
      value += 2;
      isCurrentlyEven = 0;
      pthread_mutex_unlock(&mutex);
    }
  }
}

void *odd_runner() {
  int value = 1;

  while (value <= 100) {
    if (!isCurrentlyEven) {
      pthread_mutex_lock(&mutex);
      printf("%d\n", value);
      value += 2;
      isCurrentlyEven = 1;
      pthread_mutex_unlock(&mutex);
    }
  }
}
