#Name:          Roger Silva Santos Aguiar
# Function:     This application solves a second-degree equation.
# Initial date: June 28, 2020
# Last update:  June 28, 2020

# Required modules
import second_degree_equation;

class Main:
    if __name__ == '__main__':
        print("This application solves a second degree equation. Enter the following required data:\n");

        a = int(input("Enter a value for a: "));
        b = int(input("Enter a value for b: "));
        c = int(input("Enter a value for c: "));
        equation = second_degree_equation.Second_degree_equation(a, b, c);
        equation.calculateSecondDegreeEquation();