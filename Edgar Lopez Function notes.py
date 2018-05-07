# Defining funtions
def hello_world():
    print("Hello World")


hello_world()


def square_it(number):
    return number ** 2


print("The number is %d." % square_it(3))


def tip_calc(subtotal):
    tax_amt = subtotal * 0.18 # tax_amt CANNOT be used outside of the def!
    return tax_amt

def total_bill(bill_amt):
    total = bill_amt + tip_calc(bill_amt)
    print("Your total bill is %d" % total)

total_bill(100)


def distance(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5 # This is a square root
    return answer


print (distance(0, 0, 3, 4))


def pythagrean(a, b):
    inside = a ** 2 + b ** 2
    answer = inside ** 0.5
    return answer

print (pythagrean(5, 12 ))
