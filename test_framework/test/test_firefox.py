# https://www.cnblogs.com/zhaof/p/6953241.html
import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "http://www.baidu.com"
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
driver_path = os.path.abspath(base_path + '\drivers\geckodriver.exe')
print(driver_path)
locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

driver = webdriver.Firefox(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium 灰蓝')
driver.find_element(*locator_su).click()
time.sleep(3)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)

url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
driver.get(url)
driver.switch_to.frame('iframeResult')
source = driver.find_element_by_css_selector('#draggable')
target = driver.find_element_by_css_selector('#droppable')
actions = ActionChains(driver)
actions.drag_and_drop(source, target)
actions.perform()
time.sleep(3)

driver.get("http://www.zhihu.com/explore")
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
driver.execute_script('alert("To Bottom")')
# driver.quit()

driver.get('https://www.taobao.com/')
wait = WebDriverWait(driver, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
