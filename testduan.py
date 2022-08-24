from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=None
class Py(unittest.TestCase):
        @classmethod
        def setUpClass(cls) :
            global driver
            driver=webdriver.Chrome()
            driver.get('http://ctest.loulilouwai.com.cn/admin/login/index.html')

        # @classmethod
        # def tearDownClass(cls):
        #     '''关闭'''
        #     driver.quit()
        def test01(self):
            '''登录'''
            driver.find_element_by_xpath('//input[@class="username"]').send_keys('')
            driver.find_element_by_xpath('//input[@class="password"]').send_keys('')
            driver.find_element_by_xpath('//input[@value="确定"]').click()
            sleep(2)
            test=driver.find_element_by_tag_name('dl').text
            exec='欢迎来到'
            try:
                if exec in test:
                   print("登录成功通过")
                else:
                    print("登录失败"+str(test))
            except Exception as e:
                print(e)
        def test02(self):
            '''打开营销'''
            driver.find_element_by_partial_link_text('营销').click()
            driver.find_element_by_partial_link_text('优惠活动').click()
            driver.find_element_by_partial_link_text('活动优惠').click()
            driver.find_element_by_partial_link_text('添加优惠').click()
            sleep(2)
            result=driver.find_element_by_xpath('//div[@class="lou-bread-crumbs"]').text
            exce='添加优惠'
            try:
                if exce in result:
                    print('打开营销通过')
                else:
                    print('打开营销失败',+str(result))
            except Exception as e:
                print(e)

        def test03(self):
            '''填写营销活动基本信息'''
            driver.find_element_by_xpath('//input[@name="activity_name"]').send_keys('饮料促销')
            driver.find_element_by_xpath('//input[@class="each-edit-item goods_name"]').send_keys('全场八折')
            driver.find_element_by_xpath('//input[@id="description"]').send_keys('厂家提供')
            driver.find_element_by_xpath('//label[@for="coupon_type1"]').click()
            driver.find_element_by_xpath('//input[@id="minDate"]').click()
            driver.find_element_by_xpath('//td[@lay-ymd="2022-8-27"]').click()
            driver.find_element_by_xpath('//input[@id="maxDate"]').click()
            driver.find_element_by_xpath('//td[@lay-ymd="2022-8-29"]').click()
            driver.find_element_by_xpath('//label[@for="week6"]').click()
            driver.find_element_by_xpath('//label[@for="week7"]').click()
            driver.find_elements_by_xpath('//span[@class="c_drop-down"]')[0].click()
            driver.find_element_by_xpath('//label[@for="city97"]').click()
            sleep(2)

        def test04(self):
            '''配置优惠券张数'''
            element= driver.find_element_by_xpath('//input[@id="total_limit2"]')
            ActionChains(driver).double_click(element).perform()
            element.send_keys(200)
            elements= driver.find_element_by_xpath('//input[@id="get_limit2"]')
            ActionChains(driver).double_click(elements).perform()
            elements.send_keys(2)
            get_limit2= driver.find_element_by_xpath('//input[@id="day_get_limit2"]')
            ActionChains(driver).double_click(get_limit2).perform()
            get_limit2.send_keys(2)
            sleep(2)

        def test61(self):
            '''保存活动'''
            driver.find_element_by_xpath('//a[@class="lou-btn confirm-btn"]').click()
            sleep(2)
            results=driver.switch_to.alert
            result=results.text

            exec='添加成功'
            try:
                if exec in result:
                    print('添加活动成功')
                else:
                    print('添加活动失败',+str(result))
                results.accept()
            except Exception as e:
                print(e)
if __name__=='__main__':
    unittest.main(verbosity=2)