
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

a, b, c, d, *other, e = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a) # 1
print(b) # 2
print(c) # 3 
print(d) # 4
print(other) # [5, 6, 7, 8]
print(e) # 9