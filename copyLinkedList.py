# Copy LinkedList to new address

def deepCopy(head):
    
    if(head is None):
        return None
    hashMap = {}
    copiedList = None
    secondNode = None
    firstNode = head

    while (firstNode != None):
       newNode = create_Node(firstNode.value)
       if (copiedList == None):
        copiedList = newNode
        secondNode = copiedList
       else:
        secondNode.next = newNode
        secondNode = newNode

       hashMap.update({firstNode:secondNode})
       firstNode = firstNode.next

    firstNode = head
    secondNode = copiedList

    while (firstNode != None):
      if (firstNode.arbitrary != None):
        secondNode.arbitrary = hashMap.get(firstNode.arbitrary)

      firstNode = firstNode.next
      secondNode = secondNode.next

    return copiedList

def create_Node(value):
    newAlNode = ALNode(value)
    newAlNode.next = None
    newAlNode.arbitrary = None
    return newAlNode
