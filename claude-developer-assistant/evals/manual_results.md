# Prompt Experiment V1 /V2

## Criteria

- Accuracy: /2
- Completeness: /2
- Relevance: /2
- Clarity: /2
- Example quality: /2

## Results

| Concept | Prompt A | Prompt B | Winner |
|---|---:|---:|---|
| Decorators | 6/10 | 8/10 | B |
| Generators | 7/10 | 9/10 | B |
| Context Managers | 8/10 | 7/10 | A |

## Test Cases: Decorators // Generators // Context Managers 
Explain: Python Decorators // Generators // Context Managers

## PROMPT V1
```python
PYTHON_EXPLANATION_PROMPT = """
Explain the following Python concept:

<concept>
{concept}
</concept>

The explanation should be appropriate for a Python developer
who understands basic functions and classes.

Include:
- what the concept is
- how it works
- a practical example
- one common mistake
"""
```
### Output V1: Decorators
CONCEPT:
Decorators

EXPLANATION:
Decorators are functions that modify or enhance other functions or classes without permanently changing their source code. They work by taking a function as input, wrapping it with additional functionality, and returning the modified function. Decorators use the @syntax as syntactic sugar for function wrapping. When you use @decorator_name above a function definition, Python automatically passes that function to the decorator and replaces the original function with the decorated version. Decorators are useful for adding cross-cutting concerns like logging, authentication, caching, or timing to functions without repeating code.

EXAMPLE:
```python
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start:.4f} seconds')
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return 'Done'

slow_function()  # Prints execution time automatically
```

Alternatively, you can apply decorators manually: slow_function = timing_decorator(slow_function)

COMMON MISTAKE:
Forgetting to return the wrapper function from the decorator, or forgetting to call the original function inside the wrapper. Another common mistake is not preserving the original function's metadata (name, docstring) using functools.wraps. Without @functools.wraps(func), the decorated function loses its __name__ and __doc__ attributes, making debugging harder. Always use: from functools import wraps and apply @wraps(func) to your wrapper function.

## Output V1: Generators

CONCEPT:
Generators

EXPLANATION:
Generators are functions that use the 'yield' keyword to produce a sequence of values lazily, one at a time, rather than computing and returning all values at once. When a generator function is called, it returns a generator object that can be iterated over. Each time the next() function is called (or the generator is used in a loop), execution resumes from where it left off at the previous yield statement. This approach is memory-efficient because values are generated on-demand rather than stored in memory, making generators ideal for processing large datasets or infinite sequences.

EXAMPLE:
```python
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Usage
for num in count_up(5):
    print(num)  # prints 0, 1, 2, 3, 4

# Or manually:
gen = count_up(3)
print(next(gen))  # prints 0
print(next(gen))  # prints 1
print(next(gen))  # prints 2
# print(next(gen))  # would raise StopIteration
```

COMMON MISTAKE:
A common mistake is assuming a generator is a regular function and trying to access multiple values without iteration. For example, calling a generator function multiple times thinking each call advances the generator, when actually each call creates a new generator object. Another mistake is forgetting that generators are exhausted after iteration completes; iterating over the same generator object a second time yields nothing because the generator has already been consumed and won't restart unless you create a new one.

## Output V1: Context Managers
CONCEPT:
Context Managers

EXPLANATION:
Context managers are Python objects that manage resources and define what happens when entering and exiting a block of code. They implement the `__enter__()` and `__exit__()` methods, which are automatically called by the `with` statement. The `__enter__()` method runs when entering the block and typically acquires resources (like opening a file), while `__exit__()` runs when leaving the block (whether normally or due to an exception) and handles cleanup. This ensures resources are properly released even if errors occur, eliminating the need for try-finally blocks.

EXAMPLE:
```python
class DatabaseConnection:
    def __enter__(self):
        print('Connecting to database...')
        self.connection = 'DB_CONNECTION'
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Closing database connection...')
        self.connection = None
        return False

with DatabaseConnection() as db:
    print(f'Using {db}')
    # Connection is automatically closed here

# Alternatively, use the contextlib decorator:
from contextlib import contextmanager

@contextmanager
def open_database():
    print('Opening database')
    connection = 'DB_CONNECTION'
    try:
        yield connection
    finally:
        print('Closing database')

with open_database() as db:
    print(f'Using {db}')
```

