from hypothesis import *
from confidence_intervals import *
from line_of_best_fit import *
from factorials import *

def main():
    print("make a choice\n")
    print("1: hypothesis testing\n")
    print("2: confidence intervals\n")
    print("3: factorials\n")
    print("4: line of best fit\n")
    print("5: exit\n")

    choice = raw_input("> ")

    if choice == "1":
        hypo()
    elif choice == "2":
        confidence()
    elif choice == "3":
        factorial()
    elif choice == "4":
        lineitup()
    elif choice == "5":
        exit()
    else: 
        print("good god what have you done")

main()