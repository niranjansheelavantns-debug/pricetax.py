import sys
if len(sys.argv)!=3:
    print("usage:python pricetax.py <priceofproduct><taxofproduct>")
    sys.exit()
    priceofproduct=float(sys.argv[1])
    taxofproduct=float(sys.argv[2])

if priceofproduct<=0:
    print("enter orignal price of product")

else:
    totalamount=100*taxofproduct+priceofproduct

print("Product Price=",priceofproduct)
print("Product Tax %=",taxofproduct)
print("Total Product Price=",totalamount)
