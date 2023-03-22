import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

def convert_number(num, base):
    digits = "0123456789ABCDEF"
    if base == 2 or base == 8 or base == 10 or base == 16:
        if num < base:
            return digits[num]   
        else:
            return convert_number(num//base, base) + digits[num%base]
    else:
        return f"Base {base} out of range!"
    
def add_numbers(num1, num2, base):
    try:
        return convert_number(int(num1, base) + int(num2, base), base)
    except ValueError:
        return f"Number {num1} or {num2} isnt availabe in this count system!"
    
def subtract_numbers(num1, num2, base):
    try:
        return convert_number(int(num1, base) - int(num2, base), base)
    except ValueError:
        return f"Number {num1} or {num2} isnt availabe in this count system!"
    
def multiply_numbers(num1, num2, base):
    try:
        return convert_number(int(num1, base) * int(num2, base), base)
    except ValueError:
        return f"Number {num1} or {num2} isnt availabe in this count system!"
    
def divide_numbers(num1, num2, base):
    try:
        return convert_number(int(num1, base) // int(num2, base), base)
    except ValueError:
        return f"Number {num1} or {num2} isnt availabe in this count system!"
    except ZeroDivisionError:
        return "You cant divide on zero!"
    
def rem_numbers(num1,num2,base):
    try:
        return convert_number(int(num1, base) % int(num2, base), base)
    except ValueError:
        return f"Number {num1} or {num2} isnt availabe in this count system!"
    except ZeroDivisionError:
        return "You cant divide on zero!"
    
def main():
    while True:
        print("What you want to do? \n 1: Calculate \n 2: Build a diagram \n 3: Check csv file \n 4: Quit")
        action_choice = int(input())
        if action_choice == 1:
            print("Enter two numbers and a base (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal):")
            num1 = input("First number: ")
            num2 = input("Second number: ")
            base = int(input("Base: "))
            result_array = []
            nums_array = [num1,num2,base]
            result_array.append(nums_array)
            with open("file.csv","a+") as file:
                writer = csv.writer(file)
                writer.writerows(result_array)
   
            print("Choose an operation: \n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Remainder of the division ")
            choice = int(input("Enter choice (1/2/3/4/5): "))

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
                result = divide_numbers(num1, num2, base)
                print("Result:", result)
            elif choice == 5:
                result = rem_numbers(num1,num2,base)
                print("Result:",result)           
            else:
                print("Invalid choice!")
        elif action_choice == 2:
            df = pd.read_csv('file.csv')
            base_nums = df['Base']
            binary_nums = base_nums[df['Base'] == 2].count()
            octal_nums = base_nums[df['Base'] == 8].count()
            ten_nums = base_nums[df['Base'] == 10].count()
            hex_nums = base_nums[df['Base'] == 16].count()

            x = np.array(['Binary numbers','Octal numbers','Ten numbers','Hex numbers'])
            y = np.array([binary_nums,octal_nums,ten_nums,hex_nums])

            plt.bar(x,y)
            plt.show()
        elif action_choice == 3:
            df = pd.read_csv("file.csv")
            print(df)
        elif action_choice == 4:
            return None


if __name__ == "__main__":
    main()     