

def mergeTwoLists(list1, list2):
    """
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
        Return the head of the merged linked list.
    """
    result = []
    while len(list1) + len(list2) != 0:
        if len(list1) == 0:
            for x in list2:
                x = list2.pop(0)
                result.append(x)
            continue
        if len(list2) == 0:
            result += list1
            for x in list1:
                x = list1.pop(0)
                result.append(x)
            continue
        x = list1[0]
        y = list2[0]
        if x < y:
            x = list1.pop(0)
            result.append(x)
        else:
            y = list2.pop(0)
            result.append(y)
    return result

xs = [2,5,6]
ys = [5,7,9]
zs = mergeTwoLists(xs,ys)
print(zs)