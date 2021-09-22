l = int(input("digite a largura: "))
a = int(input("digite a altura: "))
j = a
while(j > 0):
    i = l
    if(j == a or j == 1):
        while(i > 0):
            print("#", end = "")
            i = i-1
    else:
        print("#", end = "")
        while(i > 2):
            print(" ", end = "")
            i = i-1
        print("#", end = "")
    print()
    j = j-1
