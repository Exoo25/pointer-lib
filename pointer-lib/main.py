pointer_table = {}

def store(obj):
    """
    Stores a Python object in the pointer table and returns a short hex ID.

    This function simulates a pointer system in Python by using the object's `id()`.
    Only the lower 20 bits of the id are used, so collisions are possible for many objects.

    Args:
        obj: Any Python object to store.

    Returns:
        str: A hexadecimal string representing the object's short ID, e.g., "0xABCDE".
    """
    obj_id = id(obj) & 0xFFFFF  # short 20-bit ID
    pointer_table[obj_id] = obj
    return f"0x{obj_id:05X}"

def retrieve(obj_id_hex):
    """
    Retrieves a Python object from the pointer table using its hex ID.

    Args:
        obj_id_hex (str): The hex string returned by `store()`, e.g., "0xABCDE".

    Returns:
        object: The Python object stored under that ID.

    Raises:
        KeyError: If no object is found for the given ID.
    """
    obj_id = int(obj_id_hex, 16)  # convert hex string back to int
    return pointer_table[obj_id]

# Example usage
# a = [1, 2, 3]
# b = a
# print(store(a))
# print(store(b))
