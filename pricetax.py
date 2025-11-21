import sys
if len(sys.argv)!=3:
    print("usage:python pricetax.py <priceofproduct><taxofproduct>")
    sys.exit()
    productprice=float(sys.argv[1])
    producttax=float(sys.argv[2])

if productprice<=0:
    print("enter orignal price of product")

else:
    totalamount=100*producttax+productprice

print("Product Price=",productprice)
print("Product Tax %=",producttax)
print("Total Product Price=",totalamount)
