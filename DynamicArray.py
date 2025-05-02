import ctypes

class DynamicArray:
    """A dynamic array class similar to Java's ArrayList."""

    def __init__(self, capacity=10):
        """Initialize the dynamic array."""
        self._size = 0  # Number of elements currently stored
        self._capacity = max(capacity, 1) # Actual array capacity
        self._array = self._make_array(self._capacity) # Internal array

    def __len__(self):
        """Return the number of elements stored in the array."""
        return self._size

    def __getitem__(self, index):
        """Return element at index."""
        if not 0 <= index < self._size:
            raise IndexError('invalid index')
        return self._array[index] # Retrieve item

    def is_empty(self):
        """Return True if the array is empty."""
        return self._size == 0

    def append(self, obj):
        """Add object to the end of the array."""
        if self._size == self._capacity: # Check if capacity is full
            self._resize(2 * self._capacity) # Double the capacity
        self._array[self._size] = obj
        self._size += 1

    def insert(self, index, obj):
        """Insert object at index, shifting subsequent elements right."""
        if not 0 <= index <= self._size: # Allow insertion at index size
             raise IndexError('invalid index for insertion')
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        # Shift elements to the right
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = obj
        self._size += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        for i in range(self._size):
            if self._array[i] == value:
                # Shift elements to the left
                for j in range(i, self._size - 1):
                    self._array[j] = self._array[j + 1]
                self._array[self._size - 1] = None # Help garbage collection
                self._size -= 1
                # Shrink if necessary (e.g., if size is 1/4 of capacity)
                if self._size <= self._capacity // 4 and self._capacity > 1:
                     self._resize(self._capacity // 2)
                return # Exit after removing the first occurrence
        raise ValueError("value not found")

    def search(self, value):
        """Return the index of the first occurrence of value, or -1 if not found."""
        for i in range(self._size):
            if self._array[i] == value:
                return i
        return -1

    def _resize(self, new_capacity):
        """Resize internal array to new capacity."""
        print(f"Resizing from {self._capacity} to {new_capacity}") # Optional: print resize info
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def _make_array(self, capacity):
        """Return a new array with the given capacity."""
        # Uses ctypes to create a low-level array (similar to Java's Object[])
        # You could also use a list of Nones: [None] * capacity
        return (capacity * ctypes.py_object)()

    def __str__(self):
        """Return string representation of the array."""
        if self._size == 0:
            return "[]"
        # Only show elements up to _size
        elements = [str(self._array[i]) for i in range(self._size)]
        return "[" + ", ".join(elements) + "]"

    def get_capacity(self):
        """Return the current capacity of the array."""
        return self._capacity

# --- Example Usage ---
if __name__ == "__main__":
    dynamic_array = DynamicArray(5)
    print(f"Initial Array: {dynamic_array}, Size: {len(dynamic_array)}, Capacity: {dynamic_array.get_capacity()}")

    dynamic_array.append("A")
    dynamic_array.append("B")
    dynamic_array.append("C")
    dynamic_array.append("D")
    print(f"After adding A, B, C, D: {dynamic_array}, Size: {len(dynamic_array)}, Capacity: {dynamic_array.get_capacity()}")

    # Trigger grow
    dynamic_array.append("E")
    dynamic_array.append("F")
    print(f"After adding E, F (triggered grow): {dynamic_array}, Size: {len(dynamic_array)}, Capacity: {dynamic_array.get_capacity()}")

    # Insert
    dynamic_array.insert(1, "X")
    print(f"After inserting X at index 1: {dynamic_array}, Size: {len(dynamic_array)}, Capacity: {dynamic_array.get_capacity()}")

    # Remove
    dynamic_array.remove("A")
    dynamic_array.remove("B")
    dynamic_array.remove("C")
    dynamic_array.remove("D")
    dynamic_array.remove("E")
    print(f"After removing A, B, C, D, E (triggered shrink): {dynamic_array}, Size: {len(dynamic_array)}, Capacity: {dynamic_array.get_capacity()}")

    # Search
    print(f"Index of 'F': {dynamic_array.search('F')}")
    print(f"Index of 'Z': {dynamic_array.search('Z')}")

    # Get item
    print(f"Element at index 0: {dynamic_array[0]}")

    # Check if empty
    print(f"Is empty? {dynamic_array.is_empty()}")









