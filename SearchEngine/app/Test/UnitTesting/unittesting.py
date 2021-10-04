import unittest
from app.main.Controller.file_location import *
# unit testing class for file location
class TestFloc(unittest.TestCase):
    def test_drive1(self):
        self.assertEqual(multiThreading('program1.txt',['E:\\','F:\\']), [[], ['E:\\Zensar_Codes\\program1.txt']])
    def test_drive2(self):
        self.assertEqual(multiThreading('program1.txt',['F:\\']), [[]])
    def test_drive3(self):
        self.assertEqual(multiThreading('nithin.txt',['E:\\','F:\\','C:\\']),[['F:\\Tableau\\nithin.txt'],['C:\\Intel\\nithin.txt'],['E:\\PROJECT_FILES\\nithin.txt', 'E:\\zensar_ol\\nithin.txt']])
# main
if __name__ == '__main__':
    unittest.main()
