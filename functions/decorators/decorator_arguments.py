def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(2)
def hello():
    print('hello bhai')

hello()
# output
# hello bhai
# hello bhai



# Like we used to call a = func() then a() in closure similar is doinng by decorators