<h1 align = "center">Python-input_output</h1>

<h2>Project objectives</h2>

<li>Why Python programming is awesome</li>
<li>How to open a file</li>
<li>How to write text in a file</li>
<li>How to read the full content of a file</li>
<li>How to read a file line by line</li>
<li>How to move the cursor in a file</li>
<li>How to make sure a file is closed after using it</li>
<li>What is and how to use the with statement</li>
<li>What is JSON</li>
<li>What is serialization</li>
<li>What is deserialization</li>
<li>How to convert a Python data structure to a JSON string</li>
<li>How to convert a JSON string to a Python data structure</li>
<li>How to access command line parameters in a Python script</li>

<h2>what is JSON</h2>
<p>
  The JSON format is based on two main data structures: objects and arrays. A JSON object is an unordered collection of key-value pairs, where the keys are strings and the values can be of any valid JSON data type (strings, numbers, Booleans, nested JSON objects, JSON arrays, or null). A JSON array is an ordered list of JSON values.
</p>

<h3>json.dumps()</h3>
<p>This function is used to convert a Python object to a JSON string. It takes the object to be converted as an argument and returns a JSON string.</p>

<h5>Example</h5>
<pre>
  import json

  data = {
    "name": "John",
    "age": "30",
    "city": "Mexico"
}
json_data = json.dumps(data)
print(json_data)

<i>Output: { "name": "Juan", "age": 30, "city": "Mexico" } </i>
</pre>

<h3>json.loads()</h3>
<p>
  This function is used to convert a JSON string into a Python object. It takes as an argument the JSON string you want to convert and returns an object
</p>

<pre>
  import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

python_data = json.loads(json_string)
print(python_data["name"])
print(python_data["age"])
print(python_data["city"])

<i>Output: John
        30
        New York</i>
</pre>
