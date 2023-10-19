#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == None or password == None): return "Access denied";
    elif ((username == "ADMIN" or username == "admin") and password == "12345"):
        return "Access granted";
    else: return "Access denied";

def hows_the_weather(temperature):
    # your code here
    mymidpartstr = "";
    if (temperature < 40): mymidpartstr = "brisk";
    elif ((temperature == 40) or (40 < temperature and temperature < 65)):
        mymidpartstr = "a little chilly";
    elif ((temperature == 65) or (65 < temperature and temperature < 85)):
        mymidpartstr = "perfect";
    else: mymidpartstr = "too dang hot";
    return "It's " + mymidpartstr + " out there!";

def fizzbuzz(num):
    # your code here
    myretstr = "";
    if (num == None): return "";
    elif (type(num) != int and type(num) != float): return str(num);
    else: myretstr += ""; 
    if (num % 3 == 0): myretstr = "Fizz";
    else: myretstr = "";
    if (num % 5 == 0): myretstr += "Buzz";
    else: myretstr += "";
    if (len(myretstr) < 1): myretstr = num;
    else: myretstr += "";
    return myretstr;

def isnum(myvar):
    if (myvar == None): return False;
    elif (type(myvar) == int or type(myvar) == float): return True;
    else: return False;

def calculator(operation, num1, num2):
    # your code here
    if (isnum(num1) and isnum(num2)): pass;
    else: raise Exception("num1 and num2 must be numbers!");
    if (operation == None):
        print("Invalid operation!");
        return None;
    elif (len(operation) == 1): pass;
    else:
        print("Invalid operation!");
        return None;
    if (operation == "-"): return num1 - num2;
    elif (operation == "+"): return num1 + num2;
    elif (operation == "*"): return num1 * num2;
    elif (operation == "/"):
        if (num2 == 0): raise Exception("Cannot divide by zero (0)!");
        else: return num1 / num2;
    else:
        print("Invalid operation!");
        return None;
