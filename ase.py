def createlist():
    numlist =[]
    print("enter a number of the word 'end' to finish: ")
    i = 0
    while True:
        x=input()
        if not x.isnumeric():
            break
        numlist.append(int(x))
    return numlist

def maximum (list1):
    return max(list1), list1.index(max(list1))

max1,pos = maximum(createlist())

print('maximum is: ',max1,'\nPosition of max is: ', pos)
      


