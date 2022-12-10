
# 1
#
#
# a = [4,8,12,16,20]
# p = 8
# count = 0
# k = 0
# for i in a:
#     count +=1
#     if i==p:
#         print('found',p,'at',count,'position')
#         k = 1
#         break
# if k==0 : print('sorry not found')
#
#
# # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # 2
#
#
# a = [4,8,12,16,20]
# p = 9
# j = 0
# k = 0
# while j<len(a):
#     if a[j]==p:
#         print('found',p,'at',j+1,'position')
#         k = 1
#         break
#     j+=1
# if k==0 : print('sorry not found')
#
# # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # 3
#
# def search(list,word):
#     count = 0
#     for i in list:
#         count +=1
#         if i==word:
#             return True,count
#     return False,'none'
#
#
# list = [x for x in input('enter list\n').split()]
# word = input('enter element\n')
# a,b = search(list,word)
# if a: print('found',word,'at',b,'position')
# else: print('not found')


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# 4
# 4 3 2 6 5   5
def search(list,word):
    count = 0
    while count < len(list):
        if list[count]==word:
            return True,count
        count += 1
    return False,'none'


list = [x for x in input('enter list\n').split()]
word = input('enter element\n')
a,b = search(list,word)
if a: print('found',word,'at',b+1,'position')
else: print('not found')


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# def abc(x):
#     squ = x**2
#     return 'abc',squ
# print(abc(2))

