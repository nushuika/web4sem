arr = []
n = int(input(""))
for _ in range(n):
    command = input().strip().split()
    if command[0] == "insert":
        index = int(command[1])
        value = int(command[2])
        arr.insert(index, value)
    elif command[0] == "print":
        print(arr)
    elif command[0] == "remove":
        value = int(command[1])
        arr.remove(value)
    elif command[0] == "append":
        value = int(command[1])
        arr.append(value)
    elif command[0] == "sort":
        arr.sort()
    elif command[0] == "pop":
        arr.pop()
    elif command[0] == "reverse":
        arr.reverse()