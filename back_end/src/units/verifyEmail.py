import re

def is_valid_email(addr):
    re_email = re.compile(r'^\w+\.?\w+\@(gmail|microsoft|qq)\.com$')
    if re_email.match(addr):
        return True
    else:
        return False

def name_of_email(addr):
    re_name_email = re.compile(r'^(<([\w\s]+)>\s\w+|\w+)\@\w+\.(org|com)$')
    p = re_name_email.match(addr)

    if p:
        if p.group(2):
            return p.group(2)
        else:
            return p.group(1)