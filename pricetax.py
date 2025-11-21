import sys

if len(sys.argv) != 3:
    print("No inputs given, using default values...")
    productprice = 1000
    producttax = 2
else:
    productprice = float(sys.argv[1])
    producttax = float(sys.argv[2])
if productprice<=0:
    print("enter correct input")
elif producttax<=0:
    print("tax must be inculde it madidtory")


else:
    taxamount = (productprice * producttax) / 100
    totalamount = productprice + taxamount
    print("Product Price =", productprice)
    print("Product Tax % =", producttax)
    print("Tax Amount =", taxamount)
    print("Total Product Price =", totalamount)




