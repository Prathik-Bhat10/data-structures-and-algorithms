"""
1
12
123
1234
12345
"""

def main(n):
    for i in range(1, n+1):
        for j in range(i):
            print(f"{j+1}", end="")
        print()
    
    
    
    
    
    
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)