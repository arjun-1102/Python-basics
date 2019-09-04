# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:39:54 2019

@author: Vader
"""

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        final = []
        for i in self.pattern:
            if i == '.':
                final.append("dot")
            if i == "_":
                final.append("dash")

        return "-".join(final)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)