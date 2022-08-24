#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Inserts a node in an organized linked list
 * @head: head node
 * @number: number to insert
 *
 * Return: New node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = *head;

	new = malloc(sizeof(listint_t));
	if (!new || !head)
		return (NULL);
	new->n = number;
	/* if the value of head is equal to NULL then we place new before it */
	if (!*head)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (temp)
	{
		if ((temp->n <= number) && (temp->next && (temp->next->n >= number)))
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		else if (temp->n <= number && !(temp->next))
		{
			new->next = NULL;
			temp->next = new;
			return (new);
		}
		/* when the number is smaller than heads value */
		/* then we insert it before head and do stuff */
		else if (temp->n > number)
		{
			new->next = temp;
			*head = new;
			return (new);
		}
		temp = temp->next;
	}
	return (NULL);
}
