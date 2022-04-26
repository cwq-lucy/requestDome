import unittest
from  ddt import ddt,data,unpack,file_data

@ddt
class loginCass(unittest.TestCase):
     # @data(('zhangsan','123456'),('lisi','123456'))
     # @unpack
     @file_data('login.yaml')
     def test_login(self,username,password):
          data = {'username':username,'password':password}
          print(data)



if __name__ == '__main__':
     unittest.main()