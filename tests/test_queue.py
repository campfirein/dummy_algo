import unittest
from data_structures.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        """Set up a new queue before each test."""
        self.queue = Queue()

    def test_queue_empty_on_creation(self):
        """Test that a new queue is empty."""
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

    def test_enqueue(self):
        """Test enqueueing items to the queue."""
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)
        
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)

    def test_dequeue(self):
        """Test dequeuing items from the queue."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        
        # Test FIFO behavior
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertTrue(self.queue.is_empty())

    def test_peek(self):
        """Test peeking at the first item."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        
        # Peek should return first item without removing it
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.size(), 2)

    def test_dequeue_empty(self):
        """Test dequeuing from an empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek_empty(self):
        """Test peeking at an empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_size(self):
        """Test size method."""
        sizes = [0, 1, 2, 3]
        for expected_size in sizes:
            self.assertEqual(self.queue.size(), expected_size)
            self.queue.enqueue(expected_size)

    def test_clear(self):
        """Test clearing the queue."""
        # Add some items
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        
        # Clear the queue
        self.queue.clear()
        
        # Verify queue is empty
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

if __name__ == '__main__':
    unittest.main() 