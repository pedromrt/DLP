list1 = [1,0,0,0,0,1]
list2 = [0,1,0,0,1,0]
list3 = [0,0,1,1,0,0]
list4 = [0,0,1,1,0,0]
list5 = [0,1,0,0,1,0]
list6 = [1,0,0,0,0,1]

matriz = [list1,list2,list3,list4,list5,list6]
print ("")

for i in range (0,len(matriz),1):
    for k in range (0,len (matriz[i]),1):
        print(matriz[i][k], end=" ")
    print("\n")