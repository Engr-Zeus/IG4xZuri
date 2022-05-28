# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word) == sorted(anagram)):
        return True
    else:
        return False


subject_word = input("Enter the Subject Word: ")
anagram_word = input("Enter the Anagram Word: ")
word = subject_word.lower()
anagram = anagram_word.lower()
print (find_anagram(word, anagram))
print(input("Press Enter to Terminate"))    

