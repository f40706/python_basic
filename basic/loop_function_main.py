
# range使用於for，0~9
for i in range(0, 10):
    print(f"{i}")

# for使用list讀取
list = ["R2", "R4", "R6"]
for item in list:
    print(item)

#list變更index利用for
list = ["a2","a3","a4","a5","a6"]
list_index = [2,0,1,3,4]
list = [list[i] for i in list_index] 
print(list)

def printData():
    list = [2,3,4,5]
    print(list)
printData()

i = 0
while i < 10:
    i+=1
    print(f"---{i}")