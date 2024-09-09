# Samuel Foss
# Program 2 average age
# 9/9/2024


def average_age():
    # Get User Input
    age1 = float(input("First age: "))
    age2 = float(input("Second age: "))
    age3 = float(input("Third age: "))
    age4 = float(input("Fourth age: "))
    age5 = float(input("Fifth age: "))

    # Sum ages
    sum=age1+age2+age3+age4+age5


    # Average the ages
    average=sum/5


    # Print the results
    print(average)


# Line which calls the above function.
average_age()


#output code
#First age: 1
#Second age: 5
#Third age: 62
#Fourth age: 24
#Fifth age: 21
#22.6
