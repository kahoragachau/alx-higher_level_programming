#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_len = len(sys.argv)
    if num_len == 1:
        print(f'{num_len - 1} arguments.')
    elif num_len == 2:
        print(f'{num_len - 1} argument:')
    else:
        print(f"{num_len - 1} arguments:")
    for i in range(1, num_len):
        print(f"{i}: {sys.argv[i]}")
