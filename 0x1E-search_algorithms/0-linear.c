#include "search_algos.h"

/**
 * linear_search - Searches for value in arry
 *              
 * @array: A pointer to the first element of the array
 * @size: number of elements in the array
 * @value: The value to search for.
 *
 * Return: If  value is not present or the array is NULL, -1.
 *
 *
 * 
 */
int linear_search(int *array, size_t size, int value)
{
	size_t iter;

	if (array == NULL)
		return (-1);
	for (iter = 0; iter < size; iter++)
	{
		printf("Value checked array[%ld] = [%d]\n", iter, array[iter]);
		if (array[iter] == value)
			return (iter);
	}
	return (-1);
}
