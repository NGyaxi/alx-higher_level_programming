#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *speed = list;

	if (!list)
		return (0);

	while (slow && speed && speed->next)
	{
		slow = slow->next;
		speed = speed->next->next;
		if (slow == speed)
			return (1);
	}

	return (0);
}
