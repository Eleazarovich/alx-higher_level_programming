#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of `listint_t` list
 * @h: points to listint_t
 *
 * Return: number of nodes
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *tmp;
	unsigned int n;

	tmp = h;
	n = 0;

	while (tmp != NULL)
	{
		printf("%i\n", tmp->n);
		tmp = tmp->next;
		n++;
	}
	return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of `listint_t` list
 * @head: points to listint_t
 * @n: value to insert in a node
 *
 * Return: address of the new elements or NULL if it fails
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listint - frees a `listint_t` list
 * @head: points to listint_t
 */

void free_listint(listint_t *head)
{
	listint_t *tmp;

	while (head != NULL)
	{
		tmp = head;
		head = head->next;
		free(tmp);
	}
}
























