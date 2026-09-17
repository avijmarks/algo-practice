# Try LeetCode #20 — Valid Parentheses.

# Given a string s containing only:

# ( ) { } [ ]

# Return True if the string is valid.

# A string is valid if:

# every opening bracket is closed by the same type of bracket
# brackets are closed in the correct order
# every closing bracket has a corresponding opening bracket

def valid_parentheses(s: str):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []

    for char in s:
        if char not in pairs:
            stack.append(char)
        else:
            if not stack:
                return False
            
            last_brace = stack.pop()
            if pairs[char] != last_brace:
                return False

    if stack:
        return False

    return True


s = "{()}(])"
print(valid_parentheses(s))