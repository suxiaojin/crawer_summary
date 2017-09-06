# -*- coding: utf-8 -*-
import urllib.request

def demo():
    s = urllib.request.urlopen('http://blog.kamidox.com')
    for i in range(10):
       print('line %d  %s' %(i+1,s.readline()))


if __name__ == '__main__':
    demo()