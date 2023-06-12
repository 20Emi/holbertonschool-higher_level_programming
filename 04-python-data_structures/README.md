<h1 align = "center">python-data_structures</h1>

<h2>Project objectives</h2>

<li>What are lists and how to use them</li>

<li>What are the differences and similarities between strings and lists</li>

<li>What are the most common methods of lists and how to use them</li>

<li>How to use lists as stacks and queues</li>

<li>What are list comprehensions and how to use them</li>

<li>What are tuples and how to use them</li>

<li>When to use tuples versus lists</li>

<li>What is a sequence</li>

<li>What is tuple packing</li>

<li>What is sequence unpacking</li>

<li>What is the del statement and how to use it</li>
<h2>prototype of the functions</h2>
<table>
  <tr>
    <td>File</td>
    <td>Prototype</td>
  </tr>
  <tr>
    <td>0-print_list_integer.py</td>
    <td>def print_list_integer(my_list=[]):</td>
  </tr>
  <tr>
    <td>1-element_at.py</td>
    <td>def element_at(my_list, idx):</td>
  </tr>
  <tr>
    <td>2-replace_in_list.py</td>
    <td>def replace_in_list(my_list, idx, element):</td>
  </tr>
  <tr>
    <td>3-print_reversed_list_integer.py</td>
    <td>def print_reversed_list_integer(my_list=[]):</td>
  </tr>
  <tr>
    <td>4-new_in_list.py</td>
    <td>def new_in_list(my_list, idx, element):</td>
  </tr>
  <tr>
    <td>5-no_c.py</td>
    <td>def no_c(my_string):</td>
  </tr>
  <tr>
    <td>6-print_matrix_integer.py</td>
    <td>def print_matrix_integer(matrix=[[]]):</td>
  </tr>
  <tr>
    <td>7-add_tuple.py</td>
    <td>def add_tuple(tuple_a=(), tuple_b=()):</td>
  </tr>
  <tr>
    <td>8-multiple_returns.py</td>
    <td>def multiple_returns(sentence):</td>
  </tr>
  <tr>
    <td>9-max_integer.py</td>
    <td>def max_integer(my_list=[]):</td>
  </tr>
  <tr>
    <td>10-divisible_by_2.py</td>
    <td>def divisible_by_2(my_list=[]):</td>
  </tr>
  <tr>
    <td>11-delete_at.py</td>
    <td>def delete_at(my_list=[], idx=0):</td>
  </tr>
  </table>

<h2>Lists</h2>
<p>You store and manipulate collections of items. They are ordered, mutable, and can contain elements of different data types. Lists are defined by enclosing comma-separated values within square brackets [ ].
</p>

<h3>Common Methods of Lists</h3>
<p>
<li><b>append():</b> Adds an item to the end of the list.</li>

<li><b>extend():</b> Appends multiple items from an iterable to the list.</li>

<li><b>insert():</b> Inserts an item at a specified position.</li>

<li><b>remove():</b>Removes the first occurrence of a specified item.</li>

<li><b>pop():</b> Removes and returns the item at a specified index.</li>

<li><b>index():</b> Returns the index of the first occurrence of a specified item.</li>

<li><b>sort():</b> Sorts the list in ascending order.</li>

<li><b>reverse():</b> Reverses the order of the elements in the list.</li>
  
  <h2>Using Lists as Stacks and Queues</h2>
  <p>Lists can be used as <b>stacks</b> (Last-In, First-Out) and <b>queues</b> (First-In, First-Out). To use a list as a stack, you can use the <i>append()</i> method to add elements to the end of the list, and the <i>pop()</i> method to remove elements from the end. To use a list as a queue, you can use the <i>append()</i> method to add elements to the end of the list, and the <i>pop(0)</i> method to remove elements from the beginning.
</p>

<h2>List Comprehensions</h2>
<p>
They allow to build and generate lists in a concise way f<></>rom an expression and a control structure.
</p>
<h5>Syntax:</h5>
<pre>
new_list = [expression <b>for</b> element <b>in</b> original_list <b>if</b> condition]
</pre>
<p>
Where:

<li><b>expression</b> is the expression that is evaluated and added to the new list.</i>

<li><b>element</b> is a temporary variable that takes the value of each element of the original_list while it is being traversed.</i>

<li><b>original_list</b> is the list from which the elements are taken.</i>

<li><b>condition (optional)</b> is a boolean expression that determines if the element is included in the new list.</i>

</p>
<h2>Tuples</h2>
Tuples are similar to lists, but they are immutable, meaning their contents cannot be modified after creation. Tuples are defined by enclosing comma-separated values within parentheses ( ).

<h3>When to Use Tuples vs Lists</h3>
tuples when you need an immutable collection of elements that won't change. Tuples are suitable for representing data that should remain constant, such as coordinates or database records. Lists, on the other hand, are preferred when you need to modify or extend the collection of elements.
