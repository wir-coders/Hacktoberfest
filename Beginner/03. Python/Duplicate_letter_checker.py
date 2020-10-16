"""
Edabit Challenge
https://edabit.com/challenge/WS6hR6b9EZzuDTD26

This function identifies if any word in a string contains duplicate letters.
If there are no duplicate letters it returns True, otherwise False.
"""
def no_duplicate_letters(phrase):
	split_phrase = phrase.split()
	for word in split_phrase:
		for letter in word:
			if word.lower().count(letter.lower()) > 1:
				return False
	return True

### Testing
# print(no_duplicate_letters("Hacktoberfest is fun!"))
# print(no_duplicate_letters("This word has duplicates: letters"))
# print(no_duplicate_letters("This word no duplicates: subtle"))