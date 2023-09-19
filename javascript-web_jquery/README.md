<h1 align = "center">Javascript-web_jquery</h1>

<h2>Project objectives</h2>

<li>How to select HTML elements with JQuery</li>
<li>What are differences between ID, class and tag name selectors</li>
<li>How to modify an HTML element style</li>
<li>How to get and update an HTML element content</li>
<li>How to modify the DOM</li>
<li>How to make a GET request with JQuery Ajax</li>
<li>How to make a POST request with JQuery Ajax</li>
<li>How to listen/bind to DOM events</li>
<li>How to listen/bind to user events</li>

<h2>What is jQuery?</h2>

<p>jQuery is a fast, small, and feature-rich JavaScript library. Things like iterating and editing HTML documents, event handling, animations, and Ajax are made easier with an easy-to-use API that runs on a variety of browsers. Versatility and scalabilit</p>

<h3>Select HTML Elements with jQuery</h3>

<p>To select HTML elements with jQuery, use the $() function </p>
<h4>Example</h4>
<pre>
  <code>
    $('header').css('color', '#FF0000')
  </code>
</pre>

<h3>Differences Between ID, Class, and Tag Name Selectors</h3>
<p><b>ID:</b> Selects a single element by its unique ID. IDs must be unique on the page.
<b>Class:</b> Selects all elements with a specific class. Multiple elements can share the same class.
<b>Tag Name:</b> Selects all elements that match the specified tag.</div>

<h3>GET request with JQuery Ajax</h3>
<p>the <b>$.get()</b> method is used to make HTTP GET requests to a server and retrieve data from the server.</p>

<h4>Example</h4>
<pre>
  <code>
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
})
  </code>
</pre>
