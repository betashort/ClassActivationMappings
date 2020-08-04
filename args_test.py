import argparse

def display_args(args):
    print(args)
    print(f'arg1 : {args.arg1}')
    print(f'arg2 : {args.arg2}')
    
    return 0


parser = argparse.ArgumentParser()
parser.add_argument(#"-短縮ver", 
                    "--arg1", 
                    help="arg1_description", 
                    #type=bool, 
                    default=False)

parser.add_argument(#"-短縮ver", 
                    "--arg2", 
                    help="arg2_description", 
                    #type=bool, 
                    default=False)

args = parser.parse_args()

print(args.arg1)

print(args.arg2)

print(args)

print("==== Function ====")

display_args(args)

