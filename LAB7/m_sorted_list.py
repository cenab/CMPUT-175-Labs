from d_linked_list import d_linked_list
from d_linked_node import d_linked_node

class m_sorted_list:
    def __init__(self, m_sorted):
        self.m_sorted = m_sorted
        self.b = d_linked_list()
        # TODO:

    def add(self, item):
        if self.m_sorted == True:
            index = self.b.search_larger(item)
            try:
                self.b.insert(index, item)
            except:
                self.b.append(item)
        if self.m_sorted == False:
            self.b.append(item)
        return
        # TODO:

    def pop(self):
        if self.m_sorted == True:
            return self.b.pop()
        elif self.m_sorted == False:
            returningValue4 = self.b.get_item(0)
            self.b.remove(returningValue4)
            return returningValue4
        # TODO:

    def search(self, item):
        # TODO:
        if self.b.search(item) == True:
            tuple1 = (self.b.search(item), self.b.index(item))
            return tuple1
        elif self.m_sorted == True and self.b.search(item) == False:
            tuple2 = (self.b.search(item), self.b.search_larger(item))
            return tuple2
        elif self.m_sorted == False and self.b.search(item) == False:
            tuple3 = (self.b.search(item), -1)
            return tuple3

    def change_sorted(self):
        if self.m_sorted == True:
            self.m_sorted = False
        elif self.m_sorted == False:
            raise Exception("“I don’t know how to sort a doubly linked list yet”")
        return self.m_sorted

    def get_size(self):
        # TODO:
        return self.b.get_size()

    def get_item(self, pos):

        # TODO:
        return self.b.get_item(pos)
    def __str__(self):
        # TODO:
        return self.b.__str__()
def test():

    sor_list = m_sorted_list(True)

    is_pass = (sor_list.get_size() == 0)
    assert is_pass == True, "fail the test"

    sor_list.add(4)
    sor_list.add(3)
    sor_list.add(8)
    sor_list.add(7)
    sor_list.add(1)

    is_pass = (str(sor_list) == "1 3 4 7 8")
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_size() == 5)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.pop() == 8)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.pop() == 7)
    assert is_pass == True, "fail the test"

    is_pass = (str(sor_list) == "1 3 4")
    assert is_pass == True, "fail the test"

    a = sor_list.search(2)
    is_pass = (a[0] == False and a[1] == 1)
    assert is_pass == True, "fail the test"

    a = sor_list.search(3)
    is_pass = (a[0] == True and a[1] == 1)
    assert is_pass == True, "fail the test"

    a = sor_list.search(7)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_size() == 3)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_item(2) == 4)
    assert is_pass == True, "fail the test"

    sor_list.change_sorted()
    sor_list.add(1)

    is_pass = (str(sor_list) == "1 3 4 1")
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_size() == 4)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.pop() == 1)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.pop() == 3)
    assert is_pass == True, "fail the test"

    sor_list.add(7)
    sor_list.add(6)

    is_pass = (str(sor_list) == "4 1 7 6")
    assert is_pass == True, "fail the test"

    a = sor_list.search(2)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"

    a = sor_list.search(7)
    is_pass = (a[0] == True and a[1] == 2)
    assert is_pass == True, "fail the test"

    a = sor_list.search(8)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_size() == 4)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_item(2) == 7)
    assert is_pass == True, "fail the test"


    sor_list2 = m_sorted_list(False)

    is_pass = (sor_list2.get_size() == 0)
    assert is_pass == True, "fail the test"

    sor_list2.add(4)
    sor_list2.add(3)
    sor_list2.add(8)
    sor_list2.add(7)
    sor_list2.add(1)

    is_pass = (str(sor_list2) == "4 3 8 7 1")
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.get_size() == 5)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.pop() == 4)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.pop() == 3)
    assert is_pass == True, "fail the test"

    is_pass = (str(sor_list2) == "8 7 1")
    assert is_pass == True, "fail the test"

    a = sor_list2.search(2)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"

    a = sor_list2.search(7)
    is_pass = (a[0] == True and a[1] == 1)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.get_size() == 3)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.get_item(2) == 1)
    assert is_pass == True, "fail the test"

    try:
        sor_list2.change_sorted()
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"


    sor_list2.add(3)
    sor_list2.add(2)

    is_pass = (str(sor_list2) == "8 7 1 3 2")
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.get_size() == 5)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.pop() == 8)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.pop() == 7)
    assert is_pass == True, "fail the test"


    is_pass = (str(sor_list2) == "1 3 2")
    assert is_pass == True, "fail the test"


    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

if __name__ == '__main__':
    test()
