import unittest
# import time
# import HTMLTestRunner
suit=unittest.TestSuite()
tests=unittest.defaultTestLoader.discover(
    './',pattern='test*.py'
)
suit.addTests(tests)
# now=time.strftime('%Y%m%d%H%M%S',time.localtime())
# report=now+'.html'
# file=open(report,'wb')
# runner=HTMLTestRunner.HTMLTestRunner(stream=file,title='测试报告',description='测试报告描述',tester='郭')
runner=unittest.TextTestRunner(verbosity=2)

runner.run(suit)