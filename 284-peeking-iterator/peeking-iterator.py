class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        """
        self.iterator = iterator
        # Pre-fetch the first element to cache it
        self.next_val = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self) -> int:
        """
        Returns the next element in the iteration without advancing it.
        """
        return self.next_val

    def next(self) -> int:
        """
        Returns the next element in the iteration and advances the iterator.
        """
        res = self.next_val
        self.next_val = self.iterator.next() if self.iterator.hasNext() else None
        return res

    def hasNext(self) -> bool:
        """
        Returns true if the iteration has more elements.
        """
        return self.next_val is not None