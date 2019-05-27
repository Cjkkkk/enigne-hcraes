'''
class: RankMethodBase
    description: the base class of rank base, every class inheriting it should implement the method rank.

'''


class RankMethodBase(object):
    def rank(self, documents, sentence):
        raise NotImplementedError
