# BINARY SEARCH

def search(lst,p):
    l = 0
    u = len(lst)-1
    while l<=u:
        m = (l+u)//2
        if lst[m]==p:
            return True,m+1
        else:
            if lst[m]<p: l = m+1
            if lst[m]>p: u = m-1
    return False,'none'



lst = [int(x) for x in input('enter list\n').split()]     # [2,4,1,3,21,32]
lst.sort()
print(lst)                                                # [1,2,3,4,21,32]
p = int(input('enter number to search\n'))
a,b = search(lst,p)
if a: print('found at location',b)
else: print('not found')


