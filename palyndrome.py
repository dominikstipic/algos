def isPalindrome(x):
    x = str(x)
    n = len(x)//2
    if len(x) % 2 == 1:
        for i in range(n):
            if x[i] != x[len(x)-1-i]:
                return False
    else:
        i = 0
        while True:
            print(i, len(x)-1-i)
            if x[i] != x[len(x)-1-i]:
                return False
            if ((len(x)-1-i)-i) == 1:
                break 
            i += 1
    return True

bs = isPalindrome(11)