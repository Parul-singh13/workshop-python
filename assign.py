x=int(input("enter item1 cost in $"))
y=int(input("enter item2 cost in $"))
z=x+y
member=str(input("the customer is member(yes/no)")).lower()
if z>=100 and member =="yes":
    discount=0.1*z
    totalcost=z-discount
    print("the total cost is",totalcost.2f)
else:
    totalcost=z
     
   

