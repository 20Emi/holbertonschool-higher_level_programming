<h1 align = "center">Python-exception</h1>

<h2>Project objectives</h2>
<li>Why Python programming is awesome</li>

<li>What’s the difference between errors and exceptions</li>

<li>What are exceptions and how to use them</li>

<li>When do we need to use exceptions</li>

<li>How to correctly handle an exception</li>

<li>What’s the purpose of catching exceptions</li>

<li>How to raise a builtin exception</li>

<li>When do we need to implement a clean-up action after an exception</li>
<h2>prototype of the functions</h2>

<table>
  <tr>
    <td>File</td>
    <td>Prototype</td>
  </tr>
  <tr>

  <td>0-safe_print_list.py </td>

   <td>def safe_print_division(a, b):</td>

</tr><tr>

   <td>1-safe_print_integer.py</td>

   <td>def safe_print_integer(value)</td>

</tr><tr>

   <td>2-safe_print_list_integers.py</td>

   <td>def safe_print_list_integers(my_list=[], x=0):</td>

</tr><tr>

   <td>3-safe_print_division.py</td>

   <td>def safe_print_division(a, b):</td>

</tr><tr>

   <td>4-list_division.py</td>

   <td>def list_division(my_list_1, my_list_2, list_length):</td>

</tr><tr>

   <td>5-raise_exception.py</td>

   <td>def raise_exception():</td>

</tr><tr>

   <td>6-raise_exception_msg.py</td>

   <td>def raise_exception_msg(message=""):</td>

</tr>
</table>
<h2>Difference between errors and exceptions</h2>
<li><b>Errors</b> refer to any abnormal situations or conditions that prevent a program from executing successfully. They can occur due to syntax mistakes (syntax errors) or logical flaws (runtime errors). Errors typically cause the program to halt and display an error message.</li>

<li><b>Exceptions</b> on the other hand, are events that occur during program execution and disrupt the normal flow. They are a mechanism in Python to handle errors or exceptional situations gracefully. When an exception is raised, it can be caught and processed, allowing the program to respond to the error and continue execution, if desired.</li>
