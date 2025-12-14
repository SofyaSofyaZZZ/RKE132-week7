def get_greeting(hour: int) -> str:
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def say_hello(name: str, hour: int) -> None:
    greeting = get_greeting(hour)
    print(f"{greeting}, {name}!")
