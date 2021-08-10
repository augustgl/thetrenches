from math_utils import *

list_xsquared = []
list_xy = []


# +======+ user input list prototypes

#lstx = []
#lsty = []

def makelistx():
    input_x = raw_input("enter list x with values seperated by a space ")
    lstx = input_x.split()

    floatlist = []
    
    for i in lstx:
        floatlist.append(float(i))

    return floatlist

def makelisty():
    input_y = raw_input("enter list y with values seperated by a space ")
    lsty = input_y.split()

    floatlist = []

    for i in lsty:
        floatlist.append(float(i))

    return floatlist 


def calc_xy(list_x, list_y): 
    for x, y in zip(list_x, list_y):
        list_xy.append(x * y)
    return

def calc_xsquared(lst):
    for x in lst:
        list_xsquared.append(x ** 2)
    return


def lineitup():
    
    x_list = makelistx()
    y_list = makelisty()

    print(y_list)
    print(x_list)

    calc_xy(x_list, y_list)
    calc_xsquared(x_list)

    slope = calc_slope(x_list, x_list, y_list, list_xy, list_xsquared)
    b = calc_b(x_list, y_list, x_list, slope)

    
    
    
    print("final equation: ")
    print("y = " + str(slope) + "x + " + str(b))
    