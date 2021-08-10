# math functions 

import time
import math 

# z scores for different confidence levels

zscore_90 = 1.645
zscore_95 = 1.960
zscore_99 = 2.576 

# hypothesis testing functions

def standard_deviation(s1, s2, n1, n2):
    thingy = (
        math.sqrt(
            (
                ((float(s1) ** 2) / float(n1)) + ((float(s2) ** 2) / float(n2))          
            )  
        )
    )

    return thingy

def z_test(x1, x2, standard_deviation):
    test_statistic = (int(x1) - int(x2))
    top_half = (int(test_statistic))

    z = top_half / standard_deviation
    return z

def which_test(alt_hypo):
    if alt_hypo == "notequal":
        result = "twotail"
    elif alt_hypo == "greater":
        result = "right"
    elif alt_hypo == "less":
        result = "left"
    else:
        print("could not decide which test")
    
    print
    print(result)
    print
    return result


# line of best fit

def calc_slope(list_x, x, y, xy, x2):
    size = len(list_x)

    sigma_xy = float(sum(xy))
    sigma_xsquared = float(sum(x2))
    sigma_x = float(sum(x))
    sigma_y = float(sum(y))

    tophalf = (size * sigma_xy - (sigma_x * sigma_y))
    bottomhalf = (size * sigma_xsquared - (sigma_x ** 2))

    slope = tophalf / bottomhalf

    return slope


def calc_b(list_x, y, x, m):
    size = len(list_x)

    sigma_y = float(sum(y))
    sigma_x = float(sum(x))

    tophalf = (sigma_y - (m * sigma_x))
    
    b = tophalf / size
    return b



# factorials

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i 
    
    return fact

def permutations(n, r):
    numerator = factorial(int(n))
    denominator = int(n) - int(r) 
    factorial_of_denom = factorial(denominator)

    return numerator / factorial_of_denom

def combinations(n, r):
    numerator = factorial(int(n)) 
    denominator = factorial(int(r)) * factorial(int(n) - int(r))

    return numerator / denominator


# margin of error, confidence intervals

def margin_of_error(zscore, mean, s, n, plus):
    if (plus == True):
        return mean + (zscore * (s / math.sqrt(n)))
    if (plus == False):
        return mean - (zscore * (s / math.sqrt(n)))
    else:
        return "whoops :p"
        exit()
