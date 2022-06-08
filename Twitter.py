from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://twitter.com/i/flow/login")
sleep(4)

#Kullancici adi Giriş YYYYYYYYYYYYYY
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")\
    .send_keys("YYYYYYYYYYYYYYYYYY")
sleep(0.5)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")\
    .click()
sleep(1.5)
#Kullancici Şifre Giriş XXXXXXXXXXXXXX
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")\
    .send_keys("XXXXXXXXXXXXX")
sleep(0.5)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")\
    .click()
sleep(5)
driver.get("https://twitter.com/i/connect_people?user_id=1529431017177612290")
sleep(5)

for i in range(200):
    for a in range(10):
        b=str(a+3)
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div["+b+"]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/span/span")\
                  .click()               
        except:
            driver.refresh()
            print("gecildi"+b)
            pass       
        sleep(1.7)
    driver.refresh()
    sleep(300)


