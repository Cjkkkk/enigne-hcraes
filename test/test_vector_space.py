import unittest
from vectorSpace.vectorSpace import *

inverted_index = {
    "hello": {
        0: [3, 5, 10],
        1: [4, 6, 10]
    },
    "world": {
        2: [1],
        3: [3, 10],
        4: [1, 9, 20, 21]
    }
}
N = 5

df = {
    "hello": 2,
    "world": 3
}
idf = {
    "hello": math.log(N / df["hello"], 10),
    "world": math.log(N / df["world"], 10)
}
tf = {
    "hello": {
        0: 1 + math.log(3, 10),
        1: 1 + math.log(3, 10),
    },
    "world": {
        2: 1 + math.log(1, 10),
        3: 1 + math.log(2, 10),
        4: 1 + math.log(4, 10),
    }
}
wf = {
    0: {
        "hello": idf["hello"] * tf["hello"][0]
    },
    1: {
        "hello": idf["hello"] * tf["hello"][1]
    },
    2: {
        "world": idf["world"] * tf["world"][2]
    },
    3: {
        "world": idf["world"] * tf["world"][3]
    },
    4: {
        "world": idf["world"] * tf["world"][4]
    }
}


class TestStringMethods(unittest.TestCase):
    def test_cal_wf(self):
        vector_space = VectorSpace(inverted_index, True, 5)
        self.assertEqual(wf, vector_space.wf)


if __name__ == '__main__':
    unittest.main()
