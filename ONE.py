##Pyton Coding questions
##Question 1
##Write function to print "hello_username!" with USERNAME as input of the function.  


def hello_name(user_name):
    print("Hello_" + user_name)
hello_name(str(input("WHAT IS YOUR USER NAME?")))


## Question 2
##Write function first_odds() that prints the odd numbers from 1-100 and returns nothing 

def first_odds(start, stop):
    for num in range(1, 100 + 1):
        if num % 2 != 0:
            print(num)
first_odds(1, 100)

##Question 3
## Write function max_num_in_list to return the max 
##number of a given list.  

## a_list = [ 3, 12, -1, 25]

def max_num_in_list(a_list):
    int(a_list)
print(max(a_list))
    


##Question 4
## Write function to return if the given year is
##a leap year.  
##a leap year divisible by 4, but not by 100, unless 
## also divisible by 400
##return should be boolean

##  % 4 == 0, % 400 == 0, % 100 !=0  

a_year = 2021

def is_leap_year(a_year):
    int(a_year)
    if ((a_year % 4 == 0) or (a_year % 100 != 0) and (a_year % 400 == 0)):

        print(a_year, " is a leap year")
    else:
        print(a_year, " is NOT a leap year")
print(is_leap_year(a_year))




##Question 5
##Write a function to check to see if all numbers
##in the list are consecutive numbers
##ex: [2,3,4,5,6,7] are consecutive, but [1,3,5]
##are not.  RETURN BOOLEAN

##a_list = [1,2,3,4,5]
##a_list = [1,2,5,3,7,6]

def is_consecutive(a_list):
    sort_list = sorted(a_list)
    if sort_list == a_list:
        return True
    else:
        return False
print(is_consecutive(a_list))

