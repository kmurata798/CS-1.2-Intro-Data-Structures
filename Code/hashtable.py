#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: 
        Average case --> O(l*b)==O(n) Every bucket has 1 item == immediately locates data.
        Worst case ----> O(l*b)==O(n) Must loop through each bucket, followed by each item in the bucket"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: 
        Average case --> O(l*b)==O(n) Every bucket has 1 item == immediately locates data.
        Worst case ----> O(l*b)==O(n) Must loop through each bucket, followed by each item in the bucket."""
        # Loop through all buckets
        # Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: 
        Average case --> O(l*b)==O(n) Every bucket has 1 item == immediately locates data.
        Worst case ----> O(l*b)==O(n) When more than one item is hashed into the specified bucket."""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: 
        Average case --> O(l*b)==O(n) Only 1 item in 1 bucket == only need to loop through for loop once to get
                         length.
        Worst case ----> O(l*b)==O(n) When more than one item is hashed into one or more buckets == must loop n
                         times based on how many items exist."""
        # Loop through all buckets
        # Count number of key-value entries in each bucket
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: 
        Average case --> O(1) Every bucket has 1 item == immediately locates data.
        Worst case ----> O(n/b)==O(l) When more than one item is hashed into the specified bucket."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        bucket = self.get_bucket(key)
        for current_key, value in bucket.items():
            if current_key == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: 
        Average case --> O(1) Every bucket has 1 item == immediately locates data.
        Worst case ----> O(n/b)==O(l) When more than one item is hashed into the specified bucket."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, return value associated with given key
        # Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.get_bucket(key)
        for current_key, value in bucket.items():
            if current_key == key:
                return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: 
        Average case --> O(1) Every bucket has 1 item == immediately locates data.
        Worst case ----> O(n/b)==O(l) When more than one item is hashed into the specified bucket."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, update value associated with given key
        # Otherwise, insert given key-value entry into bucket
        bucket = self.get_bucket(key)
        if self.contains(key):
            for current_key, current_value in bucket.items():
                if current_key == key:
                    bucket.delete((current_key, current_value))
                    bucket.append((key, value))
        else:
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: 
        Average case --> O(1) Every bucket has 1 item == immediately locates data.
        Worst case ----> O(n/b)==O(l) When more than one item is hashed into the specified bucket."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, delete entry associated with given key
        # Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.get_bucket(key)
        if self.contains(key):
            for current_key, value in bucket.items():
                if current_key == key:
                    bucket.delete((current_key, value))
        else:
            raise KeyError('Key not found: {}'.format(key))

    def get_bucket(self, key):
        """Uses the hash value of the specific key to return the bucket that corresponds"""
        return self.buckets[self._bucket_index(key)]


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
