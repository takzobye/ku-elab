def count_char(word):
    result = {}

    for char in word:
        char = char.lower()

        if not char.isalpha():
            continue

        if char not in result:
            result[char] = 0

        result[char] += 1

    return result

print(count_char('Hello, There'))