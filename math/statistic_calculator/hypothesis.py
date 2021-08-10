from math_utils import *

import scipy.stats as st

def verify(n1, n2):
    if n1 >= 30:
        if n2 >= 30:
            return True
        else:
            return False
    else:
        return False

def hypo():
    print("[+] PLEASE ENTER ONE OF THE FOLLOWING OPTIONS WHEN STATING ALTERNATIVE HYPOTHESIS")   
    print     
    print("[*] notequal")
    print("[*] greater")
    print("[*] less")
    print("[+] PROGRAM WILL NOT WORK IF YOU ENTER ANYTHING ELSE\n")

    alt_hypothesis = input("[>] state the alternative hypothesis: ")
    n_one = input("[>] state population sample 1 (N1): ")
    n_two = input("[>] state population sample 2 (N2): ")
    x_one = input("[>] state mean (X1): ")
    x_two = input("[>] state mean (X2): ")
    s_one = input("[>] state standard deviation for population one (S1): ")
    s_two = input("[>] state standard deviation for population two (S2): ")
    alpha = input("[>] state level of significance (alpha): ")

    print
    print("[+] VARIABLES!")
    print ("[+] N1: " + n_one)
    print ("[+] N2: " + n_two)
    print
    print ("[+] X1: " + x_one)
    print ("[+] X2: " + x_two)
    print
    print ("[+] S1: " + s_one)
    print ("[+] S2: " + s_two)
    print
    print ("[+] alpha: " + alpha)
    print 
    print ("[+] verifying that we can do the experiment")

    ver = verify(int(n_one), int(n_two))

    if ver == True: 
        print("[+] we will proceed")
    elif ver == False: 
        print ("[+] we will not proceed")
    else:
        print ("whoops")

    deviation = standard_deviation(s_one, s_two, n_one, n_two)
    z = z_test(x_one, x_two, deviation)

    print ("[+] standard deviation: " + str(deviation))
    print ("[+] z score: " + str(z))

    which_tail = which_test(alt_hypothesis)

    if which_tail == "right":
        p_value = 1 - (st.norm.sf(abs(float(z))))
    elif which_tail == "left":
        p_value = st.norm.sf(abs(float(z)))
    elif which_tail == "twotail":
        p_value = ((1/2) * (st.norm.sf(abs(float(z)))))

    print ("[+] p value: " + str(p_value))

    if (p_value < alpha):
        print("FAIL TO REJECT!\n")
    elif (p_value > alpha):
        print("REJECT!\n")
    else: 
        print("whoops")

    exit()