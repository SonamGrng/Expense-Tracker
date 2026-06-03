#use lists to store categories of the expenses, 3 lists for each category, then each list item is stored into a csv file 
import csv 
expenses = []
amounts = []
descriptions = []

def addExpense():
    category = input("Enter the category: ")
    amount = float(input("Enter the ammount: "))
    description = input("Enter the discription: ") 
    expenses.append(category)
    amounts.append(amount)
    descriptions.append(description)
    with open("expenses.csv","a",newline="")as file:#note no need to close the file due to with keyword 
        writer=csv.writer(file)
        writer.writerow([category,amount,description])
    

    
    

    
    
    

def checkTotalExpense():
    total = 0
    with open("expenses.csv","r",newline="")as file: 
        reader = csv.reader(file)
        for row in reader: 
            total += float(row[1])

    print("Total expenses: $",total)








print("1.Enter an expense")
print("2.Check total of expenses so far")
print("3.Exit")
option = input("Enter which option you would like to choose: ")
while option != "3":
    if(option == "1"):
        addExpense()
    if (option == "2"): 
        checkTotalExpense()
    print("1.Enter an expense")
    print("2.Check total of expenses so far")
    print("3.Exit")
    option = input("Enter which option you would like to choose: ")
print("Program now closing!")#left the while loop 