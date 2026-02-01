"""
ABCDE
ABCD
ABC
AB
A
"""


def main(n):
    for i in range(1, n+1):
        for j in range(n - i + 1):
            print(chr(65 + j), end="")
        print()
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)