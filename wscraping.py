from selenium import webdriver
driver=webdriver.Chrome()
driver.get('http://iitmandi.co.in/?fbclid=IwAR3X6SS3Zj26ksPLTVaZgIQWwdr2_EBuke8oeHd4ROwLPCgZ_5oXPtNBHa4')
someText=driver.find_element_by_id('body-content')
print(someText.text)
driver.close()