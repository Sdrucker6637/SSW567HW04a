import unittest
import hw04a

class testhw04a(unittest.TestCase):
    def userrepos_test1(self):
        self.assertEqual(hw04a.combined("Sdrucker6637","HW4"),"('Number of commits: ', 2)")
    def userrepos_test2(self):
        self.assertEqual(hw04a.combined("dfskdfnsdk","HW4"),"User Does Not Exist Error")
if __name__ == '__main__':  

    unittest.main()