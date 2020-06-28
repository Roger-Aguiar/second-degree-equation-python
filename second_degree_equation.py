# Name:         Roger Silva Santos Aguiar
# Function:     This module solves a complete second-degree equation.
# Initial date: June 28, 2020
# Last update:  June 28, 2020

# Required modules
import math;

class Second_degree_equation:
    def __init__(self, a, b, c):
        self.a = a;
        self.b = b;
        self.c = c;

    def calculateX1AndX2(self):
        delta = (self.b * self.b) - (4 * self.a * self.c);
        x1 = (-(self.b) + math.sqrt(delta)) / (2 * self.a);
        x2 = (-(self.b) - math.sqrt(delta)) / (2 * self.a);

        x1 = int(x1);
        x2 = int(x2);

        print("\n*************************Result*************************\n");

        print("The value of delta = {} " .format(delta));
        print("The value of X1 = {} " .format(x1));
        print("The value of X2 = {} " .format(x2));

if __name__ == '__main__':
    a = int(input("Enter a value for a: "));
    b = int(input("Enter a value for b: "));
    c = int(input("Enter a value for c: "));
    equation = Second_degree_equation(a, b, c);
    equation.calculateX1AndX2();