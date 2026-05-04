lst = []
n = int(input())
for _ in range(n):
    command = input().split()
    cmd = command[0]
    
    if cmd == "insert":
        lst.insert(int(command[1]),int(command[2]))  
    elif cmd == "append":
        lst.append(int(command[1]))
    elif cmd == "remove":
        lst.remove(int(command[1]))
    elif cmd == "sort":
        lst.sort()
    elif cmd == "pop":
        lst.pop()
    elif cmd == "reverse":
        lst.reverse()
    elif cmd == "print":
        print(lst) 
        
        