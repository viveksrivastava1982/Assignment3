def factorial(num):
    result =1
    for i in range (1,num+1):
        result=result * i

    return result
    

num =5
fact=factorial(num)
print(f"Factorial of {num} is: {fact}")
