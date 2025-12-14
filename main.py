from datetime import datetime
from greeting import say_hello


def main():
    name = input("Enter your name: ")
    current_hour = datetime.now().hour
    say_hello(name, current_hour)


if __name__ == "__main__":
    main()
