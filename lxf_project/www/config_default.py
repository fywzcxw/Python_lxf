#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'cxw',
        'password': 'cxw',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}