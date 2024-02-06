'''
Name: main.py
Description: Piece to code to practice the usage of functions
Author: Emmanuel Uwaifo
Date created: Feb. 4th, 2024
Last modified: Feb. 4th, 2024
'''

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mymath
amount = 67.89

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("Hi, " + name)
    print("Hi, {}".format(name))


def multiply_two_nums(num1: int, num2: int) -> int:
    res = num1 * num2
    return res

def print_name_age(name: str, age: int):
    print("Name: {0}, Age: {1}".format(name, age))

def circle_area():
    '''
    Desc: Calculates the area of a circle
    :radius: radius of the circle
    :area: stores the area of a circle
    :return: area of a circle (float or int)
    '''

    # ask user for radius of circle
    radius = float(input("Enter radius: "))

    # calculates area of circle
    area = 3.142 * radius**2

    return area

def modulus(number, divisor):
    result = number % divisor
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    print_hi('PyCharm')
    ans = mymath.multiply_by_two(56)
    print(ans)
    result = modulus(9, 2)
    print_name_age("Frank", 32)
    print(result)
    result = circle_area()
    print(multiply_two_nums(5, 7))
    print(result)
    '''
    length = 50
    breadth = 60

    print("Area of a rectangle with length {} and breadth {} is {}".format(length, breadth, mymath.rectangle_perimeter(length, breadth)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
