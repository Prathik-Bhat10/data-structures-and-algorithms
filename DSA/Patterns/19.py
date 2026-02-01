"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********  
"""

def main(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j <= n - i+1:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range(1, n+1):
            if j < i:
                print(" ", end="")
            else:
                print("*", end="")
        print()
    for i in range(n, 0, -1):
        for j in range(1, n+1):
            if j <= n - i + 1:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range(1, n+1):
            if j < i:
                print(" ", end="")
            else:
                print("*", end="")
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)