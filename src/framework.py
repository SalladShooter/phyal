from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response


class App:

  def __init__(self):
    self.url_map = Map()
    self.view_functions = {}
    self.html_content = []

  def route(self, rule, **options):

    def decorator(function):
      self.url_map.add(Rule(rule, endpoint=function.__name__))
      self.view_functions[function.__name__] = function
      return function

    return decorator

  def dispatch_request(self, request):
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

  def run(self, host='0.0.0.0', port=5000):
    app = SharedDataMiddleware(self, {'/static': 'static'})
    run_simple(host, port, app)

  def reload_content(self, new_content):
    self.html_content = new_content


class Tag:

  def __init__(self, name, text=''):
    self.name = name
    self.attributes = []
    self.children = []
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

  class abbr(Tag):

    def __init__(self, text='', title=''):
      super().__init__('abbr', text)
      self.attribute('title', title)

  class b(Tag):

    def __init__(self, text=''):
      super().__init__('b', text)

  class bdi(Tag):

    def __init__(self, text=''):
      super().__init__('bdi', text)

  class bdo(Tag):

    def __init__(self, text=''):
      super().__init__('bdo', text)

  class br(Tag):

    def __init__(self, text=''):
      super().__init__('br', text)

  class cite(Tag):

    def __init__(self, text=''):
      super().__init__('cite', text)

  class code(Tag):

    def __init__(self, text=''):
      super().__init__('code', text)

  class data(Tag):

    def __init__(self, text='', value=''):
      super().__init__('data', text)
      self.attribute('value', value)

  class dfn(Tag):

    def __init__(self, text=''):
      super().__init__('dfn', text)

  class em(Tag):

    def __init__(self, text=''):
      super().__init__('em', text)

  class i(Tag):

    def __init__(self, text=''):
      super().__init__('i', text)

  class kbd(Tag):

    def __init__(self, text=''):
      super().__init__('kbd', text)

  class mark(Tag):

    def __init__(self, text=''):
      super().__init__('mark', text)

  class q(Tag):

    def __init__(self, text='', cite=''):
      super().__init__('q', text)
      self.attribute('cite', cite)

  class q(Tag):

    def __init__(self, text='', cite=''):
      super().__init__('q', text)
      self.attribute('cite', cite)
  
  class rp(Tag):

    def __init__(self, text=''):
      super().__init__('rp', text)

  class rt(Tag):

    def __init__(self, text=''):
      super().__init__('rt', text)

  class ruby(Tag):

    def __init__(self, text=''):
      super().__init__('ruby', text)

  class s(Tag):

    def __init__(self, text=''):
      super().__init__('s', text)

  class samp(Tag):

    def __init__(self, text=''):
      super().__init__('samp', text)

  class small(Tag):

    def __init__(self, text=''):
      super().__init__('small', text)

  class span(Tag):

    def __init__(self, text=''):
      super().__init__('span', text)

  class strong(Tag):

    def __init__(self, text=''):
      super().__init__('strong', text)

  class sub(Tag):

    def __init__(self, text=''):
      super().__init__('sub', text)

  class sup(Tag):

    def __init__(self, text=''):
      super().__init__('sup', text)

  class time(Tag):

    def __init__(self, text='', cite=''):
      super().__init__('time', text)

  class u(Tag):

    def __init__(self, text=''):
      super().__init__('u', text)

  class var(Tag):

    def __init__(self, text=''):
      super().__init__('var', text)

  class wbr(Tag):

    def __init__(self, text=''):
      super().__init__('wbr', text)

  class area(Tag):

    def __init__(self, text='', alt='', coords='', download='', href='', ping='', referrerpolicy='', rel='', shape='', target=''):
      super().__init__('area', text)
      self.attribute('alt', alt)
      self.attribute('coords', coords)
      self.attribute('download', download)
      self.attribute('href', href)
      self.attribute('ping', ping)
      self.attribute('referrerpolicy', referrerpolicy)
      self.attribute('rel', rel)
      self.attribute('shape', shape)
      self.attribute('target', target)

  class audio(Tag):

    def __init__(self, text='', autoplay='', controls='', controlslist='', crossorigin='', disableremoteplayback='', loop='', muted='', preload='', src=''):
      super().__init__('audio', text)
      self.attribute('autoplay', autoplay)
      self.attribute('controls', controls)
      self.attribute('controlslist', controlslist)
      self.attribute('crossorigin', crossorigin)    
      self.attribute('disableremoteplayback', disableremoteplayback)
      self.attribute('loop', loop)
      self.attribute('muted', muted)
      self.attribute('preload', preload)
      self.attribute('src', src)

  class map(Tag):

    def __init__(self, text='', name=''):
      super().__init__('map', text)
      self.attribute('name', name)

  class track(Tag):

    def __init__(self, text='', cite='', default='', kind='', label='', src='', srclang=''):
      super().__init__('track', text)
      self.attribute('default', default)
      self.attribute('kind', kind)
      self.attribute('label', label)
      self.attribute('src', src)
      self.attribute('srclang', srclang)

  class video(Tag):

    def __init__(self, text='', autoplay='', controls='', controlslist='', crossorigin='', disablepictureinpicture='', disableremoteplayback=''):
      super().__init__('video', text)
      self.attribute('autoplay', autoplay)
      self.attribute('controls', controls)
      self.attribute('controlslist', controlslist)
      self.attribute('crossorigin', crossorigin)
      self.attribute('disablepictureinpicture', disablepictureinpicture)
      self.attribute('disableremoteplayback', disableremoteplayback)

  class embed(Tag):

    def __init__(self, text='', height='', src='', type='', width=''):
      super().__init__('embed', text)
      self.attribute('height', height)
      self.attribute('src', src)
      self.attribute('type', type)
      self.attribute('width', width)

  class iframe(Tag):

    def __init__(self, text='', allow='', allowfullscreen='', allowpaymentrequest='', browsingtopics='', credentialless='', csp='', height='', loading='', name='', referrerpolicy='', sandbox='', src='', srcdoc='', width=''):
      super().__init__('iframe', text)
      self.attribute('allow', allow)
      self.attribute('allowfullscreen', allowfullscreen)
      self.attribute('allowpaymentrequest', allowpaymentrequest)
      self.attribute('browsingtopics', browsingtopics)
      self.attribute('credentialless', credentialless)
      self.attribute('csp', csp)
      self.attribute('height', height)
      self.attribute('loading', loading)
      self.attribute('name', name)
      self.attribute('referrerpolicy', referrerpolicy)
      self.attribute('sandbox', sandbox)
      self.attribute('src', src)
      self.attribute('srcdoc', srcdoc)
      self.attribute('width', width)

  class object(Tag):

    def __init__(self, text='', archive='', border='', classid='', codebase='', codetype='', data='', declare='', height='', name='', standby='', type='', usemap='', width=''):
      super().__init__('object', text)
      self.attribute('archive', archive)
      self.attribute('border', border)
      self.attribute('classid', classid)
      self.attribute('codebase', codebase)
      self.attribute('codetype', codetype)
      self.attribute('data', data)
      self.attribute('declare', declare)
      self.attribute('height', height)
      self.attribute('name', name)
      self.attribute('standby', standby)
      self.attribute('type', type)
      self.attribute('usemap', usemap)
      self.attribute('width', width)

  class picture(Tag):

    def __init__(self, text='', img=''):
      super().__init__('picture', text)
      self.attribute('img', img)

  class portal(Tag):

    def __init__(self, text='', referrerpolicy='', src=''):
      super().__init__('portal', text)
      self.attribute('referrerpolicy', referrerpolicy)
      self.attribute('src', src)

  class source(Tag):

    def __init__(self, text='', type='', src='', srcset='', sizes='', media='', height='', width=''):
      super().__init__('source', text)
      self.attribute('type', type)
      self.attribute('src', src)
      self.attribute('srcset', srcset)
      self.attribute('sizes', sizes)
      self.attribute('media', media)
      self.attribute('height', height)
      self.attribute('width', width)

  class svg(Tag):

    def __init__(self, text='', baseProfile='', height='', preserveAspectRatio='', version='', viewBox='', width='', x='', y=''):
      super().__init__('svg', text)
      self.attribute('baseProfile', baseProfile)
      self.attribute('height', height)
      self.attribute('preserveAspectRatio', preserveAspectRatio)
      self.attribute('version', version)
      self.attribute('viewBox', viewBox)
      self.attribute('width', width)
      self.attribute('x', x)
      self.attribute('y', y)

  class math(Tag):

    def __init__(self, text='', display=''):
      super().__init__('math', text)
      self.attribute('display', display)

  class canvas(Tag):

    def __init__(self, text='', height='', mozopaque='', width=''):
      super().__init__('canvas', text)
      self.attribute('height', height)
      self.attribute('moz-opaque', mozopaque)
      self.attribute('width', width)

  class noscript(Tag):

    def __init__(self, text=''):
      super().__init__('noscript', text)

  class script(Tag):

    def __init__(self, text='', a_sync='', blocking='', crossorigin='', defer='', fetchpriority='', integrity='', nomodule='', nonce='', referrerpolicy='', src='', type=''):
      super().__init__('script', text)
      self.attribute('async', a_sync)
      self.attribute('blocking', blocking)
      self.attribute('crossorigin', crossorigin)
      self.attribute('defer', defer)
      self.attribute('fetchpriority', fetchpriority)
      self.attribute('integrity', integrity)
      self.attribute('nomodule', nomodule)
      self.attribute('nonce', nonce)
      self.attribute('integrity', integrity)
      self.attribute('referrerpolicy', referrerpolicy)
      self.attribute('src', src)
      self.attribute('type', type)
