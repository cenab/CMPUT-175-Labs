from d_linked_node import d_linked_node

class d_linked_list:
    
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0


    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index

    def add(self, item):
        # adds an item to list at the beginning
        temp = d_linked_node(item, self.__head, None)
        if self.__head != None:
            self.__head.setPrevious(temp)
        else:
            self.__tail=temp
        self.__head = temp
        self.__size += 1
        # TODO:

    def remove(self, item):
        # search for the item and remove it
        # the method assumes the item exists
        current = self.__head
        previous=None
        found = False
        while not found:
            if current.getData() == item:
                found = True
                break
            else:
                previous = current
                current = current.getNext()
        if not found:
            return
        if self.get_size() == 1:
            self.__size -= 1
            self.__head = None
            self.__tail = None
            return
        if previous == None:
            self.__head = current.getNext()
            current.getNext().setPrevious(None)
        else:
            if (current.getNext() == None):
                self.__tail = previous
                previous.setNext(None)
            else:
                previous.setNext(current.getNext())
                current.getNext().setPrevious(previous)
        self.__size -= 1
    def append(self, item):
        # adds the item to the end of the list
        # must traverse the list to the end and add item
        temp = d_linked_node(item, None, None)
        if (self.__head == None):
            self.__head=temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail=temp
        self.__size +=1
        return

    def insert(self, pos, item):
        if pos == 0 or self.__size == 0:
            self.add(item)
            return
        if pos == self.__size:
            self.append(item)
            return
        current = self.__head
        while pos != 0:
            current = current.getNext()
            pos -= 1
        before = current.getPrevious()
        temp = d_linked_node(item, current, before)
        current.setPrevious(temp)
        before.setNext(temp)
        temp.setPrevious(before)
        temp.setNext(current)
        self.__size += 1


    def pop(self, pos=None):
        current = self.__head
        previous = None
        if self.get_size() == 1:
            returningValue = current.getData()
            self.remove(returningValue)
            return returningValue
        elif pos != None:
            while pos != 0:
                current = current.getNext()
                pos -= 1
            returningValue2 = current.getData()
            self.remove(returningValue2)
            return returningValue2
        elif pos == None:
            while (current.getNext() != None):
                current = current.getNext()
            returningValue3 = current.getData()
            self.remove(returningValue3)
            return returningValue3

    def search_larger(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() > item:
                found= True
                break
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index

    def get_size(self):
        return self.__size

    def get_item(self, pos):
        current = self.__head
        previous = None
        found = False
        index = 0
        if not (0 <= abs(pos) < self.get_size()):
            raise Exception("There is no item in that position")
            return
        if pos < 0:
            pos = pos + self.get_size()
        while index < pos:
            current = current.getNext()
            index = index + 1
        return current.getData()

    def __str__(self):
        size = self.get_size()
        i = 0
        current = self.__head
        printed = ""
        while i < size:
            printed += str(current.getData())
            if current.getNext() is not None:
                printed += " "
            current = current.getNext()
            i += 1
        return printed


def test():
    linked_list = d_linked_list()

    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add("World")
    linked_list.add("Hello")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"


    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = d_linked_list()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"

    int_list = d_linked_list()

    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"



    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"


    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test"
    int_list.insert(7,801)
    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"
#    print("passed until here")
#    print(int_list)
    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"
#    print("passed until here123")
    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 1! ============")

if __name__ == '__main__':
    test()
