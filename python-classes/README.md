<h1 align = "center">Python-classes</h1>

<h2>Project objectives</h2>

<li>What is OOP</li>

<li>“first-class everything”</li>

<li>What is a class</li>

<li>What is an object and an instance</li>

<li>What is the difference between a class and an object or instance</li>

<li>What is an attribute</li>

<li>What are and how to use public, protected and private attributes</li>

<li>What is self</li>

<li>Whats is a method</li>

<li>What is the special __init__ method and how to use it</li>

<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>

<li>What is a property</li>

<li>What is the difference between an attribute and a property in Python</li>

<li>What is the Pythonic way to write getters and setters in Python</li>

<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>

<li>How to bind attributes to object and classes</li>

<li>What is the __dict__ of a class and/or instance of a class and what does it contain</li>

<li>How does Python find the attributes of an object or class</li>

<li>How to use the getattr function</li>

<h2>Object-oriented program</h2>

It is a paradigm that is based on objects. It combines data and functionalities and wraps them inside objects.
two main aspects are classes and objects. 

<h2>class</h2>

<li>A class is a template or model that defines the structure and behavior of an object in object-oriented programming.</li>

<li>It defines the attributes (variables) and methods (functions) that an object created from that class will have.</li>
<li>A class creates a new type where objects are instances of the class</li>

<h2>Objects</h2>
<li>can store data using ordinary variables that belong to the object.</li>

<li>Fields are variables that are associated with a specific object or class. These fields store information relevant to the object or class in question. On the other hand, methods are functions that are related to an object or class and provide specific functionality. Methods can access and manipulate the fields of an object, and are used to perform different operations and actions related to the object or class.</li>
<li>Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively</li>

<h2>instance</h2>
An instance is a specific object created from a class. When an instance is created, memory is allocated for that particular object and its attributes are initialized as defined in the class. Each instance has its own unique identity and may have different values for its attributes.
<h5>Example</h5>
<pre>
class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def greet(self):

        print("Hello, my name is", self.name).
</pre>

<h2>What are and how to use public, protected and private attributes</h2>

<h3>Public</h3>
Attributes and methods are considered public by default, which means they can be accessed and modified from anywhere.
To define a public attribute, simply declare it without any leading underscores.

<h5>Example</h5>
<pre>
class MyClass:

    def __init__(self):

        self.public_attribute = 10

    def public_method(self):

        # Code goes here

        pass
</pre>
 
 <h3>Protected</h3>
 There is a convention to use a single leading underscore (_) to indicate that an attribute or method should be treated as protected. 
 
<h5>Example</h5>
<pre>
 class MyClass:

    def __init__(self):

        self._protected_attribute = 20

    def _protected_method(self):

        # Code goes here
        pass
</pre>

<h3>Private</h3>
there is a convention to use a double leading underscore ( __ ) to indicate that an attribute or method should be treated as private.
The names of private members are mangled to include the class name, which makes them still accessible but discourages direct usage.

<h5>Exmple</h5>
<pre>
class MyClass:

    def __init__(self):

        self.__private_attribute = 30

    def __private_method(self):

        # Code goes here

        pass


</pre>
