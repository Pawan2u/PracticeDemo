
def checkPalindrome(s):
    s1=s[::-1]
    if s==s1:
        return "Palindrome!"
    else:
        return "Not Palindrome!"

def reverseString(s):
    r=""
    for i in range(len(s)-1,-1,-1):
        r+=s[i]
    return r






s="102001"
print(checkPalindrome(s))
print(reverseString(s))