#include <linux/sched.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>


// Steps to running the code
// 1) run "make" from the command line
// 2) Then type this on the command line: sudo insmod q1.ko
// 3) Type: dmesg
// After the first three steps, the module will be loaded.
// To remove the loaded module, type: sudo rmmod q1
// To confirm if module has been removed, type: sudo dmesg -c

// function for performing the dfs operation
void dfs_operation(struct task_struct *init_task){

	struct task_struct *next_task;
	struct list_head *list;

	list_for_each(list, &init_task->children){

		next_task = list_entry(list, struct task_struct, sibling); // defining the next operation to be operated upon using the list_entry macro
		printk(KERN_INFO "Name: %s | State: %ld | Pid: %d\n", next_task->comm, next_task->state, next_task->pid);  // prints the informatino wanted
		dfs_operation(next_task); // performs a dfs on the next process in the tree.

	}
}

/* This function is called when the module is loaded. */
int dfs_init(void){
	printk(KERN_INFO "Loading Module\n");
	dfs_operation(&init_task);  // starting the module with init_task
	printk(KERN_INFO "Module Loaded\n");
	return 0;
}

/* This function is called when the module is removed. */
void dfs_exit(void) {
	printk(KERN_INFO "Removing Module\n");
}

/* Macros for registering module entry and exit points. */
module_init(dfs_init);
module_exit(dfs_exit);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("DFS Module");
MODULE_AUTHOR("SGG");
