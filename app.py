from src.framework import App, Response, Tag, Tags

app = App()

@app.route('/')
def index(request):
    css_link = '<link rel="stylesheet" type="text/css" href="/static/style.css">'
    js_link = '<script src="/static/script.js"></script>'

    html_content = [
        css_link, js_link,
        str(Tag('p', 'Hello World'))
    ]
    
    while True:
        app.reload_content(html_content)
        return Response(html_content, content_type='text/html')

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)