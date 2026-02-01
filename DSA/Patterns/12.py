"""
1      1
12    21
123  321
12344321
"""
def main(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        for k in range(2*(n-i-1)):
            print(" ", end="")
        for l in range(i, -1, -1):
            print(l+1, end="")
        print()
    
    
    
    
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)