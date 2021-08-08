


a = [10, 12, 34, 36, 45, 48, 100, 90, 123, 123, 123, 124, 125]

def bin_search(a, key):
    start = 0
    end = len(a)
    while(start!=end):
        mid = (start + end)//2
        print(start, end, mid)
        if a[mid] == key:
            return mid
        if key > a[mid]:
            start = mid+1
        else:
            end = mid-1

    return -1

key = 125
idx = bin_search(a, key)
if  idx == -1:
    print('{} not found'.format(key))
else:
    print('{} found at idx = {}'.format(key, idx))