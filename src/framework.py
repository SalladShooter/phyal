# Copyright (c) 2024 SalladShooter

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