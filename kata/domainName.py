# Solution by PauloBA

import re

pattern = re.compile(r'(https?://)?(www\.)?([^.]+)\.\w+')


def domain_name(url):
    res = re.match(pattern, url)
    return res.group(3)

arg1 = "http://google.com"
arg2 = "http://google.co.jp"
arg3 = "www.xakep.ru"
arg4 = "https://youtube.com"

print(domain_name(arg1))
print(domain_name(arg2))
print(domain_name(arg3))
print(domain_name(arg4))