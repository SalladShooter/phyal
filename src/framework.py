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

    def route(self: Self, rule: str, **options) -> Callable:
        def decorator(function: Callable) -> Callable:
            self.url_map.add(Rule(rule, endpoint=function.__name__))
            self.view_functions[function.__name__] = function
            return function

        return decorator

    def dispatch_request(self: Self, request: Request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return self.view_functions[endpoint](request, **values)
        except HTTPException as e:
            return e

    def __call__(self: Self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def run(self: Self, host:str='0.0.0.0', port:int=5000) -> None:
        app: SharedDataMiddleware = SharedDataMiddleware(self, {'/static': 'static'})
        run_simple(host, port, app)

    def reload_content(self: Self, new_content: list[str]):
        self.html_content = new_content

# Copyright (c) 2024 SalladShooter

class Tag:

    def __init__(self: Self, name: str, text:str='', **attributes: str) -> None:
        self.name: str = name
        self.attributes: dict[str, str] = attributes

        self.children: list[Tag] = []
        self.text: str = text

    def attribute(self: Self, key: str, value: str) -> Self:
        self.attributes[key] = value
        return self

    def id(self: Self, value: str) -> Self:
        self.attributes['id'] = value
        return self

    def add_children(self: Self, *tags: Self) -> Self:
        self.children.extend(tags)
        return self

    def __str__(self: Self) -> str:
        attrs: str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        children: str = ''.join(map(str, self.children))
        return f'<{self.name} {attrs}>{self.text}{children}</{self.name}>'

class Tags:

    # Document metadata

    class link(Tag):
        def __init__(self: Self, href:str='', rel:str='') -> None:
            super().__init__('link')
            self.attribute('href', href)
            self.attribute('rel', rel)
    
    class meta(Tag):
        def __init__(self: Self, text:str='', name:str='', httpequiv:str='', charset:str='', itemprop:str='') -> None:
            super().__init__('meta', text)
            self.attribute('name', name)
            self.attribute('http-equiv', httpequiv)
            self.attribute('charset', charset)
            self.attribute('itemprop', itemprop)
            
    class style(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('style', text)

    # Sectioning root
            
    class body(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('body', text)

    # Content sectioning

    class address(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('address', text)

    class article(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('article', text)

    class aside(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('aside', text)

    class footer(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('footer', text)

    class header(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('header', text)

    class h1(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('h1', text)

    class h2(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('h2', text)

    class h3(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('h3', text)

    class h4(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('h4', text)

    class h5(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('h5', text)

    class h6(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('h6', text)

    class hgroup(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('hgroup', text)

    class main(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('main', text)

    class nav(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('nav', text)

    class section(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('section', text)

    class search(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('search', text)

    # Text content

    class blockquote(Tag):
        def __init__(self: Self, text:str='', cite:str='') -> None:
            super().__init__('blockquote', text)
            self: Self.attribute('cite', cite)

    class dd(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('dd', text)
    
    class div(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('div', text)

    class dl(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('dl', text)

    class dt(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('dt', text)

    class figcaption(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('figcaption', text)

    class figure(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('figure', text)
    
    class hr(Tag):
        def __init__(self: Self) -> None:
            super().__init__('hr')

    class li(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('li', text)

    class menu(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('menu', text)

    class ol(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('ol', text)

    class p(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('p', text)

    class pre(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('pre', text)

    class ul(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('ul', text)
    
    # Inline text semantics

    class a(Tag):
        def __init__(self: Self, text:str='', href:str='#') -> None:
            super().__init__('a', text)
            self.attribute('href', href)
    
    class abbr(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('abbr', text)
    
    class b(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('b', text)
    
    class bdi(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('bdi', text)
    
    class bdo(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('bdo', text)
    
    class br(Tag):
        def __init__(self: Self) -> None:
            super().__init__('br')
    
    class cite(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('div', text)
    
    class code(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('div', text)
    
    class data(Tag):
        def __init__(self: Self, text:str='', value:str='') -> None:
            super().__init__('div', text)
            self.attribute('value', value)
    
    class dfn(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('dfn', text)
    
    class em(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('em', text)
    
    class i(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('i', text)
    
    class kbd(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('kbd', text)
    
    class mark(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('mark', text)
    
    class q(Tag):
        def __init__(self: Self, text:str='', cite:str='') -> None:
            super().__init__('q', text)
            self.attribtute('cite', cite)

    class span(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('span', text)

    class img(Tag):
        def __init__(self: Self, src:str='', alt:str='') -> None:
            super().__init__('img')
            self.attribute('src', src)
            self.attribute('alt', alt)

    class table(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('table', text)

    class tr(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('tr', text)

    class th(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('th', text)

    class td(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('td', text)

    class form(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('form', text)

    class input(Tag):
        def __init__(self: Self, type:str='', value:str='') -> None:
            super().__init__('input')
            self.attribute('type', type)
            self.attribute('value', value)

    class button(Tag):
        def __init__(self: Self, text:str='') -> None:
            super().__init__('button', text)
