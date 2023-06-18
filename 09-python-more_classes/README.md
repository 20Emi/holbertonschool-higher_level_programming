<h1 align = "center">Python-more_classes</h1>

<h2>Project objectives</h2>

<li>Why Python programming is awesome</li>
<li>What is OOP</li>
<li>“first-class everything”</li>
<li>What is a class</li>
<li>What is an object and an instance</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is an attribute</li>
<li>What are and how to use public, protected and private attributes</li>
<li>What is self</li>
<li>What is a method</li>
<li>What is the special __init__ method and how to use it</li>
<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
<li>What is a property</li>
<li>What is the difference between an attribute and a property in Python</li>
<li>What is the Pythonic way to write getters and setters in Python</li>
<li>What are the special __str__ and __repr__ methods and how to use them</li>
<li>What is the difference between __str__ and __repr__</li>
<li>What is a class attribute</li>
<li>What is the difference between a object attribute and a class attribute</li>
<li>What is a class method</li>
<li>What is a static method</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is and what does contain __dict__ of a class and of an instance of a class</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the getattr function</li>

<h3>What is __str__</h3>
<p>A special method used to define a readable representation of an object as a string. It is part of the string representation protocol and is invoked when the str() function is called on an object or when the print() function is used to print the object.</p>

<h3>What is __repr__</h3>
<p>This is another special method used to define a canonical representation of an object. Unlike __str__, __repr__ is intended to be a more detailed and accurate representation of the object, generally used for debugging and replay purposes.

The main purpose of __repr__ is to return a text string representing the object so that it is possible to accurately reconstruct it using the eval() function.</p>

<h2>Object attribute</h2>
<p><li>Object attributes are specific to an instance of a class. They are defined and accessed through an individual object.</li>
<li>Each object can have its own set of values for object attributes, independent of other objects of the same class.</li>
<li>Object attributes can be created, modified, or accessed using the dot notation (object.attribute).</li>
<li>They are usually defined within the methods of a class or assigned dynamically during runtime.</li>
<li>Object attributes are used to store information that is unique to each instance of a class.</li></p>

<h5>Example</h5>
<pre>
  class Car:
    <b>def __init__(self, brand):</b>
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand)  
<i># Output: Toyota</i>
print(car2.brand)  
<i># Output: Honda</i>
</pre>

<h2>Class Attributes</h2>
<li>Class attributes are shared by all instances of a class. They are defined directly within the class.</li>
<li>All objects of the class have the same value for a class attribute.</li>
<li>Class attributes are accessed using the dot notation (Class.attribute) or through an instance of the class.</li>
<li>They are typically defined outside the methods of a class and are usually placed at the beginning of the class definition.</li>
<li>Class attributes are used to define properties or behaviors that are common to all instances of a class.</li>

<h5>Example</h5>
<pre>
  class Car:
    wheels = 4  <i># Class attribute</i>
  <b>def __init__(self, brand):</b>
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.wheels)  <i># Output: 4</i>
print(car2.wheels)  <i># Output: 4</i>

print(Car.wheels)   <i># Output: 4</i>
</pre>

<h2>Class Method</h2>
<p>A class method is a method that is bound to the class and not the instance of the class. It receives the class itself as the first argument, conventionally named cls. Class methods are defined using the @classmethod decorator before the method definition. They can be accessed via the class itself or any instance of the class.
The primary use case for class methods is when you want to define a method that operates on the class itself, rather than on instances of the class. Class methods can access and modify class-level attributes but cannot access instance-level attributes directly.</p>

<h5>Example.</h5>
<pre>
  class MyClass:
    count = 0
    <b>def __init__(self):</b>
        MyClass.count += 1
   <b>@classmethod</b>
   <b>def get_count(cls):</b>
        return cls.count

obj1 = MyClass()
obj2 = MyClass()

print(obj1.get_count()) <i># Output: 2</i>
print(obj2.get_count()) <i># Output: 2</i>
print(MyClass.get_count()) <i> # Output: 2</i>
</pre>

<h2>Static Method</h2>
<p>A static method is a method that belongs to the class but does not have access to the class or instance. It does not receive any special first argument like class methods do. Static methods are defined using the @staticmethod decorator before the method definition.
Static methods are commonly used when you want to define a utility function that does not require access to instance or class attributes. They are independent of the state of the class or its instances.</p>

<h5>Example</h5>
<pre>
  class MathUtils:
    <b>@staticmethod</b>
    <b>def add_numbers(x, y):</b>
        return x + y

result = MathUtils.add_numbers(3, 5)
print(result)  <i># Output: 8</i>
</pre>

<h4><a href="https://github.com/20Emi"target="_blank">Emily Sánchez</a></h4>
