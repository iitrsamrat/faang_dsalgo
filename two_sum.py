


a = [1, 2, 3, 4, 56, 10]

#Brute Force O(n2)
def twoSum(a, target):
    if len(a) <= 1:
        return None
    n = len(a)
    for i in range(0, n):
        num_to_find = target - a[i]
        for j in range(i+1, n):
            if a[j] == num_to_find:
                return [i, j]
    return None


#Brute Force O(n2)
def twoSumUsingSet(a, sum):
    if len(a) <= 1:
        return None
    n = len(a)
    d = dict()
    d[a[0]] = 0
    for i in range(1, n):
        num_to_find = abs(sum - a[i])
        print(i, d, num_to_find)
        if num_to_find in d.keys():
            return [d[num_to_find], i]
        d[a[i]] = i

    return None

print(twoSum(a, 7))
print(twoSumUsingSet(a, 10))