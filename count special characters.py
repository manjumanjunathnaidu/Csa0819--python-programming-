def count_special_characters(statement):
    special_characters = 0

    for char in statement:
        # You can customize this condition based on your definition of special characters
        if not char.isalnum() and char != ' ':
            special_characters += 1

    return special_characters

# Example usage:
input_statement = "Hello! How are you today? #SpecialChars!$"

result = count_special_characters(input_statement)

print(f"Original statement: {input_statement}")
print(f"Number of special characters: {result}")
