def f(x,y) :
    return x+y

l = list(range(1, 11))
l_2 = list(range(1, 11))
squares = list(map(f, l, l_2))

squares_2 = list(map(lambda x:x**2, range(1, 11)))
squares_3 = [x**2 for x in range(1, 11)]

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
adder = lambda x, y: x + y
print(adder(1, 2))
adder_result = list(map(lambda x, y: x + y, list_1, list_2))
print(adder_result)

print(squares)
print(squares_2)
print(squares_3)


m = [[1,2,3], [4, 5, 6], [7,8,9]]

mt = []
temp_list = []
for i in range(len(m[0])):
    temp_list = []
    print(temp_list)
    for row in m:
        temp_list.append(row[i])
    mt.append(temp_list)

print(m)
print(mt)

print(m[1][0])

