class PeekingIterator:
    def __init__(self, iterator):
        """
        Initializes the object with the given integer iterator.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._next_val = None
        self._has_next = False
        
        # Pre-fetch the first element
        self._advance()

    def _advance(self):
        """Internal helper to move the underlying iterator."""
        if self.iterator.hasNext():
            self._next_val = self.iterator.next()
            self._has_next = True
        else:
            self._next_val = None
            self._has_next = False

    def peek(self):
        """
        Returns the next element in the array without moving the pointer.
        :rtype: int
        """
        return self._next_val

    def next(self):
        """
        Returns the next element and moves the pointer.
        :rtype: int
        """
        res = self._next_val
        self._advance()
        return res

    def hasNext(self):
        """
        Returns true if there are still elements in the array.
        :rtype: bool
        """
        return self._has_next