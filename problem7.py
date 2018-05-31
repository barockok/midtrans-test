n = int(input())
name = list()

for i in range(n):
    cmd = input().split(" ")

    if(cmd[0]=="add"):
        name.append(cmd[1])
    elif(cmd[0]=="find"):
        word = cmd[1]
        count = 0
        for j, nm in enumerate(name):
            if(word==nm[:len(word)]):
                count = count+1
        print(count)