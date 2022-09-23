from ast import arguments


list = ["2244", "5566", "8899"]

# 在尾巴新增
list.append("3300")

# 多資料新增
list.extend(["aabb", "rrpp"])

# 重頭取資料
print(list[0])

# 可以倒數回來
print(list[-1])

# 計算list大小
print(len(list))

# List串接
list1 = ["234", "a234", "b234", "c234", "d234", "e234", "f234"]
list2 = ["1234", "a1234", "b1234", "c1234", "d1234", "e1234", "f1234"]
listAll = [list1, list2]
print(listAll)
