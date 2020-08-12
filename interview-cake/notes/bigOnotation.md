# Big O Notation

Big O notation is the language we use for talking about how long an algorithm takes to run.
With big O notation we express the runtime in terms of -- how quickly it grows relative to the input, as the input gets arbitrarily large.

## Some examples:

```python
def print_first_item(items):
    print(items[0])
```
This function runs in **O(1)** time (or "constant time") relative to its input.

```python
def print_all_items(items):
    for item in items:
        print(item)

def say_hi_n_times(n):
    for time in range(n):
        print("hi")

def print_all_items(items):
    for item in items:
        print(item)
```
This function runs in **O(n)** time (or "linear time"), where n is the number of items in the list.

```python
def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)
```
This function runs in **O(n^2)** time (or "quadratic time").


### Drop the constants
When you're calculating the big O complexity of something, you just throw out the constants.

```python
def print_all_items_twice(items):
    for item in items:
        print(item)
    
    for item in items:
        print(item)
```
This is **O(2n)**, which we just call **O(n)**.

```python
def print_first_item_then_first_half_then_say_hi_100_items(items):
    print(items[0])
    
    middle_index = len(items) / 2
    index = 0
    while index < middle_index:
        print(items[index])
        index += 1
    
    for time in range(100):
        print("hi")
```
This is **O(1 + n/2 + 100)**, which we just call **O(n)**.

For big O notation we're looking at what happen **as n gets arbitrarily large**. As n gets really big, adding 100 or dividing by 2 has
a decreasingly significant effect.

### Drop the less significant terms

```python
def print_all_numbers_then_all_pair_sums(numbers):
    print("There are the numbers:")
    for number in numbers:
        print(number)
    
    print("and these are their sums:")
    for first_number in numbers:
        for second_number in numbers:
            print(first_number + second_number)
 ```
 Here our runtine is **O(n + n^2)**< which we just call**O(n^2)**. Even if it was **O(n^2/2 + 100n)**, it would still be **O(n^2)**.
 
 Similarly:
 
 + O(n^3 + 50n^2 + 10000) is O(n^3)
 + O((n+30)∗(n+5)) is O(n^2)
 
 ### We're usually talking about the "worst case"
 
 Sometimes the worst case runtime is significantly worse than the best case runtime.
 
 ```python
 def contains(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False
```
Here we might have 100 items in our haystack, but the first item might be the needle, in which case we would return in just 1 iteration 
of our loop.

In general we'd say this is O(n) runtime and the "worst case" part would be implied. But to be more specific we could say this
is worst case O(n) and best case O(1) runtime. For some algorithms we can also make rigorous statements about the "average case" runtime.

# Space Complexity: the final frontier

Sometimes we want to optimize for using less memory instead of (or in addition to) using less time.
Talking about memeory cost (or "sapce complexity") is very similar to talking about the time cost.

```python
def say_hi_n_times(n):
    for time in range(n):
        print("hi")
```
This function takes O(1) space (we use a fixed number of varaibles).

```python
def list_of_hi_n_times(n):
    hi_list = []
    for time in range(n):
        h1_list.append("hi")
    return hi_list
```
This function takes O(n) space (the size of hi_list scales with the size of the input)

**Usually when we talk about space complexity, we're talking about additional space**, so we don't include space taken up by the inputs.
For example, this function takes constant space even though the input has n items

```python
def get_largest_item(items):
    largest = float('-inf')
    for item in items:
        if item > largest:
            largest = items
    return largest
```

**Sometimes htere's a tradeoff between saving time and saving space**, so you have to decide which one you're optimizing for.
    
