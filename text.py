# 1.Create a python program that displays the name of a user.
# 2. Put your code in a while loop to keep it coninuous.
# 3. Create a function that allows you to add and remove an item in a list. (Do some research on collections) I will give you the solution but try it your own way you must work together as a class to solve this.
# 4. Lastly your program must have a try catch.

from datetime import datetime

def function():
   
    items = []
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter item to add: ")
            items.append(item)
            print(items)
        elif choice == 2:
            print(items)
            item = input("Enter item to remove: ")
            items.remove(item)
            print(items)
        elif choice == 3:
            break
        elif choice == 4:
            print(items)
        
        else:
            print("Invalid choice")
        
function()