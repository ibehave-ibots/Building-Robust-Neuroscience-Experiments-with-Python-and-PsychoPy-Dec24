import argparse

# parse command line arguments
parser = argparse.ArgumentParser(description="A script that says hi to someone")
parser.add_argument("--first", type=str, default="", help="First name of the person you want to say hi to")
parser.add_argument("--last", type=str, default="", help="Last name of the person you want to say hi to")
parser.add_argument(
    "--shout", default=False, action="store_true", help="Use this flag to shout"
)
args = parser.parse_args()

# print message
text = "Hi " + args.first + " " + args.last + "!"
if args.shout:
    text = text.upper()
print(text)
