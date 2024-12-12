from argparse import ArgumentParser

parser = ArgumentParser(description="Run multiple trials")
parser.add_argument("--n_trials", type=int, help="The number of trials")
args = parser.parse_args()
print(args.n_trials)