# phyal

Quickly build websites without the hassle of HTML
___

phyal is easily used with the template, otherwise it requires some setup.

So first you have to import the necessary files ->

```py
import phyal
```
and in the shell
```shell script
pip install phyal
```

Then you will have to define a route/source, for example ->
```py
app = App()

@app.route('/')
def index(request):
```

and now you can add links to other files like `JavaScript` and `CSS` ->
```py
css_link = Tags.link().attr('href', '/static/style.css').attr('rel', 'stylesheet')
js_script = Tags.script().attr('src', '/static/script.js')

html_content = str()
```

Outside of your route you need to allow the file to be ran ->
```py
if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
```

Now you can code away using phyal in your route.

___

### Syntax

phyal components go hand in hand with HTML elements but are written in the Python programming language.

You can use an element by setting up an advised `html_content` list ->
```py
html_content = str(
    Tags.#element
)
```

you can then add your element (currently select few, but most/all elements will be added eventually) to the line, for example the paragraph element or `<p>` ->
```py
Tags.p('Hello, world!')
```


> The first set of parentheses on all elements is for text (if it is used withen HTML, think `<a>` tags, or `<h1>` tags, etc.)


Then you can add `attributes`, things like `HREF`'s `SRC`'s `ALT`'s would fall in this category. You would add `.attribute(# attribute())` to your line, for example an `<a>` tag ->
```py
Tags.a('Link').attr('href', 'https://google.com')
```

You can use the phyal framework along side things like `JavaScript` and `CSS` and add ID's like so `.id('')`, for example with a `<p>` tag ->
```py
Tags.p('Hello, world!').id('my_id')
```

You can also add children to the elements in a hireachy system like HTML like so `.add_children(Tags.) # Element`, for example a `<p>` tag ->
```py
Tags.div().id('container').child(
    Tags.h1('Title').id('title'),
    # Add more children here if needed
)
```

___

### Running

Once you have written out your code with phyal you can use it along side JavaScript with some simple scripting or just run your code.

```py
app.reload_content([html_content])
return Response(html_content, content_type='text/html')
```
___

# Contributors

Thank you so much to those that have contributed, you have been a big help in this process!