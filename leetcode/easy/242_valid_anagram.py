def valid_anagram(s, t):

    chars_s = {}

    for char_num in s:
        if char_num in chars_s:
            chars_s[char_num] += 1
        else:
            chars_s[char_num] = 1

    seen = set()

    for char in t:
        if char not in seen:
            seen.add(char)

            if char in chars_s:
                if not t.count(char) == chars_s[char]:
                    return False
                del chars_s[char]
            else:
                return False

    if len(chars_s) > 0:
        return False

    return True

# def valid_anagram(s,t): 
#     seen = set()

#     valid = True

#     if len(s) != len(t):
#         return False

#     for char in s:
#         num_in_s = get_num_chars(char, s)

#         if char in t:
#             num_in_t = get_num_chars(char, t)

#             if num_in_s != num_in_t:
#                 return False
#         else:
#             return False

#     return valid

# def get_num_chars(char, word):
#     num = 0
#     for c in word:
#         if c == char:
#             num += 1

#     return num


s = "anagram"
t = "nagaram"

print(valid_anagram(s,t))