
#Attept a
def isPerfectSquare(n):
    if n <= 1:
        return True

    start = 0
    end = n//2
    while((end - start) > 1):

        mid = (start + end)//2

        sq = mid*mid
        print(mid, sq, start, end)
        if sq == n:
            return True
        if sq > n:
            end = mid
        if sq < n:
            start = mid
    return False


s = 1111*1111
print(isPerfectSquare(s))


