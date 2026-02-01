"""
E
D E
C D E
B C D E
A B C D E
"""
def main(n):
    for i in range(n):
        for j in range(n - i):
            print(chr(65 + n - j - 1), end=" ")
        print()
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)