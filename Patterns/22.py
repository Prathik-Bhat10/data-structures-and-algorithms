"""
4444444
4333334
4322234
4321234
4322234
4333334
4444444  
"""


def main(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top = i
            left = j
            bottom = (2 * n - 2) - i
            right = (2 * n - 2) - j
            minDist = min(top, bottom, left, right)
            print(n - minDist, end=" ")
        print()


if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)
