class Queue:
    """
    A simple implementation of a Queue data structure.
    Queue follows FIFO (First In First Out) principle.
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)
    
    def peek(self):
        """
        Return the first item from the queue without removing it.
        
        Returns:
            The first item from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty queue")
        return self.items[0]
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)
    
    def clear(self):
        """Remove all items from the queue."""
        self.items = []


# Example usage
if __name__ == "__main__":
    # Create a new queue
    queue = Queue()
    
    # Enqueue some items
    print("Enqueuing items: 1, 2, 3, 4")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    
    # Check the size
    print(f"Queue size: {queue.size()}")
    
    # Peek at the first item
    print(f"First item (peek): {queue.peek()}")
    
    # Dequeue some items
    print("\nDequeuing items:")
    print(f"Dequeued: {queue.dequeue()}")  # Should print 1
    print(f"Dequeued: {queue.dequeue()}")  # Should print 2
    
    # Check size after dequeuing
    print(f"Queue size after dequeuing: {queue.size()}")
    
    # Clear the queue
    queue.clear()
    print(f"Queue size after clearing: {queue.size()}")
    
    # Try to dequeue from empty queue
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"\nError: {e}") 