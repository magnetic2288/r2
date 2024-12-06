a = ["a", "ab", "abc", "abcd", "12345", "123", "987654321"]
def Countchar(str):
    if len(str) <= 3:
        return True
    else:
        return False

a2 = filter(Countchar, a)

print(list(a2))