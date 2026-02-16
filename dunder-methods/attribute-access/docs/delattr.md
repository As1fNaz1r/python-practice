# `__delattr__` - The Delete Interceptor

## What It Does
Intercepts **EVERY** attribute deletion on an object.

## The Golden Rule
- Called whenever you do `del obj.x`
- Controls what can and cannot be deleted

## Basic Example
```python
class Logged:
    def __delattr__(self, name):
        print(f"Deleting {name}")
        super().__delattr__(name)

obj = Logged()
obj.x = 10
del obj.x  # Prints: "Deleting x"
```

## Critical Rules

### 1. Always Use `super().__delattr__()`
```python
# ❌ WRONG - Doesn't actually delete
def __delattr__(self, name):
    print(f"Deleting {name}")
    # Forgot to call super()!

# ✅ RIGHT
def __delattr__(self, name):
    print(f"Deleting {name}")
    super().__delattr__(name)
```

### 2. Can Prevent Deletion
```python
class Protected:
    def __delattr__(self, name):
        if name == "important":
            raise AttributeError("Cannot delete 'important'")
        super().__delattr__(name)

obj = Protected()
obj.important = "data"
obj.temp = "value"

del obj.temp       # OK
del obj.important  # AttributeError
```

## Use Cases

### 1. Prevent Deletion of Critical Attributes
```python
class Config:
    PROTECTED = {"api_key", "secret"}
    
    def __delattr__(self, name):
        if name in self.PROTECTED:
            raise AttributeError(f"Cannot delete protected attribute '{name}'")
        super().__delattr__(name)
```

### 2. Resource Cleanup
```python
class FileHandler:
    def __delattr__(self, name):
        if name == "file":
            if hasattr(self, "file") and self.file:
                self.file.close()
                print("File closed before deletion")
        super().__delattr__(name)
```

### 3. Logging Deletions
```python
class Audited:
    def __delattr__(self, name):
        value = getattr(self, name, None)
        print(f"Audit: Deleted {name} (was {value})")
        super().__delattr__(name)
```

### 4. Cascade Deletion
```python
class Node:
    def __delattr__(self, name):
        if name == "children":
            # Clean up child nodes first
            for child in self.children:
                del child
        super().__delattr__(name)
```

### 5. Debugging
```python
class Debugged:
    def __delattr__(self, name):
        import traceback
        print(f"Deleting {name} from:")
        traceback.print_stack()
        super().__delattr__(name)
```

## Common Patterns

### Read-Only Object
```python
class Immutable:
    def __delattr__(self, name):
        raise AttributeError("Cannot delete attributes from immutable object")
```

### Conditional Deletion
```python
class Conditional:
    def __init__(self):
        self.locked = False
    
    def __delattr__(self, name):
        if self.locked:
            raise AttributeError("Object is locked")
        super().__delattr__(name)
```

### Soft Delete (Mark Instead of Delete)
```python
class SoftDelete:
    def __init__(self):
        self._deleted = set()
    
    def __delattr__(self, name):
        self._deleted.add(name)
        # Don't actually delete, just mark as deleted
    
    def __getattribute__(self, name):
        deleted = super().__getattribute__("_deleted")
        if name in deleted:
            raise AttributeError(f"'{name}' has been deleted")
        return super().__getattribute__(name)
```

## Working with `__setattr__` and `__delattr__`
```python
class Controlled:
    def __setattr__(self, name, value):
        print(f"Set {name} = {value}")
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        print(f"Delete {name}")
        super().__delattr__(name)

obj = Controlled()
obj.x = 10    # "Set x = 10"
del obj.x     # "Delete x"
```

## Common Pitfalls

### 1. Forgetting to Call `super()`
```python
# ❌ BAD - Attribute never actually deleted
def __delattr__(self, name):
    print(f"Deleting {name}")
    # Oops, forgot super()!
```

### 2. Accessing Deleted Attribute
```python
def __delattr__(self, name):
    value = self.name  # Might not exist anymore!
    super().__delattr__(name)

# ✅ BETTER
def __delattr__(self, name):
    value = getattr(self, name, None)  # Safe
    super().__delattr__(name)
```

### 3. Circular Dependencies
```python
class Bad:
    def __delattr__(self, name):
        del self.other  # Might cause issues if 'other' doesn't exist
        super().__delattr__(name)
```

## When to Use
- Preventing deletion of critical attributes
- Resource cleanup (closing files, connections)
- Logging/auditing deletions
- Implementing soft deletes
- Debugging attribute lifecycle
- Enforcing object invariants

## Less Common Than Others
`__delattr__` is used less frequently than `__getattr__` or `__setattr__` because explicit deletion is relatively rare in Python code. Most objects rely on garbage collection rather than explicit `del` statements.
