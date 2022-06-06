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

for i in range(20):
    for a in range(10):
        b=str(a+3)
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div["+b+"]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/span/span")\
                  .click()               
        except:
            pass       
        sleep(1.7)
    driver.refresh()
    #<span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">Takip et</span>
    #<div aria-describedby="id__6yjh28kyaqi" aria-label="Takip et @kahve1919" role="button" tabindex="0" class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr" data-testid="1488379504837943296-follow" style="background-color: rgb(239, 243, 244);"><div dir="auto" class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0" style="color: rgb(15, 20, 25);"><span class="css-901oao css-16my406 css-bfa6kz r-poiln3 r-1b43r93 r-1cwl3u0 r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">Takip et</span></span></div></div>
    sleep(7)


