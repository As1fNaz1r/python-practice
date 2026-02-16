# Miscellaneous Attribute Access Concepts

## Attribute Lookup Order (MRO)

When you access `obj.attr`, Python searches in this order:

1. **Data descriptors** (from class, has `__get__` and `__set__`)
2. **Instance `__dict__`** (obj's own attributes)
3. **Non-data descriptors** (from class, only has `__get__`)
4. **Class `__dict__`** (class attributes)
5. **Parent classes** (following MRO)
6. **`__getattr__`** (if defined)
7. **`AttributeError`** (if nothing found)

```python
class Parent:
    x = "parent"

class Child(Parent):
    def __getattr__(self, name):
        return "fallback"

obj = Child()
obj.y = "instance"

print(obj.y)  # Step 2: "instance" (instance dict)
print(obj.x)  # Step 4: "parent" (class dict)
print(obj.z)  # Step 6: "fallback" (__getattr__)
```

## Descriptors vs Attribute Access Methods

### Descriptors (Property-like)
```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        return "descriptor value"
    
    def __set__(self, obj, value):
        print(f"Setting to {value}")

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)  # Calls Descriptor.__get__
obj.attr = 10    # Calls Descriptor.__set__
```

### How They Interact
- Descriptors are checked BEFORE instance `__dict__`
- `__getattribute__` can intercept descriptor access
- `__getattr__` is called AFTER descriptor lookup fails

## `__dir__` - Customizing Attribute Listing

Controls what `dir(obj)` returns:

```python
class Custom:
    def __init__(self):
        self.visible = 1
        self._hidden = 2
    
    def __dir__(self):
        return ["visible", "custom_attr"]

obj = Custom()
print(dir(obj))  # ["visible", "custom_attr"]
print(obj._hidden)  # Still accessible! Just not in dir()
```

## `__slots__` - Restricting Attributes

Prevents dynamic attribute creation and saves memory:

```python
class Restricted:
    __slots__ = ["x", "y"]  # Only these attributes allowed
    
    def __init__(self):
        self.x = 1
        self.y = 2

obj = Restricted()
obj.z = 3  # AttributeError: 'Restricted' object has no attribute 'z'
print(obj.__dict__)  # AttributeError: no __dict__!
```

### Benefits of `__slots__`
- Faster attribute access
- Lower memory usage (no `__dict__`)
- Prevents typos (can't accidentally create new attributes)

### Limitations
- Can't add new attributes dynamically
- Inheritance can be tricky
- No `__dict__` (unless explicitly added to `__slots__`)

## `hasattr`, `getattr`, `setattr`, `delattr` Built-ins

These built-in functions use the dunder methods internally:

```python
class Example:
    def __init__(self):
        self.x = 10

obj = Example()

# hasattr - checks if attribute exists
print(hasattr(obj, "x"))  # True
print(hasattr(obj, "y"))  # False

# getattr - gets attribute with optional default
print(getattr(obj, "x"))        # 10
print(getattr(obj, "y", "default"))  # "default"

# setattr - sets attribute
setattr(obj, "y", 20)
print(obj.y)  # 20

# delattr - deletes attribute
delattr(obj, "y")
print(hasattr(obj, "y"))  # False
```

### How They Work
```python
hasattr(obj, "x")  # Calls obj.__getattribute__("x")
getattr(obj, "x")  # Calls obj.__getattribute__("x")
setattr(obj, "x", 10)  # Calls obj.__setattr__("x", 10)
delattr(obj, "x")  # Calls obj.__delattr__("x")
```

## Proxy Pattern

Forwarding all attribute access to another object:

```python
class Proxy:
    def __init__(self, target):
        # Use object.__setattr__ to avoid triggering our __setattr__
        object.__setattr__(self, "_target", target)
    
    def __getattribute__(self, name):
        if name == "_target":
            return object.__getattribute__(self, name)
        target = object.__getattribute__(self, "_target")
        return getattr(target, name)
    
    def __setattr__(self, name, value):
        target = object.__getattribute__(self, "_target")
        setattr(target, name, value)

class Real:
    def __init__(self):
        self.value = 42

real = Real()
proxy = Proxy(real)
print(proxy.value)  # 42 (forwarded to real)
proxy.value = 100
print(real.value)   # 100 (changed on real object)
```

## Lazy Initialization Pattern

Load expensive resources only when needed:

```python
class LazyLoader:
    def __init__(self):
        self._cache = {}
    
    def __getattr__(self, name):
        if name not in self._cache:
            print(f"Loading {name}...")
            self._cache[name] = self._load_resource(name)
        return self._cache[name]
    
    def _load_resource(self, name):
        # Simulate expensive operation
        return f"Resource: {name}"

obj = LazyLoader()
print(obj.database)  # Loads on first access
print(obj.database)  # Uses cached value
```

## Common Interview Questions

### Q1: Why doesn't this work?
```python
class A:
    def __getattribute__(self, name):
        return self.__dict__[name]  # Infinite recursion!
```
**Answer:** `self.__dict__` calls `__getattribute__` again. Use `super().__getattribute__(name)`.

### Q2: Why isn't `__getattr__` called?
```python
class B:
    def __init__(self):
        self.x = None
    
    def __getattr__(self, name):
        return "default"

b = B()
print(b.x)  # None, not "default"
```
**Answer:** `__getattr__` only runs if attribute doesn't exist. `x` exists (even though it's `None`).

### Q3: What's the difference?
```python
obj.x = 10      # Calls __setattr__
obj.__dict__["x"] = 10  # Bypasses __setattr__
```
**Answer:** Direct `__dict__` access bypasses `__setattr__`, useful inside `__setattr__` to avoid recursion.

## Performance Considerations

- `__getattribute__` adds overhead to EVERY attribute access
- `__getattr__` only adds overhead for missing attributes
- `__slots__` is faster and uses less memory than `__dict__`
- Descriptors have some overhead but are optimized in CPython

## Best Practices

1. **Prefer `__getattr__` over `__getattribute__`** unless you need total control
2. **Always call `super()`** in `__getattribute__`, `__setattr__`, `__delattr__`
3. **Use `__slots__`** for classes with many instances
4. **Document magic behavior** - these methods can be surprising
5. **Test edge cases** - recursion, missing attributes, inheritance
6. **Consider performance** - these methods run frequently

## Debugging Tips

```python
class Debugged:
    def __getattribute__(self, name):
        print(f"GET: {name}")
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        print(f"SET: {name} = {value}")
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        print(f"DEL: {name}")
        super().__delattr__(name)
```

This helps trace attribute access patterns and find bugs.
