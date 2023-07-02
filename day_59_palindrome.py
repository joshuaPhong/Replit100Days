def clean(word):
    return word.strip().lower()


def my_palindrome():
    while True:
        print("Lets test for palindromes")
        word = input("Enter a word: ").replace(" ", "")
        word_reverse = word[::-1]
        if clean(word) == clean(word_reverse):
            print("It is a palindrome")
        else:
            print("Not a palindrome")


# from answer
# using a recursive function
def palindrome(word):
    # if the word has a length of zero or one it is a palindrome
    if len(word) <= 1:
        return True
    # check the first and last letters
    if word[0] != word[-1]:
        return False
    # call the function again with the first and last letters removed
    return palindrome(word[1:-1])


print(palindrome("racecar"))
