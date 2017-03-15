num = int(input("‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐\n\
M A I N ‐ M E N U \n\
‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐ \n\
1. Good\n\
2. Good luck\n\
3. Excellent\n\
‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐\n\
Enter your choice [1‐3] :\n"))
if 1 <= num <= 3:
    if num == 1:
        print("Good...")
    elif num == 2:
        print("Good luck...")
    else:
        print("Excellent...")
else:
    print("Error")
