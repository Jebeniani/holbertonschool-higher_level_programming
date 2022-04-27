#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: listint_t type
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmpr, *new;

	tmpr = list;
	new = list;
	while (tmpr != NULL && new != NULL && new->next != NULL)
	{
		new = new->next->next;
		tmpr = tmpr->next;
		if (new == tmpr)
			return (1);
	}
	return (0);
}
