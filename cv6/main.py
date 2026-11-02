def linear():
    x = int(input("Zadejte cisla: "))
    lst = []
    for _ in range(x):

        i = int(input("Zadejte cislo: "))
        lst.append(i)
    p = int(input("Zadej cislo ktere hledas"))
    for num in lst:
        if num == p:
            print("Cislo se nachazi v seznamu")
            return
        print("Cislo se v seznamu nenachazi")

def binarysearch():
    search = 6
    lst = [6,1,2,30,4,5,7]
    lst.sort()
    print(lst)
    left = 0
    right = len(lst) - 1
    middle = (left + right) // 2
    while right - left != 1:
        middle = (left + right) // 2
        if lst[middle] == search:
            print("Prvek nalezen")
            return 1
        if lst[middle] > search:
            right = middle
        if lst[middle] < search:
            left = middle
        print("Nenalezeno")

    if lst[0] == search or lst[-1] == search:
        print("Nalezeno")
        return 1
    print("Nenalezeno")
    

if __name__ == "__main__":
    # linear()
    binarysearch()