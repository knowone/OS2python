choice = int(input("‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐\n\
C A L C U L A T I O N S\n\
‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐\n\
1. Addition\n\
2. Subtraction\n\
3. Multiplication\n\
4. Division\n\
5. Floor Division\n\
6. Modulus\n\
7. Exponent\n\
‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐\n\
Enter your choice [1‐7] :\n"))
op1, op2 = map(int, input("enter the 2 operands\n").split())
if choice == 1:
    print(op1 + op2)
elif choice == 2:
    print(op1 - op2)
elif choice == 3:
    print(op1 * op2)
elif choice == 4:
    print(op1 / op2)
elif choice == 5:
    print(op1 // op2)
elif choice == 6:
    print(op1 % op2)
elif choice == 7:
    print(op1 ** op2)
else:
    print("Error")
