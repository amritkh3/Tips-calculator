"""2.Write a Tipper program where the user enters a restaurantbill total. The program should then display two amounts: a
15 percent tip and a 20 percent tip.
1.ask user for total amount of bill and assign it to the variable total.
2.declare a variable with name tips15 and assign it with the value 15%of total
3. assign a variable with name tips20 and assign it with the value 20%of total.
print tips15 and tips20.

"""
total=input("whats you total bill")
total=int(total)
tips15= 15/100*total
tips20=20/100*total
print("if you tip 15 percent tipwill be",tips15)
print("if you tip 20 percnet tip will be ",tips20)
