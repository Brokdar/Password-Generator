import argparse
import string
from random import SystemRandom

def generate_password(alphabet, length):
    return ''.join(SystemRandom().choice(alphabet) for _ in range(length))


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", type=int, help = "Length of the password", default = 15)
parser.add_argument("-a", "--alphabet", help = "The alphabet of the valid characters", default = string.ascii_letters + string.digits + string.punctuation)
requirements = parser.add_argument_group("Requirements")
requirements.add_argument("--upper", type=int, help = "Number of minimum uppercases", default = 0)
requirements.add_argument("--lower", type=int, help = "Number of minimum lowercases", default = 0)
requirements.add_argument("--digits", type=int, help = "Number of minimum digits", default = 0)
requirements.add_argument("--symbols", type=int, help = "Number of minimum symbols", default = 0)


args = parser.parse_args()

allowed_uppercases = ''.join(c for c in args.alphabet if c in string.ascii_lowercase)
allowed_lowercases = ''.join(c for c in args.alphabet if c in string.ascii_uppercase)
allowed_digits = ''.join(c for c in args.alphabet if c in string.digits)
allowed_symbols = ''.join(c for c in args.alphabet if c in string.punctuation)


requiredLength = args.lower + args.upper + args.digits + args.symbols
if args.length < requiredLength:
    args.length = requiredLength

password = generate_password(allowed_uppercases, args.upper)
password += generate_password(allowed_lowercases, args.lower)
password += generate_password(allowed_digits, args.digits)
password += generate_password(allowed_symbols, args.symbols)
password += generate_password(args.alphabet, args.length - requiredLength)

print(''.join(SystemRandom().sample(password, len(password))))