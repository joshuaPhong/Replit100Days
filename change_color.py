def change_color(color):
    if color == "yellow":
        return "\033[1;33m"
    elif color == "red":
        return "\033[0;31m"
    elif color == "green":
        return "\033[0;32m"
    elif color == "brown":
        return "\033[0;33m"
    elif color == "blue":
        return "\033[0;34m"
    elif color == "purple":
        return "\033[0;35m"
    elif color == "cyan":
        return "\033[0;36m"
    elif color == "black":
        return "\033[0;30m"
    elif color == "bold":
        return "\033[1m"
    else:
        return "\033[0m"