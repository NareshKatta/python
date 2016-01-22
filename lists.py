list = [1, 1.2, 1.2, 'true', True, 'True']
print list
list = list*2
print list
print list[1]
print len(list)
print list[1:3]
list.append(5)
print list
list.insert(2, -9999)
print list
lastElement = list.pop()
print lastElement
print list
ithElement = list.pop(0)
print "Oth Element" , ithElement
print list
list.sort()
print 'sorted list', list
list.reverse()
print 'reversed list', list
print 'deleting the element with index 2'
del list[2]
print 'list after deleting the element at index 2'
print list
print 'getting the index of the element true'
print list.index('true');