COMMON MISTAKE:
A common mistake is forgetting to return `False` (or a falsy value) from `__exit__()` when you want exceptions to propagate. If you return `True`, the exception is suppressed and the caller won't know an error occurred. Another mistake is not properly handling all three exception parameters (`exc_type`, `exc_val`, `exc_tb`) — if any exception occurs in the with block, these will be populated with exception information, and you should handle them appropriately or allow them to propagate by returning `False`.


## PROMPT V2
```python
PYTHON_EXPLANATION_PROMPT = """
You are a senior Python engineer mentoring a developer.

Explain the following Python concept:

<concept>
{concept}
</concept>

The developer already understands:
- variables
- functions
- classes
- basic object-oriented programming

Structure the explanation as follows:

1. Definition
2. Mental model
3. How it works
4. Practical example
5. Common mistake
6. When to use it
7. When NOT to use it

Do not oversimplify.
Do not introduce concepts unrelated to the requested topic.
Use technically accurate Python examples.
"""
```
### Output V2: Decorators

CONCEPT:
Decorators

EXPLANATION:
Decorators are higher-order functions that take another function (or class) as input and return a modified version of it without permanently altering the original. They enable you to 'wrap' functions or classes to extend or modify their behavior through a declarative syntax.

Mental Model: Think of a decorator as a wrapper or middleware. Just as a gift box wraps a present and adds decoration without changing what's inside, a decorator wraps a function and adds functionality around it. The decorator receives the original function, optionally modifies its behavior by adding pre-processing, post-processing, or replacing logic entirely, then returns a callable that will execute this enhanced behavior.

How It Works: At its core, a decorator is a callable that accepts a function and returns a new function. When you write @decorator above a function definition, Python immediately passes that function to the decorator and rebinds the function name to whatever the decorator returns. This happens at function definition time, not at call time.

The Mechanics: (1) Define a decorator function that takes a function as a parameter. (2) Inside, define a wrapper function that contains the enhanced logic. (3) The wrapper typically calls the original function using *args and **kwargs to preserve its signature. (4) Return the wrapper from the decorator. (5) Use @decorator_name syntax above your target function.

When to Use: Decorators excel at cross-cutting concerns that apply to multiple functions: logging, authentication, caching, performance measurement, input validation, retry logic, or access control. They reduce code duplication and keep business logic separate from infrastructure concerns.

When NOT to Use: Avoid decorators when: (1) The modification is one-time only for a single function. (2) The logic is core to understanding the function's purpose (transparency matters). (3) The decorator chain becomes deeply nested (hard to debug). (4) You're just wrapping one simple operation that doesn't need reuse.

EXAMPLE:
# Basic decorator example
```python
import functools
import time

def timer_decorator(func):
    @functools.wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # Call the original function
        elapsed = time.time() - start
        print(f'{func.__name__} took {elapsed:.4f} seconds')
        return result
    return wrapper

@timer_decorator
def slow_operation(n):
    time.sleep(n)
    return f'Completed after {n} seconds'

print(slow_operation(1))  # Prints timing info before result
```
# Decorator with arguments
```python
def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f'Attempt {attempt} failed, retrying...')
        return wrapper
    return decorator

@retry(max_attempts=2)
def unreliable_api_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError('API unavailable')
    return 'Success'
```

# Class decorator example
```python
def add_repr(cls):
    def __repr__(self):
        attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
        return f'{cls.__name__}({attrs})'
    cls.__repr__ = __repr__
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Alice', 30)
print(p)  # Person(name='Alice', age=30)
```

COMMON MISTAKE:
Common Mistake 1 - Forgetting functools.wraps: When you create a wrapper function, it has its own __name__, __doc__, and other metadata. Without @functools.wraps(func), the decorated function loses its original metadata. This breaks introspection tools, documentation systems, and debugging. Always use @functools.wraps.

Common Mistake 2 - Incorrect argument handling: Using a fixed parameter list like def wrapper(x, y) instead of *args, **kwargs makes the decorator brittle and breaks when applied to functions with different signatures. Always use *args, **kwargs to preserve the original function's signature.

Common Mistake 3 - Confusing decorator syntax with decorator-with-arguments syntax: @decorator and @decorator() are different. The first applies the decorator directly. The second first calls decorator(), which must return a decorator function. Mixing these up causes 'function is not callable' errors.

