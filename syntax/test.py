my_set = {'a','b','c', 1, 2, 3}
my_set1 = set()
my_set2 = set([1,2,3,4])  

# my_set.add('d')
# print(my_set) # {1, 2, 3, 'c', 'a', 'd', 'b'}
# my_set.clear()
# print(my_set) # set()

# remove(x)
# my_set.remove('d')
# print(my_set)
# my_set.remove('x')

el = my_set.pop()
print(el)
print(my_set)

# my_set.discard(2)
# print(my_set) # {1, 3, 'a', 'c', 'b'}
# my_set.discard(10) # 에러 없음

# my_set.update([1,4,5])
# print(my_set)