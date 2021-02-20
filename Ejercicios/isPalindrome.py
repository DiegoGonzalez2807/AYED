from sys import stdin

def isPalindrome(word):
    is_palindrome = True
    wordLen = len(word)
    for index in range(wordLen//2):
        is_palindrome = is_palindrome and (word[index] == word[wordLen-(index+1)])
    return is_palindrome

def main():
    word = stdin.readline().strip()
    while word:
        print(isPalindrome(word))
        word = stdin.readline().strip()

main()