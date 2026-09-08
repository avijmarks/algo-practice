# Given a string s, return True if it is a palindrome after:

# converting all uppercase letters to lowercase
# removing all non-alphanumeric characters

# A palindrome reads the same forward and backward.

def valid_palindrome(s: str):
    s = s.lower()
    cleaned = ''.join(char for char in s if char.isalnum())

    backwards = cleaned[::-1]

    if cleaned == backwards:
        return True
    else:
        return False



s = "A man, a plan, a canal: Panamas"
print(valid_palindrome(s))