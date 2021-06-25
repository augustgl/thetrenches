# august GL
# stats class 
# 6/16/2021


# 2 sample hypothesis testing 


import scipy.stats as st # for z score and p value
import math # sqrt


# verify that we can do the test

def verify(n1, n2):
    if n1 >= 30:            # if n1 is greater than or equal to 30 check if n2 is 
        if n2 >= 30:        # if n2 is greater than or equal to 30, return true indicating we can do the test
            return True
        else:
            return False    # can't do it
    else:
        return False        # can't do it



# standard deviation formula 

def standard_deviation(s1, s2, n1, n2):
    thingy = (
        math.sqrt(
            (
                ((float(s1) ** 2) / float(n1)) + ((float(s2) ** 2) / float(n2))          
            )  
        )
    )

    return thingy

# z test
# uses the result from standard_deviation() 

def z_test(x1, x2, standard_deviation):
    test_statistic = (int(x1) - int(x2))    # x1 - x2 for test statistic 
    top_half = (int(test_statistic)) 


    z = top_half / standard_deviation       # divide by standard deviation

    return z                                # return result from z test


# function to figure out if it's right tailed, left tailed, or two tailed


def which_test(alt_hypo):           # alt_hypo is given in main()
    if alt_hypo == "notequal":      # if the alt hypothesis is not equal, it's two tailed
        result = "twotail" 
    elif alt_hypo == "greater":     # if the alt hypothesis is greater, it's right tailed
        result = "right"
    elif alt_hypo == "less":        # if the alt hypothesis is less, it's left tailed
        result = "left"
    else:
        print("could not decide which test") # this will execute if something somehow goes wrong. Don't type anything other than
        # notequal, greater, less
        # program won't be able to tell 
    
    print
    print(result) # print result for the user to see
    print
    return result # return which tail test it is

# main function

def main():
    print("[+] PLEASE ENTER ONE OF THE FOLLOWING OPTIONS WHEN STATING ALTERNATIVE HYPOTHESIS") 
    print     
    print("[*] notequal")       # two tailed
    print("[*] greater")        # right tailed
    print("[*] less")           # left tailed

    print("[+] PROGRAM WILL NOT WORK IF YOU ENTER ANYTHING ELSE\n")

    alt_hypothesis = raw_input("[>] state the alternative hypothesis: ") # get the alt hypothesis 
    n_one = raw_input("[>] state population sample 1 (N1): ") # values
    n_two = raw_input("[>] state population sample 2 (N2): ") # values
    x_one = raw_input("[>] state mean (X1): ") # values 
    x_two = raw_input("[>] state mean (X2): ") # values
    s_one = raw_input("[>] state standard deviation for population one (S1): ") # values 
    s_two = raw_input("[>] state standard deviation for population two (S2): ") # values
    alpha = raw_input("[>] state level of significance (alpha): ") # values

    # show what values will be plugged in

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

    # verify 

    ver = verify(int(n_one), int(n_two))

    if ver == True:                             # if verify() returns True  
        print("[+] we will proceed")            # continue
    elif ver == False:                          # if verify() returns False
        print ("[+] we will not proceed")       # can't do it chief
    else:
        print ("whoops")                        # something else went wrong. 
        exit()                                  # program exit

    deviation = standard_deviation(s_one, s_two, n_one, n_two)      # calculate standard deviation 
    z = z_test(x_one, x_two, deviation)                             # z test with x values, and return of the standard_deviation() function

    # output

    print ("[+] standard deviation: " + str(deviation))
    print ("[+] z score: " + str(z))


    which_tail = which_test(alt_hypothesis)             # determine which test it is

    if which_tail == "right":                           # if which_test returns "right"
        p_value = 1 - (st.norm.sf(abs(float(z))))       # calculate p value for the right tailed test
    elif which_tail == "left":                          # if which_test returns "left"
        p_value = st.norm.sf(abs(float(z)))             # calculate p value for left tailed test
    elif which_tail == "twotail":                       # if which_test returns "twotail"
        p_value = ((1/2) * (st.norm.sf(abs(float(z))))) # calculate p value for two tailed test

    print ("[+] p value: " + str(p_value))              # output

    # determine if in rejection region 

    if (p_value < alpha):           # not in rejection region
        print("FAIL TO REJECT!\n")  # fail to reject
    elif (p_value > alpha):         # in rejection region
        print("REJECT!\n")          # reject
    else: 
        print("whoops")             # whoops


    print("THANKS FOR PLAYING!!!")
    print
    print("HUGS ARE WORTH MORE THAN HANDSHAKES")


    exit() # exit program gracefully 


main() # call that bitch