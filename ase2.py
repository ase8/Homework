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

def minimum (list1):
    return min(list1), list1.index(min(list1))

newlist = createlist()
max1,pos = maximum(newlist)
print('maximum is: ',max1,'\nPosition of max is: ', pos)

minn,pos = minimum(newlist)
print('minimum is: ',minn,'\nPosition of min is: ', pos)
      


