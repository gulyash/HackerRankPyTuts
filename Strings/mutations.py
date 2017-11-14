string = input()
index, character = input().split()
print(string[:int(index)] + character + string[int(index)+1:])
