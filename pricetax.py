import sys

# Check correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python pricetax.py <price_of_product> <tax_percentage>")
    sys.exit()

# Read values from command line
productprice = float(sys.argv[1])
producttax = float(sys.argv[2])

# Validate product price
if productprice <= 0:
    print("Enter valid product price")
    sys.exit()

# Calculate tax and total amount
taxamount = (productprice * producttax) / 100
totalamount = productprice + taxamount

# Print results
print("Product Price =", productprice)
print("Product Tax % =", producttax)
print("Tax Amount =", taxamount)
print("Total Product Price =", totalamount)
