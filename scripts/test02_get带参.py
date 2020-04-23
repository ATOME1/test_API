import requests, unittest


# url = 'http://www.baidu.com'

# 案例1
# params = {'id': 1001}
# 案例2
# params = {'id': '1001,1002'} #不推荐
# 案例3
# params = {'id': 1001, 'kw': '北京'}
#
# res = requests.get(url, params)
#
# res.encoding = 'utf-8'
#
# print('请求地址是:', res.url)
# print('返回状态码', res.status_code)
# print('返回文本信息:', res.text)
# print(res.headers)


class apiTest(unittest.TestCase):

    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test_api01(self):
        url = 'http://www.baidu.com'
        params = {'id': 1001, 'kw': '北京'}
        # try:
        res = self.session.get(url, params=params)
        res.encoding = 'utf-8'
        # self.assertIn('百度一下，1你就知道', res.text, '失败')
        self.assertEqual('1', '2')
        # except Exception as e:
        #     print('错误原因：')
        #     raise e

# if __name__ == '__main__':
#     unittest.main()
