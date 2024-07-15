from typing import Callable
from typing_extensions import Self # required for versions <3.11
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

class App:
    def __init__(self:Self) -> None:
        self.url_map:Map = Map()
        self.view_functions:dict = {}
        self.html_content:list[str] = []

    def route(self:Self, rule:str, **options) -> Callable:
        def decorator(function:Callable) -> Callable:
            self.url_map.add(Rule(rule, endpoint=function.__name__))
            self.view_functions[function.__name__] = function
            return function

        return decorator

    def dispatch_request(self:Self, request:Request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return self.view_functions[endpoint](request, **values)
        except HTTPException as e:
            return e

    def run(self:Self, host:str='0.0.0.0', port:int=5000) -> None:
        app:SharedDataMiddleware = SharedDataMiddleware(self, {'/static':'static'})
        run_simple(host, port, app)

    def reload_content(self:Self, new_content:list[str]):
        self.html_content = new_content

    def __call__(self:Self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

class Tag:
    def __init__(self: Self, name: str, text: str = '') -> None:
        self.name = name
        self.text = text
        self.attributes = {}

    def attr(self: Self, key: str, value: str) -> Self:
        if value:
            self.attributes[key] = value
        return self

    def id(self: Self, id_name: str) -> Self:
        self.attributes['id'] = id_name
        return self

    def child(self: Self, *children: Self) -> Self:
        self.children = children
        return self

    def __str__(self: Self) -> str:
        attrs = ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())
        if self.text:
            return f'<{self.name} {attrs}>{self.text}</{self.name}>'
        else:
            children_str = ''.join(str(child) for child in self.children) if hasattr(self, 'children') else ''
            return f'<{self.name} {attrs}>{children_str}</{self.name}>'

class Tags:

    # Document metadata
    
    class base(Tag):
        pass
    
    class head(Tag):
        pass
    
    class link(Tag):
        def __init__(self: Self, href: str = '', rel: str = '') -> None:
            super().__init__('link')
            self.attr('href', href)
            self.attr('rel', rel)
    
    class meta(Tag):
        def __init__(self: Self, text: str = '', name: str = '', httpequiv: str = '', charset: str = '', itemprop: str = '') -> None:
            super().__init__('meta', text)
            self.attr('name', name)
            self.attr('http-equiv', httpequiv)
            self.attr('charset', charset)
            self.attr('itemprop', itemprop)
    
    class style(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('style', text)
    
    class title(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('title', text)
    
    
    # Sectioning root
    
    class body(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('body', text)
    
    # Content sectioning
    
    class address(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('address', text)
    
    class article(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('article', text)
    
    class aside(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('aside', text)
    
    class footer(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('footer', text)
    
    class header(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('header', text)
    
    class h1(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('h1', text)
    
    class h2(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('h2', text)
    
    class h3(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('h3', text)
    
    class h4(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('h4', text)
    
    class h5(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('h5', text)
    
    class h6(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('h6', text)
    
    class hgroup(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('hgroup', text)
    
    class main(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('main', text)
    
    class nav(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('nav', text)
    
    class section(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('section', text)
    
    class search(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('search', text)
    
    # Text content
    
    class blockquote(Tag):
        def __init__(self: Self, text: str = '', cite: str = '') -> None:
            super().__init__('blockquote', text)
            self.attr('cite', cite)
    
    class dd(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('dd', text)
    
    class div(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('div', text)
    
    class dl(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('dl', text)
    
    class dt(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('dt', text)
    
    class figcaption(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('figcaption', text)
    
    class figure(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('figure', text)
    
    class hr(Tag):
        def __init__(self: Self) -> None:
            super().__init__('hr')
    
    class li(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('li', text)
    
    class menu(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('menu', text)
    
    class ol(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('ol', text)
    
    class p(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('p', text)
    
    class pre(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('pre', text)
    
    class ul(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('ul', text)
    
    # Inline text semantics
    
    class a(Tag):
        def __init__(self: Self, text: str = '', href: str = '#') -> None:
            super().__init__('a', text)
            self.attr('href', href)
    
    class abbr(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('abbr', text)
    
    class b(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('b', text)
    
    class bdi(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('bdi', text)
    
    class bdo(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('bdo', text)
    
    class br(Tag):
        def __init__(self: Self) -> None:
            super().__init__('br')
    
    class cite(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('cite', text)
    
    class code(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('code', text)
    
    class data(Tag):
        def __init__(self: Self, text: str = '', value: str = '') -> None:
            super().__init__('data', text)
            self.attr('value', value)
    
    class dfn(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('dfn', text)
    
    class em(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('em', text)
    
    class i(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('i', text)
    
    class kbd(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('kbd', text)
    
    class mark(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('mark', text)
    
    class q(Tag):
        def __init__(self: Self, text: str = '', cite: str = '') -> None:
            super().__init__('q', text)
            self.attr('cite', cite)
    
    class rp(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('rp', text)
    
    class rt(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('rt', text)
    
    class ruby(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('ruby', text)
    
    class s(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('s', text)
    
    class samp(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('samp', text)
    
    class small(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('small', text)
    
    class span(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('span', text)
    
    class strong(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('strong', text)
    
    class sub(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('sub', text)
    
    class sup(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('sup', text)
    
    class time(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('time', text)
    
    class u(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('u', text)
    
    class var(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('var', text)
    
    class wbr(Tag):
        def __init__(self: Self) -> None:
            super().__init__('wbr')
    
    # Image and multimedia
    
    class area(Tag):
        def __init__(self: Self, alt: str = '', coords: str = '', download: str = '', href: str = '', hreflang: str = '', ping: str = '', referrerpolicy: str = '', rel: str = '', shape: str = '', target: str = '') -> None:
            super().__init__('area')
            self.attr('alt', alt)
            self.attr('coords', coords)
            self.attr('download', download)
            self.attr('href', href)
            self.attr('hreflang', hreflang)
            self.attr('ping', ping)
            self.attr('referrerpolicy', referrerpolicy)
            self.attr('rel', rel)
            self.attr('shape', shape)
            self.attr('target', target)
    
    class audio(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('audio', text)
    
    class img(Tag):
        def __init__(self: Self, alt: str = '', src: str = '', srcset: str = '') -> None:
            super().__init__('img')
            self.attr('alt', alt)
            self.attr('src', src)
            self.attr('srcset', srcset)
    
    class map(Tag):
        def __init__(self: Self, text: str = '', name: str = '') -> None:
            super().__init__('map', text)
            self.attr('name', name)
    
    class track(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('track', text)
    
    class video(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('video', text)
    
    # Embedded content
    
    class embed(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('embed', text)
    
    class iframe(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('iframe', text)
    
    class object(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('object', text)
    
    class param(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('param', text)
    
    class picture(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('picture', text)
    
    class source(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('source', text)
    
    # Scripting
    
    class canvas(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('canvas', text)
    
    class noscript(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('noscript', text)
    
    class script(Tag):
        def __init__(self: Self, text: str = '', src: str = '') -> None:
            super().__init__('script', text)
            self.attr('src', src)
    
    # Demarcating edits
    
    class del_(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('del', text)
    
    class ins(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('ins', text)
    
    # Table content
    
    class caption(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('caption', text)
    
    class col(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('col', text)
    
    class colgroup(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('colgroup', text)
    
    class table(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('table', text)
    
    class tbody(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('tbody', text)
    
    class td(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('td', text)
    
    class tfoot(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('tfoot', text)
    
    class th(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('th', text)
    
    class thead(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('thead', text)
    
    class tr(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('tr', text)
    
    # Forms
    
    class button(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('button', text)
    
    class datalist(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('datalist', text)
    
    class fieldset(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('fieldset', text)
    
    class form(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('form', text)
    
    class input(Tag):
        def __init__(self: Self, value: str = '', placeholder: str = '') -> None:
            super().__init__('input')
            self.attr('value', value)
            self.attr('placeholder', placeholder)
    
    class label(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('label', text)
    
    class legend(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('legend', text)
    
    class meter(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('meter', text)
    
    class optgroup(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('optgroup', text)
    
    class option(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('option', text)
    
    class output(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('output', text)
    
    class progress(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('progress', text)
    
    class select(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('select', text)
    
    class textarea(Tag):
        def __init__(self: Self, text: str = '') -> None:
            super().__init__('textarea', text)
    