# stats class
# confidence intervals for 90% 95% and 99% 

import time
import math


# ========= CODE STARTS HERE ========= #


# z scores corresponding with confidence levels
# add your own values for other z scores

zscore_90 = 1.645 # z score for 90%
zscore_95 = 1.960 # z score for 95%
zscore_99 = 2.576 # z score for 99%

# ========= MARGIN OF ERROR ========= #

# function to calculate the margin of error
# the plus variable is to figure if we're adding or subtracting
# because you need two values

def margin_of_error(zscore, mean, s, n, plus):
    if (plus == True): # plus is a boolean where True = we are adding and False = we are subtracting
    	# add
        return mean + (zscore * (s / math.sqrt(n)))
    if (plus == False):
        # subtract
        return mean - (zscore * (s / math.sqrt(n)))
    else:
        return "whoops :p"

# ========= AUTOMATIC SUMMARY ========= #

def autosummarize(confidence, plus, minus):
	if (confidence == ".99"):
		confidence_percent = "99%"
	elif(confidence == ".95"):
		confidence_percent = "95%"
	elif(confidence == ".90"):
		confidence_percent = "90%"	

	print("\n I, the program...")
	time.sleep(1)
	
	print("\n can say...")
	time.sleep(2)
	
	print("\nwith " + confidence_percent + " confidence...")
	time.sleep(3)

	print("\n THAT THE MEAN IS SOMEWHERE BETWEEN " + str(plus) + " AND " + str(minus))
	time.sleep(1)

	print("\n*heavy breathing*")
	time.sleep(3)

	print("...... so there you have it.")


# ========= MAIN FUNCTION ========= #

def main():
    n = input("[>] please enter the number of trials (n): ")    
    n_int = int(n)
    print

    s = input("[>] please enter the standard deviation (s): ")
    s_int = int(n)

    print("[*] IMPORTANT: CONFIDENCE INTERVAL MUST BE A DECIMAL. IF YOU ENTER AS AN INTEGER (WHOLE NUMBER) THE PROGRAM WILL NOT WORK CORRECTLY.\n")
    
    confidence_lvl = input("[>] please enter the confidence level as a decimal (c) (.95, .99, .90): ")
    confidence_lvl_float = float(confidence_lvl)
    print

    x = input("[>] please enter the mean (x): ")
    x_int = int(x)
    print

    # read back variables

    print("[+] VARIABLES\n")
    print

    print("[.] NUMBER OF TRIALS: " + n)
    print("[.] STANDARD DEVIATION: " + s)
    print("[.] CONFIDENCE LEVEL: " + confidence_lvl)
    print("[.] MEAN: " + x)

    print

    print("[+] CHECKING IF WE CAN DO THE EXPERIMENT...\n")

    # this cannot be done if the number of trials is less than 30

    if n_int >= 30:
        print("[+] N WAS GREATER THAN OR EQUAL TO 30. SO YOU'RE NOT AS DUMB AS YOU LOOK!\n")
    else: 
        print("[-] N WAS LESS THAN 30. FUCK YOU.")
        exit()

    # all of the calculations for the different confidence levels

    if (confidence_lvl == ".99"):
        z = zscore_99
        margin_plus = margin_of_error(z, x_int, s_int, n_int, True)
        margin_minus = margin_of_error(z, x_int, s_int, n_int, False)

        print("[+] " + str(margin_minus) + " TO " + str(margin_plus))

    elif (confidence_lvl == ".95"):
        z = zscore_95
        margin_plus = margin_of_error(z, x_int, s_int, n_int, True)
        margin_minus = margin_of_error(z, x_int, s_int, n_int, False)

        print("[+] " + str(margin_minus) + " TO " + str(margin_plus))

    elif (confidence_lvl == ".90"):
        z = zscore_90
        margin_plus = margin_of_error(z, x_int, s_int, n_int, True)
        margin_minus = margin_of_error(z, x_int, s_int, n_int, False)

        print("[+] " + str(margin_minus) + " TO " + str(margin_plus))

    else: 
        print("I told you to only enter one of the three confidence levels. you didn't do that. Now you must live with your own failure. goodbye. I hope some day you find something to replace the shell of a human that you currently are.\n")

    autosummarize(confidence_lvl, margin_plus, margin_minus)


main()