import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.file_management.create_apikeyfile import *
from lib.function_network.func_network import CallApi
from lib.file_management.file_management_lib import DirManagement

class TestCallApi(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir,"ta")
        DirManagement.create_dir(self.path)
        self.data = {"prefix" : "https://ta-api.sirateek.dev/",
                "workId" : 'testWork2',
                "apikeydir" : os.path.join(os.path.expanduser("~"), 'key')}
        with open(os.path.join(self.path, 'config.json'), "w") as wri:
            json.dump(self.data, wri)
        removeapikey()
        save_api_key('testKey')
        self.call = CallApi(parentdir)
        return super().setUp()

    def Test_apimassage(self):
        """
        return dict
        """
        self.assertIs(type(self.call.api_massage()), dict)

    def Test_fetch(self):
        """
        return boolean
        """
        self.assertTrue(self.call.fetch())

    def Test_CreateWork(self):
        """
        print(str)
        """
        self.assertTrue(self.call.createworkdraft())


    def test_Writejson(self):
        """
        return None
        """
        self.assertIsNone(self.call.writejson(self.data))
        

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path)
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()