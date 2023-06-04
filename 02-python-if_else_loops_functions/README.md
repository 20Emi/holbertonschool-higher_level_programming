<h1 align = "center">Python - if/else, loops, functions</h1>

<h2>Project objectives</h2>

<li>Why indentation is so important in Python</li>
<li>How to use the if, if ... else statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use the while and for loops</li>
<li>How to use the break and continues statements</li>
<li>How to use else clauses on loops</li>
<li>What does the pass statement do, and when to use it</li>
<li>How to use range</li>
<li>What is a function and how do you use functions</li>
<li>What does return a function that does not use any return statement</li>
<li>Scope of variables</li>
<li>What’s a traceback</li>
<li>What are the arithmetic operators and how to use them</li>

<h2>Pass statement.</h2>

<p>It is a null instruction that does not perform any operation. It is used as a placeholder when a syntactically valid instruction is required, but no action needs to be executed at that time.

It is used in several situations, such as:

<li><b>Incomplete code blocks:</b> in the case of writing a function, a class or a loop, pass can be used to avoid syntax errors. It serves as a temporary marker until the actual code is implemented.</li>

<li><b>Future implementation:</b> If you are designing a code structure and know that you will be adding functionality later, you can use pass as a placeholder until you are ready to write the actual code. This allows you to run the code without errors while working on other parts of the program.</li>

<li><b>Abstract classes:</b> In object-oriented programming, an abstract class is a class that cannot be instantiated directly and is used as a basis for other classes</li></p>

<h2>What is a function?</h2>
<p>It is a block of code that performs a specific task and can be called from elsewhere in the program. Some key features of functions are:

<li>They are defined with the keyword 'def', followed by the function name and parentheses that can contain arguments.</li>

<li>They can have optional arguments with default values.</li>

<li>They can have return values using the return keyword.</li>

<li>They allow to organize and modularize the code, which facilitates its reuse and maintenance.</li>

<li>They help improve code readability by dividing it into smaller, more focused parts.</li>

<li>They can be invoked or called from other parts of the program, passing the necessary arguments.</li></p>
<pre>
def sum(a, b):
return a + b

<i># Calling the function and assigning the result to a variable</i>
result = sum(3, 5)
print(result) 
<i># Print 8</i>
</pre>

<h2>What is a traceback?</h2>
<p>It is an error report that shows the sequence of function calls from the point where the exception occurred to the point where the program is handled or output. It provides useful information for identifying and debugging errors in code.

When an exception occurs in Python and is not handled locally, the interpreter automatically generates a traceback. The traceback shows the path that the program followed through the function calls to the point where the exception was generated.</p>
<pre>
Traceback (most recent call last):

  File "script.py", line 5, in <module>

    result = divide_numbers(10, 0)

  File "script.py", line 2, in divide_numbers

    return x / y

ZeroDivisionError: division by zero
</pre>

<h2>Arithmetic operators</h2>

<p>These are special symbols used in programming to perform mathematical operations. These operators allow performing calculations such as addition, subtraction, multiplication, division and other related operations.</p>
