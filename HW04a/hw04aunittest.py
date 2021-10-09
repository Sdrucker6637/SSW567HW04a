import unittest
import hw04a
from unittest import mock
from unittest.mock import patch

class hw04aunittest(unittest.TestCase):
    def userrepos_test1(self):
        self.assertEqual(hw04a.combined("Sdrucker6637","HW4"),"('Number of commits: ', 2)")
    
    @patch('hw04a.json.loads')

    def mockuserrepos_test1(self, mock_get):
        mock_get.return_value.count = "('Number of commits: ', 2)"
        response = hw04a.combined("Sdrucker6637","HW4")
        self.assertEqual(response, 0)

    def userrepos_test2(self):
        self.assertEqual(hw04a.combined("dfskdfnsdk","HW4"),"User Does Not Exist Error")
    
    @patch('hw04a.json.loads')
    def mockuserrepos_test2(self, mock_get):
        mock_get.return_value.count ="User Does Not Exist Error"
        response = hw04a.combined("dfskdfnsdk","HW4")
        self.assertEqual(response, "User Does Not Exist Error")
if __name__ == '__main__':  

    unittest.main()