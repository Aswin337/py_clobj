try:
    a=int(input("Enter Number A:"))
    b=int(input("Enter Number B:"))
    c=a/b
    print(c)
except Exception:
    print("Any Number divided by zero is not possible")
finally:
    print("important module")
print("Next Module")


try:
    print("Welcome to Maaran Parotta Kadai :")
    no_of_items=int(input("Enter number of items you want :"))
    total_price=200*no_of_items
    average_price=total_price/no_of_items
    print("Average price :",average_price)
except Exception:
    print("Zero division error.")
