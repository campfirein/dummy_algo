import unittest
from data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        """Set up a new stack before each test."""
        self.stack = Stack()

    def test_stack_empty_on_creation(self):
        """Test that a new stack is empty."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_push(self):
        """Test pushing items to the stack."""
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)
        
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

    def test_pop(self):
        """Test popping items from the stack."""
        self.stack.push(1)
        self.stack.push(2)
        
        # Test LIFO behavior
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        """Test peeking at the top item."""
        self.stack.push(1)
        self.stack.push(2)
        
        # Peek should return top item without removing it
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.size(), 2)

    def test_pop_empty(self):
        """Test popping from an empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        """Test peeking at an empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_size(self):
        """Test size method."""
        sizes = [0, 1, 2, 3]
        for expected_size in sizes:
            self.assertEqual(self.stack.size(), expected_size)
            self.stack.push(expected_size)

if __name__ == '__main__':
    unittest.main() 