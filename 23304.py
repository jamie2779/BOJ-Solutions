def isPal(s):
    l = len(s)
    if l == 1:
        return True
    else:
        if s == s[::-1] and isPal(s[:l//2]) and isPal(s[l-l//2:]):
            return True
        else:
            return False

s = input()
if(isPal(s)):
    print("AKARAKA")
else:
    print("IPSELENTI")