def say_hi_to(first, last="", shout=False):
    text = "Hi" + " " + first + " " + last + "!"
    if shout:
        return text.upper()
    else:
        return text