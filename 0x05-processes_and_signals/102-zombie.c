#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Programme that creates 5 zombie processes
 *
 * Return: 0
 */

int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}
		else
			return (0);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - Programme that creates an infinite wait loop
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
