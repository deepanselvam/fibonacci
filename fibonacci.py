def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

print("Enter the number")
num = int(input())
print(fibonacci(num))
