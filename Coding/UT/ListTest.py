from Coding.DataStructures.List import SLinkedList


def SListTest():
    print("-------------------Testing Empty List -------------------")
    lst = SLinkedList()
    print(lst.is_empty())

    print("---------------------Testing Insert ------------------\n")
    for i in range(1, 10, 1):
        lst.insert(i)
    arr = lst.get_List()
    for data in arr:
        print(data, " ")
    print("\n")

    print("------------------Testing Remove-------------------- \n")
    for data in arr:
        lst.remove(data)
    arr = lst.get_List()
    if arr == []:
        print("Removed all elements \n")
    else:
        print("List is not empty \n")
        for data in arr:
            print(data, " ")
        print("\n")

    print("---------------------Testing Append------------------------\n")
    for i in range(1, 10, 1):
        lst.append(i)
    arr = lst.get_List()
    for data in arr:
        print(data, " ")

    print("--------------------Testing remove_first-----------------------\n")
    lst.remove_first()
    for data in arr:
        print(data, " ")
    print("\n")

    print("--------------------Testing remove_last--------------------- \n")
    lst.remove_last()
    for data in arr:
        print(data, " ")
    print("\n")

def main():
    SListTest()

main()

if __name__ == '___main__;':
    print("Running Main")


