num = int(input("Enter a number less than 25")) 
if num >= 25:
    print("Error")
else :
    for num in range(num, 25):
	    print(f"Inside the loop, my variable is {num}")
