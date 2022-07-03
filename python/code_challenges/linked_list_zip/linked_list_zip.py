def zip_lists(a, b):
    current1 = a.head
    current2 = b.head
    temp1 = current1
    temp2 = current2
    while (current1 and current2):
        # 1,3,5,7
        # 2,4,6,8
        current1.next = temp2
        current2.next = temp1.next

    current1 = current1.next
    current2 = current2.next
    return current1
