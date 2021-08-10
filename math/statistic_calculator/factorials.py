from math_utils import *

def factorial():
    choice = raw_input("permutations (p) or combinations (c) ")
    choice = choice.strip()

    number_of_things = input("n: ")
    choice_of_things = input("r: ")

    if choice == "p":
        print("[+] WE ARE DOING PERMUTATIONS BUCKLE UP\n")
        print("[+] TOTAL NUMBER OF PERMUTATIONS " + str(permutations(number_of_things, choice_of_things)))
        print("\n[+] ALL DONE!")
    elif choice == "c":
        print("[+] WE ARE DOING COMBINATIONS KEEP YOUR HANDS INSIDE THE RIDE AT ALL TIMES\n")
        print("[+] TOTAL NUMBER OF COMBINATIONS " + str(combinations(number_of_things, choice_of_things)))
        print("\n[+] ALL DONE!")
    else:
        print("you entered something other than p or c try again plz")

    print("thanks for playing!")