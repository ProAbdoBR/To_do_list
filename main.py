todo = []


while True:
    action = input("what do you want to do?: (New task, View tasks, Remove task, Change task)")
    if action=="View tasks":
        if len(todo)==0:
            print("no tasks yet")
        else:
            for i in range(len(todo)):
                print(f"{i+1}- {todo[i]}")


    elif action == "New task":
        task= input("what task do you want to add?")
        todo.append(task)


    elif action=="Remove task":
        option = input("Do you want to remove 1 task, more, or all of them")
        if option=="1":
            number = int(input("Enter the number of the task you want to remove"))
            while not 0<=number-1<len(todo):
                number = int(input("Please enter a valid number"))
            todo.pop(number-1)
        elif option == "more" :
            num1 = int(input("Enter the number of the first task you want to remove"))
            while not 0<=num1-1<len(todo):
                num1 = int(input("Please enter a valid number"))
            num2 = int(input("The number of the last task you want to remove"))
            while not num1<=num2-1<len(todo):
                num2 = int(input("Please enter a valid number"))
            del todo[num1-1:num2]
        else:
            todo.clear()


    elif action=="Change task":
        number = int(input("What's the number of the task you want to change"))
        while not 0<=number-1<len(todo):
                number = int(input("Please enter a valid number"))
        change = input("Whay do you want to change it to")
        todo[number-1] = change


    elif action =="stop":
        print("OK, by")
        break


    else:
        print("Please enter a valid option.")