myList = [-5, -23, 5, 0, 22, -6, 23, 67]
stack = []

while myList:
    mini = myList[0]  
    
    for i in myList: 
        if i < mini:
            mini = i
    stack.append(mini)
    myList.remove(mini)    

print (stack[-3::])