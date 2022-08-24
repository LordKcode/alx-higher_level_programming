#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if there is a loop in a linked list
 * @list: list of nodes
 *
 * Return: 1 if there is a loopk 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL;
	listint_t *fast = NULL;

	if (!list || !list->next)
		return (0);

	slow = list;
	fast = list->next;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
