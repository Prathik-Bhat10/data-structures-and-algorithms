"""
*****
*****
*****
*****
*****

"""

def main(n):
    # for i in range(n):
    #     print("*"*n)
        
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
    
    
    
    
    
    
if __name__ == "__main__":
    n=int(input("Enter the size of the pattern: "))
    main(n)