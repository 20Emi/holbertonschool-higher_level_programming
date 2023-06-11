<h1 align = "center"> Python-more_data_structures</h1>

<h2>Project objectives</h2>

<li>Why Python programming is awesome</li>
<li>What are sets and how to use them</li>
<li>What are the most common methods of set and how to use them</li>
<li>When to use sets versus lists</li>
<li>How to iterate into a set</li>
<li>What are dictionaries and how to use them</li>
<li>When to use dictionaries versus lists or sets</li>
<li>What is a key in a dictionary</li>
<li>How to iterate over a dictionary</li>
<li>What is a lambda function</li>
<li>What are the map, reduce and filter functions</li>

<h2>prototype of the functions</h2>
<table>
   <tr>

   <td align = "center"><b>File</b></td>

   <td align = "center"><b>Prototype</b></td>

</tr>
<tr>
   <td>0-square_matrix_simple.py</td>
   <td>def square_matrix_simple(matrix=[]):</td>
</tr>
   
   <tr>
   <td>1-search_replace.py</td>
   <td>def search_replace(my_list, search, replace):</td>
</tr>
   
   <tr>
   <td>2-uniq_add.py</td>
   <td>def uniq_add(my_list=[]):</td>
</tr>
   
   <tr>
   <td>3-common_elements.py</td>
   <td>def common_elements(set_1, set_2):</td>
</tr>
   
   <tr>
   <td>4-only_diff_elements.py</td>
   <td>def only_diff_elements(set_1, set_2):</td>
</tr>
   
   <tr>
   <td>5-number_keys.py</td>
   <td>def number_keys(a_dictionary):</td>
</tr>
   
   <tr>
   <td>6-print_sorted_dictionary.py</td>
   <td>def print_sorted_dictionary(a_dictionary):</td>
</tr>
   
   <tr>
   <td>7-update_dictionary.py</td>
   <td>def update_dictionary(a_dictionary, key, value):</td>
</tr>
   
   <tr>
   <td>8-simple_delete.py</td>
   <td>def simple_delete(a_dictionary, key=""):</td>
</tr>
   
   <tr>
   <td>9-multiply_by_2.py</td>
   <td>def multiply_by_2(a_dictionary):</td>
</tr>
   
   <tr>
   <td>10-best_score.py</td>
   <td>def best_score(a_dictionary):</td>
</tr>
   
   <tr>
   <td>11-multiply_list_map.py</td>
   <td>def multiply_list_map(my_list=[], number=0):</td>
</tr>
   
   <tr>
   <td>12-roman_to_int.py</td>
   <td>def roman_to_int(roman_string):</td>
</tr>
  </table>
  <h2>Sets</h2>
  <p>
  A data structure that stores a collection of unique, unordered elements. It is an implementation of set theory in mathematics. Sets are defined using braces ({}) or using the set() constructor.

The main characteristic of a set is that it does not allow duplicate elements. If you try to add an element that is already present in the set, it will not be added back.
</p>
<h4>Characteristics</h4>
<li><b>They have no specific order:</b> The elements in a set have no defined order, which means that you cannot access them by means of an index.</li>

<li><b>They support mathematical set operations:</b> Sets in Python support operations such as union, intersection, difference, and symmetric difference, which can be used to combine or compare sets</li>

<li><b>They are mutable: </b>You can add or remove elements of a set after you have created it.</li>

<li><b>They can only contain immutable elements:</b> Elements within a set must be immutable, such as strings, numbers or tuples. You cannot have sets, lists or other sets within a set.</li>

<h5>Example</h5>

<li>Add elements to a set:</li>
<pre>
set.add(element)
</pre>
o
<pre>
set.update([element1, element2, element3])
</pre>
<li>Remove elements from a set:</li>
<pre>
set.remove(element)
</pre>
<b>remove()</b> will throw an error if the element does not exist in the set.
<pre>
set.discard(element)
</pre>
<b>discard()</b> will remove the element if it exists in the set, but will not throw an error if the element does not exist.
<pre>
element = set.pop()
</pre>
<b>pop()</b> will remove and return a random element from the set.

<h2>Dictionaries</h2>

It is a data structure that stores pairs of elements, where each pair consists of a key and an associated value.

Dictionaries are indexed by unique keys. Keys can be of any immutable type, such as strings, numbers, or tuples. Values can be of any object type.

Dictionaries are useful when you need to store and access data efficiently through a key. You can add, modify and delete items in a dictionary, and you can also look up values associated with a specific key.

<h5>Example</h5>
<pre>
<i># Create an empty dictionary</i>
dictionary = {}

<i># Add items to the dictionary</i>
dictionary["key1"] = "value1".
dictionary["key2"] = "value2"

<i># Access a value by its key</i>
print(dictionary["key1"]) <i># Print "value1" # Print "value2"</i>

<i># Modify an existing value</i>
dictionary["key2"] = "new_value"

<i># Delete a dictionary element</i>
from dictionary["key1"]

<i># Check if a key exists in the dictionary</i>
if "key1" in dictionary:
    print("Key exists")

<i># Get the list of all the keys in the dictionary</i>
keys = dictionary.keys()

<i># Get the list of all the values in the dictionary</i>
values = dictionary.values()

<i># Get the list of key-value pairs as tuples</i>
items = dictionary.items()
</pre>

<h2>Lambda</h2>
A keyword used to create anonymous functions or single-expression functions. A lambda function is a small, anonymous function that can take any number of arguments, but can only have one expression.

<h4>Sintaxis</h4>
<pre>
<b>lambda</b> arguments: expression
</pre>

<h5>Example</h5>
<pre>
sum = <b>lambda</b> x, y: x + y
result = sum(3, 5)
print(result)  

<i>#Output: 8</i>
</pre>

<h2>Map</h2>

It is a higher-order function that takes a function and one or more sequences as arguments. It then applies the function to each element of the sequences and returns an iterable containing the results.

<h4>Sintaxis</h4>
<pre>
<b>map</b>(function, sequence1, sequence2, ...)
</pre>

<h5>Example</h5>
<pre>
numbers = [1, 2, 3, 3, 4, 5].
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

<i># Output: [1, 4, 9, 9, 16, 25].</i>
</pre>

<h2>Filter</h2>
A higher-order function that takes a function and a sequence as arguments. The <b>filter()</b> function applies the function to each element of the sequence and returns an iterable containing only the elements for which the function returns <b>True.</b>

<h4>Sintaxis</h4>
<pre>
filter(function, sequence)
</pre>

<h5>Example</h5>
<pre>
numbers = [1, 2, 3, 3, 4, 5]
pairs = list(filter(lambda x: x % 2 == 0, numbers))
print(pairs) 
# Output: [2, 4]
</pre>

