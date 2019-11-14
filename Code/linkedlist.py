#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because we're checking each node 
        n number of times, checking if the nodes contain a next node"""
        count = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            count += 1
        return count
        # Loop through all nodes and count one for each

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because we can instantly access the tail."""
        # if (head == None):
        #     head = Node(data)
        # else:
        #     current = head
        #     while (current.next != None):
        #         current = current.next
        #     current.next = Node(data)
        # return head

        node = Node(item)
        if self.tail is not None:
            self.tail.next = node
        # Append node after tail, if it exists
        else:
            self.head = node
        self.tail = node
        # Create new node to hold given item

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) because we have instant access to the Head."""
        node = Node(item)
        # Create new node to hold given item
        if self.head is not None:
            node.next = self.head
        else:
            self.tail = node
        self.head = node
        # Prepend node before head, if it exists

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) because if the first search, head, 
        matches the given quality, we can end the searching?
        Worst case running time: O(n) because we have to go through all n number of nodes which takes more time"""
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                if quality(current_node.data) is True:
                    return current_node.data
                else:
                    current_node = current_node.next
        else:
            return None
        # Loop through all nodes to find item where quality(item) is True
        # Check if node's data satisfies given quality function

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) because if the first search, head, 
        matches the given quality, we can end the searching?
        TODO: Worst case running time: O(n) """
        temp = self.head 
  
        # If head node itself holds the key to be deleted
        if (temp is not None): 
            if (temp.data == item): 
                self.head = temp.next
                temp = None
                return

            # Search for the key to be deleted, keep track of the 
            # previous node as we need to change 'prev.next' 
            while(temp is not None): 
                if temp.data == item: 
                    break 
                prev = temp 
                temp = temp.next 
    
            # if key was not present in linked list 
            if(temp == None): 
                return 
    
            # Unlink the node from linked list 
            prev.next = temp.next 
    
            temp = None 
        
        else:
            raise ValueError('Item not found: {}'.format(item))
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
