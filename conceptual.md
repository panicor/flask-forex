### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  JS uses brackets to define the body of functions/methods, while Python relies on indentation. Also, Python is a little more high level than JS. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  get(key, def_value)
  setdefault(key, def_value)

- What is a unit test?

  A test written to test a single unit of functionality. It helps create modular code. 

- What is an integration test?

  A test written to test that components work together. 

- What is the role of web application framework, like Flask?

  It helps define which requests to respond to and how to respond to them. They can handle forms and cookies, for example.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  The URL paramete is the subject of the page, while the query param is extra information (often coming from a form).

- How do you collect data from a URL placeholder parameter using Flask?

  `<variable_name>` in @app.route

- How do you collect data from the query string using Flask?

  request.args.get("variable_name")

- How do you collect data from the body of the request using Flask?

  request.form

- What is a cookie and what kinds of things are they commonly used for?

  A cookie is a name/string-value pair stored by the client. They are commonly used to save state. 

- What is the session object in Flask?

  The session object contains information for the current browser. It preserves type and are "signed" so users cannot modify data. 

- What does Flask's `jsonify()` do?

  Turns JSON into a response object with the application/json mimetype. 
