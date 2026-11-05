str = "madam"
print(str == str[::-1])  # True

# def is_palindrome(text):
#     return text == text[::-1]

def is_palindrome(text):
    clean = ""
    for ch in text:
        if ch.isalnum():
            clean += ch.lower()
        # else:
        #     return False

    return clean == clean[::-1]

# def is_palindrome(s):
#     cleaned = ''.join(c.lower() for c in s if c.isalnum())
#     return cleaned == cleaned[::-1]


print(is_palindrome("Racecar"))  # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))  # False

print(is_palindrome("ma:dam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("a()\""))  # False