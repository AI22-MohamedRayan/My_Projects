#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <signal.h>

int main() {
    pid_t child_pid;

    // Fork a child process
    child_pid = fork();

    if (child_pid < 0) {
        // Error occurred
        fprintf(stderr, "Fork failed\n");
        return 1;
    } else if (child_pid == 0) {
        // Child process
        printf("Child process with PID: %d\n", getpid());
        
        // Execute a new program (replace "ls" with any other command)
        execlp("ls", "ls", "-la", NULL);
        
        // If execlp() fails
        fprintf(stderr, "execlp() failed\n");
        return 1;
    } else {
        // Parent process
        printf("Parent process with PID: %d\n", getpid());
        
        // Wait for the child process to terminate
        int status;
        waitpid(child_pid, &status, 0);
        printf("Child process terminated with status: %d\n", WEXITSTATUS(status));
        
        // Create a new process
        pid_t new_pid = fork();
        if (new_pid < 0) {
            // Error occurred
            fprintf(stderr, "Fork failed\n");
            return 1;
        } else if (new_pid == 0) {
            // New child process
            printf("New child process with PID: %d\n", getpid());
            
            // Do some processing here
            
            // Terminate the new child process
            exit(0);
        } else {
            // Parent process
            printf("Parent process with PID: %d\n", getpid());
            
            // Wait for the new child process to terminate
            waitpid(new_pid, NULL, 0);
            
            // Terminate the new child process using kill
            kill(new_pid, SIGTERM);
        }
    }

    return 0;
}
