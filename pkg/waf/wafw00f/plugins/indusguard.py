
NAME = 'IndusGuard (Indusface)'


def is_waf(self):
    if self.matchHeader(('Server', r'IF_WAF')):
        return True

    if self.matchContent(r'This website is secured against online attacks. Your request was blocked'):
        return True

    return False