"""  
A
AB       Asciii value of Capital Letters starts from 65 and ends at 90
ABC
ABCD
ABCDE
"""
def main(n):
    for i in range(1, n+1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)