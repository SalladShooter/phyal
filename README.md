# VIAL

[![Static Badge](https://img.shields.io/badge/Contributors-2-blue)](https://img.shields.io/badge/Contributor-2-4?style=flat&color=blue)

A simple to use Framework with a Python syntax that can replace HTML in a comfortable and easy way.

___

VIAL is easily used with the template, otherwise it requires some setup.

So first you have to import the necessary files ->

```py
from src.framework import App, Response
from src.html_generator import Tag, Tags
```

Then you will have to define a route/source, for example ->
```py
app = App()

@app.route('/')
def index(request):
```

and now you can add links to other files like `JavaScript` and `CSS` ->
```py
css_link = '<link rel="stylesheet" type="text/css" href="/static/style.css">'
js_link = '<script src="/static/script.js"></script>'

html_content = [
    css_link, js_link
]
```

Outside of your route you need to allow the file to be ran ->
```py
if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
```

Now you can code away using VIAL in your route.

___

### Syntax

VIAL components go hand in hand with HTML elements but are written in the Python programming language.

You can use an element by setting up an advised `html_content` list ->
```py
html_content = [
    css_link, js_link,
    str(Tag()) # Element
]
```

you can then add your element (currently select few, but most/all elements will be added eventually) to the line, for example the paragraph element or `<p>` ->
```py
str(Tag('p', 'Hello World'))
```


> The first set of parentheses on all elements is for text (if it is used withen HTML, think `<a>` tags, or `<h1>` tags, etc.)


Then you can add `attributes`, things like `HREF`'s `SRC`'s `ALT`'s would fall in this category. You would add `.attribute(# attribute())` to your line, for example an `<a>` tag ->
```py
str(Tag('a', 'Link', href='https://google.com'))
```

You can use the VIAL framework along side things like `JavaScript` and `CSS` and add ID's like so `.id('')`, for example with a `<p>` tag ->
```py
str(Tag('p', 'Hello World', id='my_id'))
```

You can also add children to the elements in a hireachy system like HTML like so `.add_children(Tags.) # Element`, for example a `<p>` tag ->
```py
str(Tag('p', 'Hello World', children=[
    Tag('div', children=[
        # Add more children here if needed
    ])
]))
```

___

### Running

Once you have written out your code with VIAL you can either write it where it runs once or runs continuously (harder on preformance, but works with JS better)

#### Single Use

```py
return Response(html_content, content_type='text/html')
```

#### Continuously

```py
while True:
    app.reload_content(html_content)
    return Response(html_content, content_type='text/html')
```
