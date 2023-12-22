"""Task 1
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
 and the number of occurrences as values. """
def count_words(sentence: str) -> dict:
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
print(count_words("the surreptitious thief stole the precious diamond from the museum."))
