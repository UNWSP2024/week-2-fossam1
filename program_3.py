# Samuel Foss
# Program 3 Total Purchases
# 9/9/2024

def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    # then displays the subtotal of the sale,
    # the amount of sales tax, and the total.
    # Assume the sales tax is 7 percent.

    item1name = input("Name of item 1: ")
    item1cost = float(input("Cost of item 1: "))
    item2name = input("Name of item 2: ")
    item2cost = float(input("Cost of item 2: "))
    item3name = input("Name of item 3: ")
    item3cost = float(input("Cost of item 3: "))
    item4name = input("Name of item 4: ")
    item4cost = float(input("Cost of item 4: "))
    item5name = input("Name of item 5: ")
    item5cost = float(input("Cost of item 5: "))

    print(f"{item1name} Cost: ${item1cost}")
    print(f"{item2name} Cost: ${item2cost}")
    print(f"{item3name} Cost: ${item3cost}")
    print(f"{item4name} Cost: ${item4cost}")
    print(f"{item5name} Cost: ${item5cost}")

    subtotal=item1cost+item2cost+item3cost+item4cost+item5cost

    tax=subtotal*0.07
    total=subtotal+tax

    print(f"subtotal: ${subtotal:.2f}")
    print(f"tax: ${tax:.2f}")
    print(f"total: ${total:.2f}")

calculate_total_purchase()



#Output
#Name of item 1: milk
#Cost of item 1: 2.00
#Name of item 2: eggs
#Cost of item 2: 3.00
#Name of item 3: eggs
#Cost of item 3: 4.11
#Name of item 4: banana
#Cost of item 4: 6.77
#Name of item 5: ice
#Cost of item 5: 9.65
#milk Cost: $2.0
#eggs Cost: $3.0
#eggs Cost: $4.11
#banana Cost: $6.77
#ice Cost: $9.65
#subtotal: $25.53
#tax: $1.79
#total: $27.32
