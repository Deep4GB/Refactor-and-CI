import sys
sys.path.append("./refactornci")
from main import Node, DoublyLinkedList

def test_add():
    node = Node(1)
    assert str(node) == "(1, None)"

def test_doubly_linked_list():
    # Test the DoublyLinkedList class
    dll = DoublyLinkedList()

    # Test the size and is_empty methods
    assert dll.size() == 0
    assert dll.is_empty() == True

    # Test adding elements
    node1 = Node(1)
    node2 = Node(2)

    dll.add_first(node1)
    assert dll.size() == 1
    assert dll.is_empty() == False
    assert dll.get_first() == node1
    assert dll.get_last() == node1

    dll.add_last(node2)
    assert dll.size() == 2
    assert dll.get_first() == node1
    assert dll.get_last() == node2

    # Test get_previous and get_next methods
    assert dll.get_previous(node1) == dll._DoublyLinkedList__header  # Should be the header node
    assert dll.get_next(node1) == node2
    assert dll.get_previous(node2) == node1
    assert dll.get_next(node2) == dll._DoublyLinkedList__trailer  # Should be the trailer node

if __name__ == "__main__":
    test_add()
    test_doubly_linked_list()
