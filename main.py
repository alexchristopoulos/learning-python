def wordCount():
    text = "Some text for testing the word count in in the the text text"

    dictionary = {}

    for word in text.split(" "):
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    print(dictionary.items())


def fib(n):
    if n < 2:
        print("n should be geater than 2")
    else:
        numbers = [1, 1, 2]

        for x in range(2, n + 1):
            numbers.append(numbers[x] + numbers[x - 1])

        return numbers[n + 1]


wordCount()
print(fib(10))
print(fib(14))
