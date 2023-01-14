#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if sigly linked list is a cycle
 * @list: points to a sigly linked list
 * Return: 1 if cycle. otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (1)
	{
		if (first->next != NULL && first->next->next != NULL)
		{
			first = first->next->next;
			second = second->next;

			if (first == second)
				return (1);
		}
		else
			return (0);
	}
}
