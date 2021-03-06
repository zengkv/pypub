#coding=utf-8
import unittest
import sys
sys.path.append(".")
from pypub import RemoteApp, CONFIG_T

class remoteappTest(unittest.TestCase):
    def test_remote(self):
        app = CONFIG_T.get_apps("ps")
        ra_remote = RemoteApp(app, "photo1")
        
        app = CONFIG_T.get_apps("app1")
        ra_local = RemoteApp(app, "local")
        
        ra_remote.get("dog.php", "temp/dog.php")
        ra_local.get("dir1/file3", "temp/file3")


        ra_remote.put("temp/dog.php", "temp/dog2.php")
        ra_local.put("temp/file3", "temp/file3")

        ra_remote.remove("temp/dog2.php")
        ra_local.remove("temp/file3")

        print ra_remote.file_md5("dog.php")
        print ra_local.file_md5("dir1/file3")

        print ra_remote.get_md5s()
        print ra_local.get_md5s()


if __name__ == '__main__':
    CONFIG_T.init_logger()
    unittest.main()