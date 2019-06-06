import unittest
from vectorSpace.vectorSpace import *
inverted_index = {
    "hello": {
        1: [3, 5, 10],
        17: [4, 6, 10]
    },
    "world": {
        3: [1],
        13: [3, 10],
        14: [1, 9, 20, 21]
    }
}

N = 30


class TestStringMethods(unittest.TestCase):
    def test_cal_df(self):
        tf = {
            "hello": 2,
            "world": 3
        }
        self.assertEqual(tf, cal_df(inverted_index))

    def test_cal_idf(self):
        df = cal_df(inverted_index)
        idf = {
            "hello": math.log(N / df["hello"], 10),
            "world": math.log(N / df["world"], 10)
        }
        self.assertEqual(idf, cal_idf(df, N))

    def test_cal_tf(self):
        tf = {
            "hello": {
                1: 1 + math.log(3, 10),
                17: 1 + math.log(3, 10),
            },
            "world": {
                3: 1 + math.log(1, 10),
                13: 1 + math.log(2, 10),
                14: 1 + math.log(4, 10),
            }
        }
        self.assertEqual(tf, cal_tf(inverted_index, N))


if __name__ == '__main__':
    unittest.main()
