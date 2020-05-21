


def sequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    	
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
    return found

testlist = [1,2,3,4,5,6,7,8,9]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))


