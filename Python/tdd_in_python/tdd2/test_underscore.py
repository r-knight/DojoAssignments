import unittest
from underscore import Underscore
class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
        self.test_list = [1,2,3,4,5]
        self.result_map = self._.map(self.test_list, lambda x: x + 1)
        self.result_find = self._.find(self.test_list, lambda x: x == 4)
        self.result_find2 = self._.find(self.test_list, lambda x: x == 6)
        self.result_filter = self._.filter(self.test_list, lambda x: x%2==0)
        self.result_reject = self._.reject(self.test_list, lambda x: x%2==1)
        self.result_reduce = self._.reduce(self.test_list, 0, lambda x, y: x + y)
    def testMap(self):
        return self.assertEqual([2,3,4,5,6], self.result_map)
    def testReduce(self):
        return self.assertEqual(20, self.result_reduce)
    def testFind(self):
        return (self.assertEqual(4, self.result_find) and self.assertEqual(False, self.result_find2))   
    def testFilter(self):
        return self.assertEqual([2,4,6], self.result_filter)
    def testReject(self):
        return self.assertEqual([2,4,6], self.result_reject)
if __name__ == "__main__":
    unittest.main()
