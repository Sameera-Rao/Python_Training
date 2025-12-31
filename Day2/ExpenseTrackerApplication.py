expenses=[]
num_days=int(input("Enter number of days:"))

for i in range(1, num_days+1):
    amount=float(input(f"Enter expense for Day {i}:"))
    expenses.append(amount)

total=0
minimum=expenses[0]
maximum=expenses[0]

for expense in expenses:
    total+=expense
    if expense<minimum:
        minimum=expense
    if expense>maximum:
        maximum=expense

average=total/len(expenses)

print("Expense Report")
print(f"Total Expenses:{total:}")
print(f"Average Expense:{average:}")
print(f"Minimum Expense:{minimum:}")
print(f"Maximum Expense:{maximum:}")

