"""
1
22
333
4444
55555
"""

def main(n):
    for i in range(1, n+1):
        for j in range(i):
            print(f"{i}", end="")
        print()
    
    
    
    
    
    
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)