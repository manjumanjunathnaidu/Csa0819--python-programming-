def remove_duplicates(sorted_array):
    if not sorted_array:
        return []

    unique_elements = [sorted_array[0]]

    for i in range(1, len(sorted_array)):
        if sorted_array[i] != sorted_array[i - 1]:
            unique_elements.append(sorted_array[i])

    return unique_elements

# Example usage:
sorted_array = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]

result = remove_duplicates(sorted_array)

print("Original sorted array:", sorted_array)
print("Array after removing duplicates:", result)
