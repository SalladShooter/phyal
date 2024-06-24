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

# Copyright (c) 2024 SalladShooter

class Tag:

    def __init__(self: Self, name: str, text:str='', **attributes:str) -> None:
        self.name: str = name
        self.attributes: dict[str, str] = attributes
        self.children: list[Tag] = []
        self.text: str = text

    def attr(self:Self, key:str, value:str) -> Self:
        self.attributes[key] = value
        return self

    def id(self:Self, value:str) -> Self:
        self.attributes['id'] = value
        return self

    def child(self:Self, *tags:Self) -> Self:
        self.children.extend(tags)
        return self

    def __str__(self:Self) -> str:
        attrs:str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        children:str = ''.join(map(str, self.children))
        return f'<{self.name} {attrs}>{self.text}{children}</{self.name}>'

class Tags:

    # Document metadata

    class base(Tag):
        pass

    class head(Tag):
        pass

    class link(Tag):
        def __init__(self:Self, href:str='', rel:str='') -> None: # More attributes required
            super().__init__('link')
            self.attr('href', href)
            self.attr('rel', rel)
    
    class meta(Tag):
        def __init__(self:Self, text:str='', name:str='', httpequiv:str='', charset:str='', itemprop:str='') -> None:
            super().__init__('meta', text)
            self.attr('name', name)
            self.attr('http-equiv', httpequiv)
            self.attr('charset', charset)
            self.attr('itemprop', itemprop)
            
    class style(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('style', text)

    class title(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('title', text)


    # Sectioning root
            
    class body(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('body', text)

    # Content sectioning

    class address(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('address', text)

    class article(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('article', text)

    class aside(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('aside', text)

    class footer(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('footer', text)

    class header(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('header', text)

    class h1(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('h1', text)

    class h2(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('h2', text)

    class h3(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('h3', text)

    class h4(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('h4', text)

    class h5(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('h5', text)

    class h6(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('h6', text)

    class hgroup(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('hgroup', text)

    class main(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('main', text)

    class nav(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('nav', text)

    class section(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('section', text)

    class search(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('search', text)

    # Text content

    class blockquote(Tag):
        def __init__(self:Self, text:str='', cite:str='') -> None:
            super().__init__('blockquote', text)
            self:self.attr('cite', cite)

    class dd(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('dd', text)
    
    class div(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('div', text)

    class dl(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('dl', text)

    class dt(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('dt', text)

    class figcaption(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('figcaption', text)

    class figure(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('figure', text)
    
    class hr(Tag):
        def __init__(self:Self) -> None:
            super().__init__('hr')

    class li(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('li', text)

    class menu(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('menu', text)

    class ol(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('ol', text)

    class p(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('p', text)

    class pre(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('pre', text)

    class ul(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('ul', text)
    
    # Inline text semantics

    class a(Tag):
        def __init__(self:Self, text:str='', href:str='#') -> None:
            super().__init__('a', text)
            self.attr('href', href)
    
    class abbr(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('abbr', text)
    
    class b(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('b', text)
    
    class bdi(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('bdi', text)
    
    class bdo(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('bdo', text)
    
    class br(Tag):
        def __init__(self:Self) -> None:
            super().__init__('br')
    
    class cite(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('div', text)
    
    class code(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('div', text)
    
    class data(Tag):
        def __init__(self:Self, text:str='', value:str='') -> None:
            super().__init__('div', text)
            self.attr('value', value)
    
    class dfn(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('dfn', text)
    
    class em(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('em', text)
    
    class i(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('i', text)
    
    class kbd(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('kbd', text)
    
    class mark(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('mark', text)
    
    class q(Tag):
        def __init__(self:Self, text:str='', cite:str='') -> None:
            super().__init__('q', text)
            self.attributes('cite', cite)

    class rp(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('rp', text)

    class rt(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('rt', text)

    class ruby(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('ruby', text)

    class s(Tag):
         def __init__(self:Self, text:str='') -> None:
            super().__init__('s', text)

    class samp(Tag):
         def __init__(self:Self, text:str='') -> None:
            super().__init__('samp', text)

    class small(Tag):
         def __init__(self:Self, text:str='') -> None:
            super().__init__('small', text)

    class span(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('span', text)

    class strong(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('strong', text)

    class sub(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('sub', text)

    class sup(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('sup', text)

    class time(Tag):
        def __init__(self:Self, text:str='', date_time:str='') -> None:
            super().__init__('time', text)
            self.attr('datetime', date_time)

    class u(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('u', text)

    class var(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('var', text)

    class wbr(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('wbr', text)

    # Image and multimedia

    class map(Tag):
         def __init__(self:Self, name:str='') -> None:
            super().__init__('map')
            self.attr('name', name)

    class area(Tag):
        pass # Will be added later, too many attributes

    class audio(Tag):
        pass # Will be added later, too many attributes

    class img(Tag):
        def __init__(self:Self, src:str='', alt:str='') -> None:
            super().__init__('img')
            self.attr('src', src)
            self.attr('alt', alt)

    class track(Tag):
        pass # Will be added later, too many attributes

    class video(Tag):
        pass # Will be added later, too many attributes

    # Embedded content

    class embed(Tag):
        def __init__(self:Self, type:str='', src:str='', width:str='', height:str='') -> None:
            super().__init__('embed')
            self.attr('type', type)
            self.attr('src', src)
            self.attr('width', width)
            self.attr('height', height)

    class iframe(Tag):
        pass # Will be added later, too many attributes

    class object(Tag):
        pass # Will be added later, too many attributes

    class picture(Tag):
        def __init__(self:Self) -> None:
            super().__init__('picture')

    class portal(Tag):
        def __init__(self:Self, text:str='', src:str='', referrer_policy:str='') -> None:
            super().__init__('portal', text)
            self.attr('src', src)
            self.attr('referrerpolicy', referrer_policy)

    class source(Tag):
        pass # Will be added later, too many attributes

    # SVG and MathML

    class svg(Tag):
        pass # Will be added later, too many attributes

    class math(Tag):
         def __init__(self:Self, text:str='') -> None:
            super().__init__('math', text)

    # Scripting

    class canvas(Tag):
         def __init__(self:Self, text:str='', width:str='', height:str='', moz_opaque:str='') -> None:
            super().__init__('canvas', text)
            self.attr('width', width)
            self.attr('height', height)
            self.attr('moz-opaque', moz_opaque)

    class noscript(Tag):
         def __init__(self:Self) -> None:
            super().__init__('noscript')

    class script(Tag):
        pass # Will be added later, too many attributes

    # Demarcating edits

    class _del(Tag): # Problem here
        pass

    class ins(Tag):
        def __init__(self:Self, text:str='', cite:str='', date_time:str='') -> None:
            super().__init__('ins', text)
            self.attr('cite', cite)
            self.attr('datetime', date_time)

    # Table content

    class caption(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('caption', text)

    class col(Tag):
        def __init__(self:Self, text:str='', span:str='') -> None:
            super().__init__('col', text)
            self.attr('span', span)

    class colgroup(Tag):
        def __init__(self:Self, text:str='', span:str='') -> None:
            super().__init__('colgroup', text)
            self.attr('span', span)

    class table(Tag):
            def __init__(self:Self, text:str='') -> None:
                super().__init__('table', text)

    class tbody(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('tbody', text)

    class td(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('td', text)

    class th(Tag):
        def __init__(self:Self, text:str='', scope:str='') -> None:
            super().__init__('th', text)
            self.attr('scope', scope)

    class tr(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('tr', text)

     class thead(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('thead', text)

    class tfoot(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('tfoot', text)

    # Forms (incomplete)

    class form(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('form', text)

    class input(Tag):
        def __init__(self:Self, type:str='', value:str='') -> None:
            super().__init__('input')
            self.attr('type', type)
            self.attr('value', value)

    class button(Tag):
        def __init__(self:Self, text:str='') -> None:
            super().__init__('button', text)