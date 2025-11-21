import sys


if len(sys.argv) != 3:
    print("Usage: python pricetax.py <product_price> <tax_percentage>")
    sys.exit(1)


productprice = float(sys.argv[1])
producttax = float(sys.argv[2])


else:
    productprice = 1000
    producttax = 2




taxamount = (productprice * producttax) / 100
totalamount = productprice + taxamount

if productprice <= 0:
    print("Product price must be greater than 0")
    sys.exit(1)
elif producttax < 0:
    print("Tax percentage must be greater than or equal to 0")
    sys.exit(1)
    print("Product Price =", productprice)
    print("Product Tax % =", producttax)
    print("Tax Amount =", taxamount)
    print("Total Product Price =", totalamount)
