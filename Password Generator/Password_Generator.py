import argparse
import string
import random

def generate_password(alphabet, length):
    return ''.join(random.choice(alphabet) for _ in range(length))


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", dest = "length", help = "The number of characters for the password")
parser.add_argument("-a", "--alphabet", dest = "alphabet", help = "The alphabet of the valid characters of the password")

args = parser.parse_args()

if(args.alphabet):
    alphabet = args.alphabet
else:
    alphabet = string.ascii_letters + string.digits + string.punctuation

if(args.length):
    length = int(args.length)
else:
    length = 15

print(generate_password(alphabet, length))