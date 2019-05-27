'''
class: Document
    inherit: tuple
    description: inheriting from tuple, Document class can just be converted from sql cursor.fetchall(),
    attributes:
        name: document name
        title: document title
        url: document url
        clusters: document's clusters in words vectors space.
'''


class Document(tuple):
    def __init__(self,tuple=None):
        tuple.__init__(tuple)
        self.name = self[0]
        self.title = self[1]
        self.url = self[2]
        self.clusters = None
    