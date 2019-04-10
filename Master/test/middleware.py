from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class LoginFilter(MiddlewareMixin):
    no_filter = [
        '/login',
        '/join',
        '/api/login',
        '/api/join',
        '/init'
    ]

    def process_request(self, requests):
        if requests.path not in self.no_filter and not requests.user.is_authenticated:
            return redirect('/login')
