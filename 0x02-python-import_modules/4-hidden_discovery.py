#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_dir = dir(hidden_4)
    __ = "__"
    for i in range(len(all_dir)):
        if __ not in all_dir[i]:
            print(all_dir[i])
