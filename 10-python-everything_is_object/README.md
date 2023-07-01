<h1 align = "center">Python-everything_is_object</h1>

<h2>Project objectives</h2>
<li>What is an object</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is the difference between immutable object and mutable object</li>
<li>What is a reference</li>
<li>What is an assignment</li>
<li>What is an alias</li>
<li>How to know if two variables are identical</li>
<li>How to know if two variables are linked to the same object</li>
<li>How to display the variable identifier (which is the memory address in the CPython implementation)</li>
<li>What is mutable and immutable</li>
<li>What are the built-in mutable types</li>
<li>What are the built-in immutable types</li>
<li>How does Python pass variables to functions</li>

<h2>What is an object?</h2>

<p>An object is a fundamental concept in object-oriented programming (OOP). It represents a specific instance of a class, which is a blueprint or template defining the properties and behavior of objects. An object combines data (attributes or properties) and functions (methods) into a single entity. It encapsulates both the data and the operations that can be performed on that data.</p>

<pre>
  <i># Class definition</i>
class Car:
    <b>def __init__(self, color, brand, model):</b>
        self.color = color
        self.brand = brand
        self.model = model

    <b>def startEngine(self):</b>
        <i># Code to start the car's engine</i>

    <b>def accelerate(self, speed):</b>
        <i># Code to accelerate the car to a given speed</i>

<i># Object instantiation</i>
myCar = Car("blue", "Toyota", "Corolla")
</pre>

<h2>What are the built-in mutable types</h2>

<li>Lists: list - Ordered, changeable, and allows duplicate elements.</li>
<li>Dictionaries: dict - Key-value pairs, unordered, and changeable.</li>
<li>Sets: set - Unordered collection of unique elements, mutable.</li>

<h2>What are the built-in immutable types</h2>

<li>Integers: int - Whole numbers without a fractional part.</li>
<li>Floats: float - Numbers with a fractional part.</li>
<li>Strings: str - Ordered sequence of characters.</li>
<li>Tuples: tuple - Ordered, immutable collection of elements.</li>
