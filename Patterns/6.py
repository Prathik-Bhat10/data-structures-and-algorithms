"""
12345
1234
123
12
1

"""

def main(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(j+1,end="")
        print() 






if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)