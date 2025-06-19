def greeting(name=None):
    if name is None:
        print("hello, noble stranger.")
    elif isinstance(name, str):
    else:
        print("Error! It was not a name.")
    greetings('Alexandra')
    greetings('wil')
    greetings()
    greetings(42)