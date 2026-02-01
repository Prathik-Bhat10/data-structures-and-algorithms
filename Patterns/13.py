"""
1
23
456
78910
1112131415
"""
def main(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern: "))
    main(n)