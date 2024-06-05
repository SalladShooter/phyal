from typing import Callable
from typing_extensions import Self # required for versions <3.11
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

class App:

    def __init__(self: Self) -> None:
        self.url_map: Map = Map()
        self.view_functions: dict = {}
        self.html_content: list = []

    def route(self, rule: str, **options) -> Callable:
        def decorator(function: Callable) -> Callable:
            self.url_map.add(Rule(rule, endpoint=function.__name__))
            self.view_functions[function.__name__] = function
            return function

        return decorator

    def dispatch_request(self, request: Request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return self.view_functions[endpoint](request, **values)
        except HTTPException as e:
            return e

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def run(self: Self, host:str='0.0.0.0', port:int=5000) -> None:
        app: SharedDataMiddleware = SharedDataMiddleware(self, {'/static': 'static'})
        run_simple(host, port, app)

    def reload_content(self, new_content: list[str]):
        self.html_content = new_content

# Copyright (c) 2024 SalladShooter

class Tag:

    def __init__(self, name: str, text:str='') -> None:
        self.name: str = name
        self.attributes: dict[str, str] = {}
        self.children: list[Tag] = []
        self.text: str = text

    def attribute(self, key: str, value: str) -> Self:
        self.attributes[key] = value
        return self

    def id(self, value: str) -> Self:
        self.attributes['id'] = value
        return self

    def add_children(self, *tags: Self) -> Self:
        self.children.extend(tags)
        return self

    def __str__(self) -> str:
        attrs: str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        children: str = ''.join(map(str, self.children))
        return f'<{self.name} {attrs}>{self.text}{children}</{self.name}>'

class Tags:

    class div(Tag):
        def __init__(self, text='') -> None:
            super().__init__('div', text)

    class address(Tag):
        def __init__(self, text='') -> None:
            super().__init__('address', text)


    class article(Tag):
        def __init__(self, text='') -> None:
            super().__init__('article', text)

    class aside(Tag):
        def __init__(self, text='') -> None:
            super().__init__('aside', text)

    class footer(Tag):
        def __init__(self, text='') -> None:
            super().__init__('footer', text)

    class header(Tag):
        def __init__(self, text='') -> None:
            super().__init__('header', text)

    class hgroup(Tag):
        def __init__(self, text='') -> None:
            super().__init__('hgroup', text)

    class main(Tag):
        def __init__(self, text='') -> None:
            super().__init__('main', text)

    class section(Tag):
        def __init__(self, text='') -> None:
            super().__init__('section', text)

    class search(Tag):
        def __init__(self, text='') -> None:
            super().__init__('search', text)

    class figure(Tag):
        def __init__(self, text='') -> None:
            super().__init__('figure', text)

    class blockquote(Tag):
        def __init__(self, text='', cite='') -> None:
            super().__init__('blockquote', text)
            self.attribute('cite', cite)

    class p(Tag):
        def __init__(self, text='') -> None:
            super().__init__('p', text)

    class h1(Tag):
        def __init__(self, text='') -> None:
            super().__init__('h1', text)

    class h2(Tag):
        def __init__(self, text='') -> None:
            super().__init__('h2', text)

    class h3(Tag):
        def __init__(self, text='') -> None:
            super().__init__('h3', text)

    class h4(Tag):
        def __init__(self, text='') -> None:
            super().__init__('h4', text)

    class h5(Tag):
        def __init__(self, text='') -> None:
            super().__init__('h5', text)

    class h6(Tag):
        def __init__(self, text='') -> None:
            super().__init__('h6', text)

    class span(Tag):
        def __init__(self, text='') -> None:
            super().__init__('span', text)

    class dd(Tag):
        def __init__(self, text='') -> None:
            super().__init__('dd', text)

    class dl(Tag):
        def __init__(self, text='') -> None:
            super().__init__('dl', text)

    class dt(Tag):
        def __init__(self, text='') -> None:
            super().__init__('dt', text)

    class figcaption(Tag):
        def __init__(self, text='') -> None:
            super().__init__('figcaption', text)

    class hr(Tag):
        def __init__(self, text='') -> None:
            super().__init__('hr', text)

    class menu(Tag):
        def __init__(self, text='') -> None:
            super().__init__('menu', text)

    class ol(Tag):
        def __init__(self, text='') -> None:
            super().__init__('ol', text)

    class pre(Tag):
        def __init__(self, text='') -> None:
            super().__init__('pre', text)

    class ul(Tag):
        def __init__(self, text='') -> None:
            super().__init__('ul', text)

    class li(Tag):
        def __init__(self, text='') -> None:
            super().__init__('li', text)

    class a(Tag):
        def __init__(self, text='', href='#') -> None:
            super().__init__('a', text)
            self.attribute('href', href)

    class img(Tag):
        def __init__(self, src='', alt='') -> None:
            super().__init__('img')
            self.attribute('src', src)
            self.attribute('alt', alt)

    class table(Tag):
        def __init__(self, text='') -> None:
            super().__init__('table', text)

    class tr(Tag):
        def __init__(self, text='') -> None:
            super().__init__('tr', text)

    class th(Tag):
        def __init__(self, text='') -> None:
            super().__init__('th', text)

    class td(Tag):
        def __init__(self, text='') -> None:
            super().__init__('td', text)

    class form(Tag):
        def __init__(self, text='') -> None:
            super().__init__('form', text)

    class input(Tag):
        def __init__(self, type='', value='') -> None:
            super().__init__('input')
            self.attribute('type', type)
            self.attribute('value', value)

    class button(Tag):
        def __init__(self, text='') -> None:
            super().__init__('button', text)
