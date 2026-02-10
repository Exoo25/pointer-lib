# 🧩 Pointer Lib - Python Pointer Simulator

A lightweight Python library to **simulate C-style pointers in Python**.  
It allows you to store Python objects and retrieve them later using short hexadecimal IDs. Perfect for debugging, experimental projects, or building advanced libraries that need object references.

> **Unlike Python's normal references, this library gives you a manual pointer-like system.**  

---

## 🚀 Features

- Store any Python object and get a short **hex ID**  
- Retrieve objects later using their hex ID  
- Free individual pointers manually (`free()`)  
- Free all pointers at once (`free_all()`)  
- Check if a pointer is valid before accessing it (`is_valid()`)  
- Easy-to-use functions with simple interface  
- Minimal dependencies, pure Python  
- Perfect for **experimental memory manipulation** or advanced library development  

---

## 📸 Usage Example

```python
from pointer_table import store, retrieve, free, free_all, is_valid

# Store objects
my_list = [1, 2, 3]
ptr = store(my_list)
print(ptr)  # e.g., 0xABCDE

# Check validity
print(is_valid(ptr))  # True

# Retrieve object
retrieved_list = retrieve(ptr)
print(retrieved_list)  # [1, 2, 3]

# Free the pointer
free(ptr)
print(is_valid(ptr))   # False

# Free all pointers
free_all()
```

---

## 📦 Installation

```bash
cd your-project-path
git clone https://github.com/Exoo25/pointer_lib/
```

> ⚠️ **Important:**  
> - The hex ID is generated using only the lower 20 bits of Python's `id()`, so collisions are **possible** if many objects are stored.  
> - Designed for experimentation, not for production memory management.  

---

## 📄 Functions

### `store(obj)`

Stores a Python object and returns a short hex ID.  

**Args:**  
- `obj`: Any Python object to store  

**Returns:**  
- `str`: Hexadecimal ID, e.g., `"0xABCDE"`  

---

### `retrieve(obj_id_hex)`

Retrieves a Python object using its hex ID.  

**Args:**  
- `obj_id_hex (str)`: Hex string returned by `store()`  

**Returns:**  
- The stored Python object  

**Raises:**  
- `InvalidPointerError` if no object exists for the given ID  

---

### `free(ptr_hex)`

Frees a single pointer from the table.  

**Args:**  
- `ptr_hex (str)`: Hex string of the pointer to free  

**Raises:**  
- `InvalidPointerError` if the pointer is already freed or invalid  

---

### `free_all()`

Frees **all pointers** from the pointer table.  

- After calling, all pointers become invalid  

---

### `is_valid(ptr_hex)`

Checks if a pointer is still valid.  

**Args:**  
- `ptr_hex (str)`: Hex string of the pointer  

**Returns:**  
- `bool`: `True` if valid, `False` if freed or invalid  

---

## 📜 Change Logs

> - [07/02/2026 10:30AM] Initial release of `pointer_lib`  
> - [09/02/2026 08:45PM] Added `free()` to manually free pointers  
> - [09/02/2026 08:50PM] Added `free_all()` to clear all pointers  
> - [09/02/2026 08:55PM] Added `is_valid()` to check pointer validity  
> - [09/02/2026 09:00PM] Updated examples and usage instructions  
