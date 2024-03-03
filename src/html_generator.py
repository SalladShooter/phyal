# Copyright (c) 2024 SalladShooter

class Tag:

    def __init__(self, name, text=''):
        self.name = name
        self.attributes = attributes
        self.children = children
        self.text = text

    def attribute(self, key, value):
        self.attributes.append((key, value))
        return self

    def id(self, value):
        self.attributes.append(('id', value))
        return self

    def add_children(self, *tags):
        self.children.extend(tags)
        return self

    def __str__(self):
        attrs = ' '.join([f'{k}="{v}"' for k, v in self.attributes])
        children = ''.join(map(str, self.children))
        return f'<{self.name} {attrs}>{self.text}{children}</{self.name}>'

class Tags:

    class div(Tag):
        def __init__(self, text=''):
            super().__init__('div', text)

    class address(Tag):
        def __init__(self, text=''):
            super().__init__('address', text)
    
    class article(Tag):
        def __init__(self, text=''):
            super().__init__('article', text)

    class aside(Tag):
        def __init__(self, text=''):
            super().__init__('aside', text)

    class footer(Tag):
        def __init__(self, text=''):
            super().__init__('footer', text)

    class header(Tag):
        def __init__(self, text=''):
            super().__init__('header', text)

    class hgroup(Tag):
        def __init__(self, text=''):
            super().__init__('hgroup', text)

    class main(Tag):
        def __init__(self, text=''):
            super().__init__('main', text)

    class section(Tag):
        def __init__(self, text=''):
            super().__init__('section', text)

    class search(Tag):
        def __init__(self, text=''):
            super().__init__('search', text)

    class figure(Tag):
        def __init__(self, text=''):
            super().__init__('figure', text)

    class blockquote(Tag):
        def __init__(self, text='', cite=''):
            super().__init__('blockquote', text)
            self.attribute('cite', cite)
    
    class p(Tag):
        def __init__(self, text=''):
            super().__init__('p', text)

    class h1(Tag):
        def __init__(self, text=''):
            super().__init__('h1', text)
            
    class h2(Tag):
        def __init__(self, text=''):
            super().__init__('h2', text)
            
    class h3(Tag):
        def __init__(self, text=''):
            super().__init__('h3', text)
            
    class h4(Tag):
        def __init__(self, text=''):
            super().__init__('h4', text)
            
    class h5(Tag):
        def __init__(self, text=''):
            super().__init__('h5', text)
            
    class h6(Tag):
        def __init__(self, text=''):
            super().__init__('h6', text)
    
    class span(Tag):
        def __init__(self, text=''):
            super().__init__('span', text)

    class dd(Tag):
        def __init__(self, text=''):
            super().__init__('dd', text)

    class dl(Tag):
        def __init__(self, text=''):
            super().__init__('dl', text)
    
    class dt(Tag):
        def __init__(self, text=''):
            super().__init__('dt', text)

    class figcaption(Tag):
        def __init__(self, text=''):
            super().__init__('figcaption', text)

    class hr(Tag):
        def __init__(self, text=''):
            super().__init__('hr', text)

    class menu(Tag):
        def __init__(self, text=''):
            super().__init__('menu', text)

    class ol(Tag):
        def __init__(self, text=''):
            super().__init__('ol', text)

    class pre(Tag):
        def __init__(self, text=''):
            super().__init__('pre', text)
    
    class ul(Tag):
        def __init__(self, text=''):
            super().__init__('ul', text)

    class li(Tag):
        def __init__(self, text=''):
            super().__init__('li', text)

    class a(Tag):
        def __init__(self, text='', href='#'):
            super().__init__('a', text)
            self.attribute('href', href)

    class img(Tag):
        def __init__(self, src='', alt=''):
            super().__init__('img')
            self.attribute('src', src)
            self.attribute('alt', alt)

    class table(Tag):
        def __init__(self, text=''):
            super().__init__('table', text)

    class tr(Tag):
        def __init__(self, text=''):
            super().__init__('tr', text)

    class th(Tag):
        def __init__(self, text=''):
            super().__init__('th', text)

    class td(Tag):
        def __init__(self, text=''):
            super().__init__('td', text)

    class form(Tag):
        def __init__(self, text=''):
            super().__init__('form', text)

    class input(Tag):
        def __init__(self, type='', value=''):
            super().__init__('input')
            self.attribute('type', type)
            self.attribute('value', value)

    class button(Tag):
        def __init__(self, text=''):
            super().__init__('button', text)
