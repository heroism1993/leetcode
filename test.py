#!/bin/python

class test(object):
    def __init__(self):
        self.followers=dict()

    def run(self):
        self.followers["hahaha"]=set([1])

    def get_item(self,key="key"):
        if(not self.followers.__contains__(key)):
            self.followers[key]=set()
        return self.followers[key]


if(__name__=="__main__"):
    t = test()
    t.run()
    print t.get_item()
    a= t.get_item("hahaha")
    for i in a:
        print i