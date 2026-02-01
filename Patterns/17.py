"""
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA  
"""
def main(n):
    for i in range(1, n+1):
        # printing spaces
        for j in range(n-i):
            print(" ", end="")
        # printing increasing part
        for j in range(1, i+1):
            print(chr(64 + j), end="")
        # printing decreasing part
        for j in range(i-1, 0, -1):
            print(chr(64 + j), end="")
        print()
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)