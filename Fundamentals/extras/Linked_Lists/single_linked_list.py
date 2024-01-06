class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        new_node = SNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        runner = self.head
        self.head = runner.next
        return self

    def remove_from_back(self):
        runner = self.head
        previous = None
        while (runner.next != None):
            previous = runner
            runner = runner.next
        previous.next = None
        return self



class SNode:
    def __init__(self, val):
        self.value = val
        self.next = None



my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()     # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!
my_list.remove_from_front().print_values()
my_list.remove_from_back().print_values()
