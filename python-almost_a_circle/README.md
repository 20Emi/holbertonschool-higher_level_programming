<h1 align = "center">Python-almost_a_circle</h1>

<h2>Project objectives</h2>

<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>What is *args and how to use it</li>
<li>What is **kwargs and how to use it</li>
<li>How to handle named arguments in a function</li>

<h2>How to Implement Unit Testing in a Large Project</h2>

<p>Python provides various unit testing frameworks, such as unittest, pytest, and nose, among others. Here, we'll use the built-in unittest module to demonstrate unit testing in a large project.

<li>Create a test file (e.g., test_module.py) alongside your main code files.</li>
<li>Import the unittest module and the functions/classes you want to test.</li>
<li>Define test cases as classes that inherit from unittest.TestCase.</li>
<li>Write test methods inside the test case classes, using assertions to check expected outcomes.</li>
<li>Run the tests using a test runner like unittest.TextTestRunner.</li>
</p>

<h5>Example</h5>
<pre>
  <i># main_module.py</i>
<b>def add_numbers(a, b):</b>
    return a + b
</pre>

<pre>
  <i># test_module.py</i>
import unittest
from main_module import add_numbers

class TestAddNumbers(unittest.TestCase):
    <b>def test_add_numbers_positive(self):</b>
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

    <b>def test_add_numbers_negative(self):</b>
        result = add_numbers(-3, -5)
        self.assertEqual(result, -8)

if __name__ == "__main__":
    unittest.main()
</pre>

<h2>Serialization and Deserialization of a Class</h2>

Serialization is the process of converting an object or data structure into a format suitable for storage or transmission. Deserialization is the reverse process, where serialized data is converted back into the original object or data structure.

<h3>How to Serialize and Deserialize a Class</h3>

<li>Import the json module.</li>
<li>Define a class with its properties and methods.</li>
<li>Implement serialization by converting the class instance to a JSON string using json.dumps().</li>
<li>Implement deserialization by converting the JSON string back to a class instance using json.loads().</li>

<h5>Example</h5>
<pre>
  import json

class Person:
    <b>def __init__(self, name, age):</b>
        self.name = name
        self.age = age

<i>#Serialization</i>
person_object = Person("John", 30)
serialized_person = json.dumps(person_object.__dict__)

<i>#Deserialization</i>
deserialized_person = json.loads(serialized_person)
print(deserialized_person["name"])  <i># Output: "John"</i>
print(deserialized_person["age"])   <i># Output: 30</i>
</pre>

<h2>*args and How to Use it</h2>

In Python, the *args syntax allows a function to accept a variable number of non-keyword arguments. The *args parameter collects these arguments into a tuple within the function. This is useful when you don't know in advance how many arguments will be passed.

<h5>Example</h5>
<pre>
  <b>def print_args(*args):</b>
    for arg in args:
        print(arg)

print_args(1, 2, 3)  <i># Output: 1 2 3</i>
print_args("Hello", "World")  <i># Output: Hello World</i>
</pre>

<h2>**kwargs and How to Use it</h2>

Similar to *args, the **kwargs syntax allows a function to accept a variable number of keyword arguments. The **kwargs parameter collects these arguments into a dictionary within the function. This is useful when you want to pass key-value pairs to a function.

<h5>Example</h5>
<pre>
  <b>def print_kwargs(**kwargs):</b>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="John", age=30)  <i># Output: name: John, age: 30</i>
print_kwargs(country="USA", city="New York")  <i># Output: country: USA, city: New York</i>
</pre>
