#author:mxp
#encoding=utf-8
from selenium import webdriver
import time

local_time = time.localtime(time.time())

while (local_time.tm_hour != 9) or (local_time.tm_min < 30):
	local_time = time.localtime(time.time())
	print("curtime:hour:%d, min:%d"%(local_time.tm_hour, local_time.tm_min))
	time.sleep(600)

#双休日
if (local_time.tm_wday == 5) or (local_time.tm_wday == 6):
	exit(0)
	
driver=webdriver.Ie()
driver.get("http://xxxxxxxxxx.com")

time.sleep(10)

elem_user=driver.find_element_by_id('txtLoginCode')
elem_user.clear()
elem_user.send_keys('nice_xp')
elem_pass=driver.find_element_by_id('txtPwd')
elem_pass.clear()
elem_pass.send_keys('*******')
elem_login=driver.find_element_by_id('btnLogin')
elem_login.click()

time.sleep(10)

elem_signin=driver.find_element_by_class_name('signIn1')
elem_signin.click()

time.sleep(5)

exit(0)