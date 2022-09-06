import argparse

def greet_user(user):
    """greet function"""
    print(f"hello {user}!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user", help="name of user")

    args = parser.parse_args()

    greet_user(args.user)
    

if __name__ == '__main__':
    main()

