# Part B: Predict the Output

# Q1. Dictionary Aliasing
d = {"a": 1, "b": 2}
d2 = d
d2["c"] = 3
print("Q1:", len(d))
# Output: 3
# Explanation: Both variables refer to the same dictionary.


# Q2. Shallow Copy
d = {"x": [1]}
e = d.copy()
e["x"].append(2)
print("Q2:", d)
# Output: {'x': [1, 2]}
# Explanation: The inner list is shared in a shallow copy.


# Q3. Dictionary Comprehension
print("Q3:", {k: v for k, v in zip("abc", range(3)) if v})
# Output: {'b': 1, 'c': 2}
# Explanation: The condition excludes the value 0.


# Q4. setdefault()
d = {"a": 1}
print("Q4:", d.setdefault("a", 9), d.setdefault("b", 5), d)
# Output: 1 5 {'a': 1, 'b': 5}
# Explanation: Existing keys are not overwritten; missing keys are inserted.


# Q5. Equivalent Dictionary Keys
d = {1: "a", 1.0: "b", True: "c"}
print("Q5:", d, len(d))
# Output: {1: 'c'} 1
# Explanation: 1, 1.0 and True are equivalent dictionary keys.


# Q6. Deleting During Iteration
d = {"a": 1, "b": 2, "c": 3}
try:
    for k in d:
        if d[k] == 2:
            del d[k]
except RuntimeError as error:
    print("Q6:", error)
# Output: RuntimeError: dictionary changed size during iteration
# Explanation: Deleting a key while iterating changes dictionary size.


# Q7. pop() and popitem()
d = {"a": 1, "b": 2}
print("Q7:", d.pop("z", None), d.popitem())
# Output: None ('b', 2)
# Explanation: pop() returns the default for a missing key.
# popitem() removes the last inserted item.


# Q8. Dictionary Comprehension with Duplicate Values
print("Q8:", {v: k for k, v in {"a": 1, "b": 1}.items()})
# Output: {1: 'b'}
# Explanation: The later value overwrites the earlier value for the same key.