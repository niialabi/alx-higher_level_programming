#!usr/bin/python3
if __name__ == "__main__":
    import hidden_4
# if __name__ == "__main__":
    hidden_list = dir(hidden_4)
    for hidden in hidden_list:
        if hidden[:2] != "--":
            print(hidden)
