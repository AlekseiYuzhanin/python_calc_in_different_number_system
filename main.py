def convert_number(num, base):
    digits = "0123456789ABCDEF"
    if num < base:
        return digits[num]
    else:
        return convert_number(num//base, base) + digits[num%base]

def add_numbers(num1, num2, base):
    return convert_number(int(num1, base) + int(num2, base), base)

def subtract_numbers(num1, num2, base):
    return convert_number(int(num1, base) - int(num2, base), base)

def multiply_numbers(num1, num2, base):
    return convert_number(int(num1, base) * int(num2, base), base)

def divide_numbers(num1, num2, base):
    return convert_number(int(num1, base) // int(num2, base), base)

def main():
    while True:
        print("Enter two numbers and a base (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal):")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        base = int(input("Base: "))  
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter choice (1/2/3/4): "))

        if choice == 1:
            result = add_numbers(num1, num2, base)
            print("Result:", result)
        elif choice == 2:
            result = subtract_numbers(num1, num2, base)
            print("Result:", result)
        elif choice == 3:
            result = multiply_numbers(num1, num2, base)
            print("Result:", result)
        elif choice == 4:
            try:
                result = divide_numbers(num1, num2, base)
                print("Result:", result)
            except ZeroDivisionError:
                print("Cant divide on zero!")   
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()        
