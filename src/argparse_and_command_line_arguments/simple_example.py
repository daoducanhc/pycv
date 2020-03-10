import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="name of the user")
args = vars(ap.parse_args())

print(args)
print("Hi {}, glhf".format(args["name"]))

# python src\argparse_and_command_line_arguments\simple_example.py --name alooooo
