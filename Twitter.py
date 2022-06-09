from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

kacKereGecildi=0
kacKisiTakipEdildi=0

kullaniciAdi=input("KULLANICI ADI: ")
kullaniciSifre=input("KULLANICI SİFRE: ")

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://twitter.com/i/flow/login")
sleep(4)

driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")\
    .send_keys(kullaniciAdi)
sleep(0.5)

driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")\
    .click()

sleep(1.5)

try:
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")\
        .send_keys(kullaniciSifre)
except:
    print("\n\n\n\nkullanici adi hatalı")
    driver.close()
    exit("Tekrar deneyeiniz")
sleep(0.5)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")\
   .click()

sleep(5)
driver.get("https://twitter.com/i/connect_people?user_id=1529431017177612290")
sleep(5)

for i in range(30):

    for a in range(15):

        b=str(a+3)
        try: 
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div["+b+"]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/span/span")\
                  .click()
            kacKisiTakipEdildi=kacKisiTakipEdildi+1;               
        except:
            kacKereGecildi=kacKereGecildi+1
            pass       
        sleep(1.7)
    driver.refresh()
    print("Button: "+b+" gecildi                SimdiyeKadarGecilen: "+kacKereGecildi+"            Kac kisi takip ediliyor: "+kacKisiTakipEdildi)
    sleep(300)

print("Bitti")

