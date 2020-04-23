import unittest
import os
import time
from BeautifulReport import BeautifulReport

# 创建一个测试套件
suite = unittest.TestSuite

# 添加测试用例到测试套件
discover = unittest.defaultTestLoader.discover('./', 'test*.py')

report_dir = './report/'
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

BeautifulReport(discover).report(filename='result'+time.strftime('%Y%m%d', time.localtime(time.time())), description='描述', report_dir=report_dir)
# 运行套件
# runner = unittest.TextTestRunner()
# runner.run(discover)
