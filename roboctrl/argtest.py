import argparse


parser = argparse.ArgumentParser(description="My Cool Application")

# eg:
# argtest.py -s 40
parser.add_argument("-s", "--speed", dest="speed", action="store", type=int, default=100)

# eg:
# argtest.py -o
parser.add_argument("-o", "--optional", dest="optional", action="store_true")

# zero or more optional values
# eg:
# argtest.py 1 2 3 4 
parser.add_argument("values", metavar="VALS", type=float, nargs="*", help="some values")

args = parser.parse_args()

print("Speed: %d" % (args.speed))
print("Optional: ", args.optional)
print("Values: ", args.values)
