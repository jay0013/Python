print("""1. Append an element at the end of the list
2. Count the occurance of the element in the list
3. Insert an element at an index in the list
4. Extend the list with another list
5. Removes an element from the list
6. Search an element in the list
7. Remove and return an element from thelist
8. Arrange the elements in the list in ascending order
9. Print the lements in the list in reverse order
0. EXIT
""")

l = ['a','b','c','d','e','f','g']

while(True):
    ch = int(input("Enter your choice"))
    if(ch == 1):
        e = input("Enter an element to append")
        l.append(e)
        print(l)
    if(ch == 2):
        e = input("Enter an element to count")
        c = l.count(e)
        print("No of 'd' are ", c)
    if(ch == 3):
        e = input("Enter an element to insert")
        p = int(input("Enter a position to insert"))
        l.insert(p,e)
        print(l)
    if(ch == 4):
        l1 = [x for x in input("Enter an element")]
        print(l1)
        l.extend(l1)
        print(l)
    if(ch == 5):
        e = input("Enter an element to remove")
        l.remove(e)
    if(ch==0):
        break
