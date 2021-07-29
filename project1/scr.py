from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import lxml
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://boards.4chan.org/wg/thread/7621783")
content=driver.page_source
soup=BeautifulSoup(content,"lxml")
tag=[]
for a in soup.findAll(type(data-utc)==int):
     print(a)
driver.close()
