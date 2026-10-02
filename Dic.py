dict = {1: "carrots", "two": [1, 2, 3], "three": 3}
print(dict)
print(dict.get(1))
print(dict.get("two"))
print(dict.get("three"))
dict[1] = "ONE"
dict[4] = "Four"
print(dict)
print(all({1: 2, 2: ".", "": 3}))
dict1 = {3: 3, 1: "one,4:4"}
print(dict1.get(1))
print(dict1.get(2))
print(dict1.get(2, "Not Found"))
print(dict1.get(5, 0))
dict1.clear()
print(dict1)
dict1 = {3: 3, 1: "one", 4: 4, 6: "seven"}
dict2 = dict1.copy()
print(dict2)
print(dict2.pop(3))
print(dict2)
print(dict2.pop(1))
tup = (1, 2, 3, 4, 5)
lis = ["a", "b", "c", "d", "e"]
print(list(zip(tup, lis)))
# dics={key: value for key , value in [1,14.25, 14,15.231]}
# dica=dict(enumerate([1,14.25, 14,15.231]))
# print(dica)
