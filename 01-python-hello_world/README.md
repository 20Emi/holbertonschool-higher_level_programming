<h1 align = "center">Python - Hello, World</h1>

<h2>Project objectives</h2>

<li>How to use the Python interpreter</li>
<li>How to print text and variables using print</li>
<li>How to use strings</li>
<li>What are indexing and slicing in Python</li>
<li>What is the official Python coding style and how to check your code with pycodestyle</li>

<h3>Print function</h3>
<p>The print() function is used to display information on the console or terminal. You can pass one or more arguments separated by commas, which can be text strings, variables or any other value that can be converted to a string.</p>

<h6>sintaxis:</h6> 
<pre>print(value1, value2, ..., valueN)
</pre>
<p>Where value1, value2, ..., valueN are the values you want to print. These values can be text strings, variables or other values that can be converted to strings.

You can use commas to separate the values you want to print. The print() function automatically adds a blank space between the printed values.</p>

<h3>Strings</h3>
<p>strings are used to represent and manipulate text. They are sequences of characters and are declared using single quotes, double quotes or triple quotes.</p>

<h4>Characteristics</h4>
<li>They are immutable objects, which means that they cannot be modified after their creation.</li>

<li>You can access individual characters in a string using indexing, where the first character has index 0.</li>

<li>Python offers a variety of operations and methods for working with strings, such as concatenation, length, substring search, replacement, case conversion, among others.</li>

<li>You can join two strings using the + operator, get the length of a string with the len() function, search for substrings with the in operator, replace substrings using the replace() method, and convert strings to uppercase or lowercase with the upper() and lower() methods respectively.</li>

<li>Strings are important objects in Python and are widely used in text processing and manipulation.</li>

<h3>Indexing:</h3>

<p>Indexing allows you to access individual elements of a sequence by their position. In Python, indexing starts at 0, so the first element of a sequence has an index of 0, the second element has an index of 1, and so on.</p>

<p>To access an element in a specific index, you can use square brackets []with the index value inside.</p>
<h6>Example</h6>
<pre>
$
my_list = [10, 20, 30, 40, 50]
print(my_list[0])
    Output: 10

print(my_list[2])
    Output: 30
$
</pre>

<h3>Slicing</h3>
<p>Slicing allows you to extract a portion of a sequence by specifying a range of indices.</p>
<h4>sintaxis</h4>
<pre>