Common Mistake 4 - Modifying original behavior without returning the result: Forgetting to return func(*args, **kwargs) means the wrapper runs but the original function's return value is lost. The calling code gets None instead of the expected result.

Common Mistake 5 - Stacking decorators without understanding order: Decorators are applied bottom-to-top at definition time. @decorator_a \n @decorator_b \n def func() means decorator_a(decorator_b(func)). Many developers misunderstand this execution order and debugging becomes difficult.

## Output V2: Generators

CONCEPT:
Generators

EXPLANATION:
Generators are special functions that use the `yield` keyword to produce a sequence of values lazily, one at a time, instead of computing and storing all values in memory at once. They return a generator object that implements the iterator protocol, allowing you to iterate through values using `next()` or in a for loop.

MENTAL MODEL: Think of a generator as a pausable function. When you call it, it doesn't execute immediately. Instead, it returns a generator object. Each time you request the next value (via `next()` or iteration), the function resumes from where it paused, executes until it hits a `yield`, pauses again, and returns that value. This pause-resume mechanism is the core difference from regular functions.

HOW IT WORKS: When you call a generator function, Python creates a generator object without executing the function body. The function only executes when you call `next()` on the generator. When execution reaches a `yield` statement, the function pauses and returns the yielded value. On the next `next()` call, execution resumes immediately after the `yield`. This continues until the function returns (implicitly returns None or explicitly raises StopIteration), which signals the end of iteration.

PRACTICAL EXAMPLE:
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(next(gen))  # Output: 3
print(next(gen))  # Output: 2
print(next(gen))  # Output: 1
# next(gen) would raise StopIteration

for value in countdown(3):
    print(value)  # Prints 3, 2, 1

# Generator expressions (like list comprehensions):
gen_expr = (x**2 for x in range(5))
print(list(gen_expr))  # [0, 1, 4, 9, 16]
```

WHEN TO USE: Use generators when you need to iterate over large datasets, infinite sequences, or computationally expensive sequences where you don't need all values at once. They're ideal for streaming data, reading large files line-by-line, and implementing custom iteration patterns. They provide memory efficiency and improve performance because values are computed on-demand.

WHEN NOT TO USE: Don't use generators when you need to access values multiple times (generators are consumed after iteration), need random access to elements, or need to know the length upfront. If you need a small, fixed dataset or must iterate through values repeatedly, a list is more appropriate. Generators are also less suitable for simple, single-pass scenarios where list comprehensions would be clearer.

EXAMPLE:
```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Memory-efficient: doesn't store all fibonacci numbers
for fib in fibonacci(100):
    print(fib)  # Prints 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
```
# Reading large files without loading entire file into memory
```python
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file('huge_file.txt'):
    process(line)  # Processes one line at a time
```
# Generator with send() for two-way communication
```python
def echo():
    while True:
        value = yield
        print(f'Received: {value}')

gen = echo()
next(gen)  # Prime the generator
gen.send('Hello')  # Output: Received: Hello
```

COMMON MISTAKE:
MISTAKE 1 - Treating generators as reusable sequences:
```python
gen = (x**2 for x in range(5))
print(list(gen))  # [0, 1, 4, 9, 16]
print(list(gen))  # [] - Generator is exhausted!
```
Generators are consumed after iteration. You must recreate them or convert to a list if you need multiple iterations.

MISTAKE 2 - Expecting length:
```python
gen = (x for x in range(10))
len(gen)  # TypeError: object of type 'generator' has no len()
```
Generators don't support `len()` because they're lazy and may be infinite.

MISTAKE 3 - Confusing yield with return:
```python
def bad_gen():
    return [1, 2, 3]  # Returns a list, not a generator

gen = bad_gen()
print(next(gen))  # TypeError: 'list' object is not an iterator
```
Use `yield` to create generators, not `return`.

MISTAKE 4 - Forgetting to prime generators with send():
```python
def echo():
    while True:
        value = yield
        print(value)

gen = echo()
gen.send('Hello')  # TypeError: can't send non-None value to just-started generator
next(gen)  # Correct: prime with next() first
gen.send('Hello')  # Works correctly
```

## Output V2: Context Managers
