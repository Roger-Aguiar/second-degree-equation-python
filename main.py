#Name:          Roger Silva Santos Aguiar
# Function:     This application solves a second-degree equation.
# Initial date: June 28, 2020
# Last update:  June 29, 2020

# Required modules
import second_degree_equation;

class Main:
    if __name__ == '__main__':
        print("This application solves a second degree equation.");

        def menu(self):
            print("\n****************************Options****************************\n");
            print("1 - Solve a new second degree equation");
            print("2 - Exit");

        def solveEquation(self):
            a = int(input("Enter a value for a: "));
            b = int(input("Enter a value for b: "));
            c = int(input("Enter a value for c: "));
            equation = second_degree_equation.Second_degree_equation(a, b, c);
            equation.calculateSecondDegreeEquation();

equation = Main();
equation.menu();

option = int(input("Choose an option: "));
while option == 1:
    equation.solveEquation();
    equation.menu();
    option = int(input("Choose an option: "));

if option == 2:
    print("End program.");