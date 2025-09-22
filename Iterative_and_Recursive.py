#Alyce Gaines
#CIS261
#Iterative and Recursive

def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)

def factorial_iterative(num):
    fact = 1
    for number in range(2, num+1):
        fact = number * fact
    return fact

def main():
    print ("factorial results of an interactive function")
    print("0! =", factorial_iterative(0))
    print("2! =", factorial_iterative(2))
    print("4! =", factorial_iterative(4))
    print("6! =", factorial_iterative(6))
    print("8! =", factorial_iterative(8))
    print("10! =", factorial_iterative(10))
    print ("factorial results of a recursive function")
    print("0! =", factorial_recursive(0))
    print("1! =", factorial_recursive(1))
    print("3! =", factorial_recursive(3))
    print("5! =", factorial_recursive(5))
    print("7! =", factorial_recursive(7))
    print("9! =", factorial_recursive(9))

if __name__ == "__main__":
    main()