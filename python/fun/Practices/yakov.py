
# x=4612861225953345
# def func(x):
#     summ=0
#     for i in range(16):
#         if i%2:
#             if x%10>4:
#                 summ+= (2 * (x % 10)) - 9
#             else:
#                 summ+= (x % 10) * 2
#         else:
#             summ+= x % 10
#         x//=10
#     return summ%10==0
# print(func(x))

# percent=10
# arr={'apple':100,'banana':80,'orange':90}
# def func (percent,dec):
#     for k,v in dec.items():
#         dec[k]=v*(1-percent/100)
#     return dec
# # print(func(percent,arr))
# c=lambda percent ,arr: {k:v*(1-percent/100) for k,v in arr.items()}
# print(c(percent,arr))

# arr = [5, 2, 9, 1, 5, 6, 3, 8, 4, 7]
# arr= [i if i%2 else i*i for i in arr ]
# print(arr)
# arr= [i for i in arr if i%2]
# print(arr)

# nums=[1001,2000,101,34,24,12,11,23]
# def func(x):
#     sum=0
#     cun=0
#     first_nu=0
#     while x>0:
#         cun+=1
#         if x<10:
#             first_nu=x
#         sum+=x%10
#         x//=10
#     return sum,cun,-first_nu
# nums.sort(key=func)
# print(nums)

# numbers = [4, -3, 7, -1, 0, 5, -6]
# positive =list(filter(lambda x:x>0,numbers))
# print(positive)

# num=["5","2","9","1","5","6","3","8","4","7"]
# result= sorted(num,key=lambda w:int(w))
# print(list(result))
#
# words = ["apple", "banana", "cherry", "date", "banana", "apple"]
# remove_words = ["apple", "date"]
# result= filter(lambda w:w not in remove_words,words)
# print(list(result))


