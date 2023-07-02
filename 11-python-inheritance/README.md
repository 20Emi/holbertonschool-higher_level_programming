<h1 align = "center">Python-inheritance</h1>

<h2>Project objectives</h2>

<li>What is a superclass, baseclass or parentclass</li>
<li>What is a subclass</li>
<li>How to list all attributes and methods of a class or instance</li>
<li>When can an instance have new attributes</li>
<li>How to inherit class from another</li>
<li>How to define a class with multiple base classes</li>
<li>What is the default class every class inherit from</li>
<li>How to override a method or attribute inherited from the base class</li>
<li>Which attributes or methods are available by heritage to subclasses</li>
<li>What is the purpose of inheritance</li>
<li>What are, when and how to use isinstance, issubclass, type and super built-in functions</li>

<h2>superclass, baseclass or parentclass</h2>

<p>a superclass, base class, or parent class refers to the class that is being inherited from by another class. When one class inherits from another, the inheriting class is known as the subclass, derived class, or child class.

The superclass provides the common attributes and methods that can be inherited by its subclasses. The subclasses can then add additional attributes and methods or override the existing ones to customize their behavior. This concept is known as inheritance and is a fundamental feature of object-oriented programming.</p>

<h5>Example</h5>

<pre>
  class Superclass:
    <b>def __init__(self):</b>
        self.attribute = "I am from the superclass."
    
    <b>def method(self):</b>
        print("This is a method from the superclass.")

class Subclass(Superclass):
    <b>def __init__(self):</b>
        super().__init__()
        self.attribute = "I am from the subclass."
    
    <b>def method(self):</b>
        print("This is a method from the subclass.")

<i># Creating objects</i>
obj1 = Superclass()
obj2 = Subclass()

<i># Accessing attributes</i>
print(obj1.attribute)  <i># Output: "I am from the superclass."</i>
print(obj2.attribute)  <i># Output: "I am from the subclass."</i>

<i># Calling methods</i>
obj1.method()  <i># Output: "This is a method from the superclass."</i>
obj2.method()  <i># Output: "This is a method from the subclass."</i>
</pre>

<h2>Subclass</h2>

<p>A subclass is a class that inherits attributes and methods from its superclass or parentclass. It extends or specializes the functionality of the superclass by adding its own unique attributes and methods.</p>

<h5>Example</h5>

<pre>
  class Dog(Animal):
    <b>def bark(self):</b>
        print(f"{self.name} is barking.")
</pre>

<h2>Listing Attributes and Methods</h2>

<p>To list all attributes and methods of a class or instance in Python, you can use the dir() function. It returns a list of names comprising the attributes and methods of the specified object.</p>

<h5>Example</h5>
<pre>
  <b>def lookup(obj):</b>
    <i># return the list of available attributes and aethods</i>
    return dir(obj)
</pre>

