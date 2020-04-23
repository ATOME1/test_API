import unittest
from selenium import webdriver
from ddt import ddt, data
import time



@ddt
class forTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(r'E:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
        self.driver.get('http://www.baidu.com')

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()

    @data('张', '凡')
    @unittest.skipUnless(1 != 2, 'reason')
    def test_aaa(self,txt):
        self.driver.find_element_by_id('kw').send_keys(txt)
        self.driver.find_element_by_id('su').click()


# if __name__ == '__main__':
#     unittest.main()
