######################################
#
# Alexander M. Thompson
# CS 250
# Assignment 7
#
#
# filename = a7.py
#
#######################################

import string
class XmlFinder:
    def __init__(self, filename):
        self._filename = filename

    def break_up(self):
        tokens = []
        token = ''
        f = open(self._filename, 'rt')
        c = f.read(1)
        while c:
            if c in string.whitespace:
                if token != '':
                    tokens.append(token)
                token = ''
            elif c == '#':
                while c != '\n':
                    c = f.read(1)
            else:
                token += c
            c = f.read(1)
        if token != '':
            tokens.append(token)
        f.close()
        for token in tokens:
            return token

    def break_up_choice(self, choice):
        choice = [choice]
        weird = []
        for i in choice:
            for c in i:
                weird.append(c)
        return weird

    def find(self, tags, weird):
        if '>' in weird and '<' in weird:
            for i in weird:
                chosen = tags.find(i)
                if chosen == int():
                    return True
                else:
                    return False
        else:
            return 'Does not exist in file'
        
def main():
    choice = '<too>'
    x = XmlFinder('test.xml')
    print(x.find(x.break_up(), x.break_up_choice(choice)))
main()
            
