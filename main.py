import re

print("Hello")

def _is_inverse_proxy_host(host):
    if host:
        return re.match(r'\S+.googleusercontent.com/{0,1}$', host)
    if re.match(r'\w+', host):
        warnings.warn(
            'The received host is %s, please include the full endpoint address '
            '(with ".(pipelines/notebooks).googleusercontent.com")' % host)
    return False

_is_inverse_proxy_host("123")
