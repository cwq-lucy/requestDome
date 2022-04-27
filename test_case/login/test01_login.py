import unittest
import requests
from ddt import ddt, data, unpack, file_data


@ddt
class loginCass(unittest.TestCase):

    @file_data('../data/login.yaml')
    def test_login03(self, loginName, encryption, yzm, userType, msgCode):
        data = dict(loginName=loginName, encryption=encryption, yzm=yzm, userType=userType, msgCode=msgCode)
        url = 'https://cms-api-test.jiaoyoushow.com/userInfo/checkPhoneLoginPost'
        res = requests.post(url, json=data)
        msg = res.json()
        print(msg)


if __name__ == '__main__':
    unittest.main()
