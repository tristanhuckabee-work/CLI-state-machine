import argparse

def setup_command(args):
  print("Running setup...")

def main():
  print("Running Python version of State Machine...")

  parser = argparse.ArgumentParser(prog="statmach-py")
  subparsers = parser.add_subparsers(dest="command")

  # Setup
  setup_parser = subparsers.add_parser("setup", help="Setup Environment")
  setup_parser.set_defaults(func=setup_command)


  args = parser.parse_args()
  if hasattr(args, "func"):
    args.func(args)
  else:
    parser.print_help()