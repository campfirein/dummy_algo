class Stack:
    """
    A simple implementation of a Stack data structure.
    Stack follows LIFO (Last In First Out) principle.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        return self.items[-1]
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


# Example usage
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()
    
    # Push some items
    print("Pushing items: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    # Check the size
    print(f"Stack size: {stack.size()}")
    
    # Peek at the top item
    print(f"Top item (peek): {stack.peek()}")
    
    # Pop all items
    print("\nPopping all items:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")
    
    # Try to pop from empty stack
    try:
        stack.pop()
    except IndexError as e:
        print(f"\nError: {e}") 