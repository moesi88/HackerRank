n = input()
str = input()

lst = str.split()
lst = map(int, lst)

t = tuple(lst)
print(hash(t))