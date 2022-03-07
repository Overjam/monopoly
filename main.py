import datetime as dt
import random
import time

login = input("Hello Sir please enter your name:  ")
if login == "Jamie":
    print("Welcome Sir")
    while True:
        service = input("What do you want Jamie   ")
        time = dt.datetime.now()
        date = time.strftime("%A")
        if service == "date":
            print(date)
        if service == "menu":
            if date == "Monday":
                print("You are having Spagettii today")
            if date == "Tuesday":
                print("You are having Cottage Pie today")
            if date == "Wednesday":
                print("You are having Curry today")
            if date == "Thursday":
                print("You are having Chicken Kievs today")
            if date == "Friday":
                print("You are having Pizza today")
        if service == "timetable":
            if date == "Monday":
                print("Science Lab 3\n ", "Pre K2\n", "Dt T3\n", "Maths Room 17\n", "Buisness C2\n")
            if date == "Tuesday":
                print("You are having Cottage Pie today")
            if date == "Wednesday":
                print("You are having Curry today")
            if date == "Thursday":
                print("You are having Chicken Kievs today")
            if date == "Friday":
                print("You are having Pizza today")
        if service == "cal":
            calculator = input("What Method Do you want")
            if calculator == "multi":
                num1 = int(input("Please Enter Your First Number:  "))
                num2 = int(input("Please Enter Your Second Number"))
                print(num1 * num2)
            if calculator == "sub":
                print(num1 - num2)
            if calculator == "add":
                print(num1 + num2)
            if calculator == "division":
                print(num1 / num2)
        if service == "random":

            x = random.randint(1,100)
            print(x)









else:
    print("Not Sir, self destructing")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(0.5)
    print("self destructing")
