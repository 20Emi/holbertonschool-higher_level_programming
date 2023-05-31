<h1 align = "center">Python - Hello, World</h1>

<h2>Project objectives</h2>

<li>How to use the Python interpreter</li>
<li>How to print text and variables using print</li>
<li>How to use strings</li>
<li>What are indexing and slicing in Python</li>
<li>What is the official Python coding style and how to check your code with pycodestyle</li>

<h3>Print function</h3>
<p>The print() function is used to display information on the console or terminal. You can pass one or more arguments separated by commas, which can be text strings, variables or any other value that can be converted to a string.</p>

<h4>sintaxis:</h4> 
<pre>print(value1, value2, ..., valueN)
</pre>
<p>Where value1, value2, ..., valueN are the values you want to print. These values can be text strings, variables or other values that can be converted to strings.

You can use commas to separate the values you want to print. The print() function automatically adds a blank space between the printed values.</p>

<h3>Strings</h3>
<p>strings are used to represent and manipulate text. They are sequences of characters and are declared using single quotes, double quotes or triple quotes.</p>

<h4>Characteristics</h4>
<li>They are immutable objects, which means 7that they cannot be modified after their creation.</li>

<li>You can access individual characters in a string using indexing, where the first character has index 0.</li>

<li>Python offers a variety of operations and methods for working with strings, such as concatenation, length, substring search, replacement, case conversion, among others.</li>

<li>You can join two strings using the + operator, get the length of a string with the len() function, search for substrings with the in operator, replace substrings using the replace() method, and convert strings to uppercase or lowercase with the upper() and lower() methods respectively.</li>

<li>Strings are important objects in Python and are widely used in text processing and manipulation.</li>

<h3>Indexing:</h3>

<p>Indexing allows you to access individual elements of a sequence by their position. In Python, indexing starts at 0, so the first element of a sequence has an index of 0, the second element has an index of 1, and so on.</p>

<p>To access an element in a specific index, you can use square brackets []with the index value inside.</p>
<h6>Example</h6>
<pre>
<b>my_list = [10, 20, 30, 40, 50]
print(my_list[0])</b>

<i># Output: 10</i>
</pre>
<pre>
<b>my_list = [10, 20, 30, 40, 50]
print(my_list[2])</b>

<i># Output: 30</i>
</pre>

<h3>Slicing</h3>
<p>Slicing allows you to extract a portion of a sequence by specifying a range of indices.</p>
<h4>sintaxis</h4>
<pre>
sequence [start:end:step].
</pre>
<p>Where:

<li><b>sequence:</b> is the sequence from which you want to extract a slice, such as a string, list, tuple, or array.</li>

<li><b>start</b> is the starting index of the chunk you want to extract. This index is included in the resulting chunk.</li>

<li><b>end</b> is the end index of the chunk you want to extract. This index is not included in the resulting slice.</li>

<li><b>step</b> is the increment between the indexes. It is optional and defaults to 1I.</li>
</p>
<h5>Example</h5>
<pre>
<b>string = "Hello, World!"
por1 = string[7:12]</b>
<i># Extract "World".</i>
</pre>
<p>Extracts the position from index 7 to index 11 (not inclusive), yielding "World".
</p>
<pre>
<b>string = "Hello, World!"
por2 = string[::2]</b>
<i># Extract "Hlo,Wrd"</i>
</pre>
<p>
 Extracts the position with a step of 2, which means that it selects every second character of the string, yielding "Hlo,Wrd".</p>
<pre>
<b>string = "Hello, World!"
por3 = string[:5]</b>
<i># Extract "Hello"</i>
</pre>
<p>
Extracts the position from the beginning up to index 4 (not inclusive), yielding "Hello".</p>
<pre>
<b>string = "Hello, World!"
por4 = string[7:]</b>
<i># Extract "World!"</i>
</pre>
<p>
Extracts the position from index 7 to the end of the string, getting "World!".</p>
<pre>
<b>string = "Hello, World!"
por5 = string[::-1]</b>
<i># Reverse string: "!dlroW ,olleH"</i>
</pre>
Extracts at the position with a step of -1, which reverses the entire string, yielding "!dlroW ,olleH".

<h4><a href="https://github.com/20Emi"target="_blank">Emily Sánchez</a></h4>
