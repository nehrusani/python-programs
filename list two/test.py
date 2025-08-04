# this is to create class with multiple function
# wich can be usedanywhere 
# for eg.
#create a file import.py
"""
from test import mouth2
dummy = mouth2("hello from another file")
dummy.india()
"""
class mouth2:
    def __init__(self, text):
        self.text = text
    def india(self):
        print(self.text)