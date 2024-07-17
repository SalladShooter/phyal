# phyal

**Quickly build websites without the hassle of HTML**

phyal was born out of a problem, like many good opensource startups alike. phyal was made to solve an issue I had encountered with people I knew and others online of the struggle of learning and implementing HTML. Many of them had already known another language such as Python and JavaScript. Since I was most comfortable with Python, and many new frontend learners would already have encountered Python previously (and if not, Python has a simple syntax), I started seeking help from others who had created frameworks and got to work. As I worked and wrote code, phyal's presense grew with it.

When the planning and begining's of the larget phyal update that I had worked on so far (0.3.0), other fans of phyal jumped into help. They gave suggestions, pull requests, and more, making my job so much easier so I could get the update out in a timely manor without burnout.

This journey led me in a direction I never thought I would take. It was challenging, but rewarding, with new knowledge and experience. phyal has allowed me to grow as a programmer, and in the future probably much more. So I hope you enjoy working with phyal as much as I did working on it.

- SalladShooter Owner and Maintainer

# 🙂 Get Started

### ⬇️ Installation

Get started with phyal in less than a minute by first using `pip install phyal` in your Shell. And by adding `import phyal` in your Python file. It‘s as easy as that.

### 📐 File Setup

**Quickly setup your main Python file with these steps**

- First a route needs to be defined, it can be simple like this, or contain multiple routes to access multiple pages.
```py
app = App()
​
@app.route('/')
def index(request):
You can easily add your CSS and JavaScript with just a few lines.
css_link = Tags.link().attr('href', '/static/style.css').attr('rel', 'stylesheet')
js_script = Tags.script().attr('src', '/static/script.js')
​
html_content = str()
```
- Inside of route still add a few lines to send your Python code to phyal to render it out into something visible.
```py
app.reload_content([html_content])
return Response(html_content, content_type='text/html')
```
- Outside of your route a run function needs to be put in place.
```py
if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
```
Now you have completed the `🙂 Get Started` section, and you can proceed to learn the simple syntax of phyal.

### ✍️ Syntax

**Quickly learn the simple phyal syntax to get started right away**

phyal components go hand in hand with HTML elements but are written in the Python programming language. Here’s a quickstart guide to the phyal syntax.

- You can use an element by setting up an advised html_content variable ->
```py
html_content = str(
    Tags.#element
)
```
- You can then add your element to the line, for example the paragraph element or <p> ->
```py
Tags.p('Hello, world!')
```
> The first set of parentheses on all elements is for text (if it is used withen HTML, think `<a>` tags, or `<h1>` tags, etc.)

- Then you can add attributes, things like HREF's SRC's ALT's would fall in this category. You would add .attribute(# attribute()) to your line, for example an <a> tag ->
```py
Tags.a('Link').attr('href', 'https://google.com')
```
- You can add ID's like so .id('') (such as uses in JavaScript in CSS), for example with a <p> tag ->
```py
Tags.p('Hello, world!').id('my_id')
```
- You can also add children to the elements in a hireachy system like HTML like so .add_children(Tags.) # Element, for example a <p> tag ->
```py
Tags.div().id('container').child(
    Tags.h1('Title').id('title'),
    # Add more children here if needed
)
```
Now that you have mastered the phyal syntax you should be able to use phyal to it‘s largest potential, if you come across any errors make sure to create an issue [here](https://github.com/SalladShooter/phyal/issues).
