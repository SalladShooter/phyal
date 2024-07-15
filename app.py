from src.framework import App, Response, Tags

app = App()

@app.route('/')
def index(request):
    css_link = Tags.link().attr('href', '/static/style.css').attr('rel', 'stylesheet')
    js_script = Tags.script().attr('src', '/static/script.js')

    html_content = str(Tags.div().id('container').child(
        Tags.h1('Trees').id('title'),
        Tags.img().attr('src', 'imgs/tree.png').attr('alt', 'image of a tree').id('tree'),
        Tags.p('A woody plant, usually having a single stem or trunk growing to be tall and has lateral branches at some distance from the ground.').id('description')
    ))

    app.reload_content([html_content])
    return Response(html_content, content_type='text/html')

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
