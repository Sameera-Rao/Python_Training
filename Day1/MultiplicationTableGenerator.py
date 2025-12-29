number=int(input("Enter number:"))
Range=int(input("Enter range of the table:"))
print(f"Multiplication table for {number}:")
for i in range(1, Range+1):
    print(f"{number}x{i}={number*i}")
