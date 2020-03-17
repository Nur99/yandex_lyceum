def palindrome(s):
    s = s.lower().replace(" ", "") 
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return 'Не палиндром'
    return 'Палиндром'
