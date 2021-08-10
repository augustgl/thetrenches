from math_utils import *

zscore_90 = 1.645
zscore_95 = 1.960
zscore_99 = 2.576

def confidence():
    n = input("[>] please enter the number of trials (n): ")
    n_int = int(n)

    print

    s = input("[>] please enter the standard deviation (s): ")
    s_int = int(s)

    print

    print("[*] IMPORTANT: CONFIDENCE INTERVAL MUST BE A DECIMAL. IF YOU ENTER AS AN INTEGER (WHOLE NUMBER) THE PROGRAM WILL NOT WORK CORRECTLY.\n")

    confidence_lvl = input("[>] please enter the confidence level as a decimal (c) (.95, .99, .90): ")
    confidence_lvl_int = float(confidence_lvl)

    print 

    x = input("[>] please enter the mean (x): ")
    x_int = int(x)

    print

    print("[+] VARIABLES\n")
    print("[.] NUMBER OF TRIALS: " + str(n))
    print("[.] STANDARD DEVIATION: " + str(s))
    print("[.] CONFIDENCE LEVEL: " + str(confidence_lvl))
    print("[.] MEAN: " + str(x))

    print

    print("[+] CHECKING IF WE CAN DO THE EXPIREMENT\n")

    if n_int >= 30:
        print("[+] N WAS GREATER THAN OR EQUAL TO 30. WE CAN DO IT!\n")
    else:
        print("[+] N WAS LESS THAN 30. EXITING.")
        exit()

    print


    if(confidence_lvl_int == .99):
        z = zscore_99
        margin_plus = margin_of_error(z, x_int, s_int, n_int, True)
        margin_minus = margin_of_error(z, x_int, s_int, n_int, False)

        print("[.] MARGIN OF ERROR ADDED: " + str(margin_plus) + "\n")
        print("[.] MARGIN OF ERROR SUBTRACTED " + str(margin_minus)  + "\n")

    if(confidence_lvl_int == .95):
        z = zscore_95
        margin_plus = margin_of_error(z, x_int, s_int, n_int, True)
        margin_minus = margin_of_error(z, x_int, s_int, n_int, False)

        print("[.] MARGIN OF ERROR ADDED: " + str(margin_plus) + "\n")
        print("[.] MARGIN OF ERROR SUBTRACTED " + str(margin_minus)  + "\n")

    if(confidence_lvl_int == .90):
        z = zscore_90
        margin_plus = margin_of_error(z, x_int, s_int, n_int, True)
        margin_minus = margin_of_error(z, x_int, s_int, n_int, False)

        print("[.] MARGIN OF ERROR ADDED: " + str(margin_plus) + "\n")
        print("[.] MARGIN OF ERROR SUBTRACTED " + str(margin_minus)  + "\n")



    