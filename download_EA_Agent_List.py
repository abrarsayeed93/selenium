from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
import os
import os.path
import time
import shutil
import glob

driver = webdriver.Edge()
driver.implicitly_wait(100)

driver.get('https://studygroup.my.salesforce.com/00OD0000006sKSx')

try:
    driver.find_element_by_id("lexNoThanks").click()
    driver.find_element_by_css_selector(".checkbox:nth-child(6) .checkbox_faux").click()
    driver.find_element_by_id("lexSubmit").click()
    driver.find_element_by_name("csvsetup").click()
    driver.find_element_by_id("xf").click()
    Select(driver.find_element_by_id("xf")).select_by_visible_text("Comma Delimited .csv")
    driver.find_element_by_id("xf").click()
    driver.find_element_by_name("export").click()
except:
    try:
        time.sleep(10)
        driver.find_element_by_id("lexNoThanks").click()
        driver.find_element_by_css_selector(".checkbox:nth-child(6) .checkbox_faux").click()
        driver.find_element_by_id("lexSubmit").click()
        driver.find_element_by_name("csvsetup").click()
        driver.find_element_by_id("xf").click()
        Select(driver.find_element_by_id("xf")).select_by_visible_text("Comma Delimited .csv")
        driver.find_element_by_id("xf").click()
        driver.find_element_by_name("export").click()
    except:
        import logging

        date = datetime.today().strftime('%Y%m%d')
        logging.basicConfig(filename=date + '_ERROR.log', level=logging.DEBUG)
        logging.debug(
            'THERE WAS AN ERROR WHICH CAUSED THE FILE TO NOT BE DOWNLOADED. CHECK IF LIGHTNING MODE IS ON. SWITCH TO CLASSIC IF IT IS AND TRY AGAIN')
        logging.info(
            'Another issue could be that structure of the website loading has changed. Check if pop-ups are not enabled.')

time.sleep(10)

#move file to autodownloaded folder

src_dir = "C:\\Users\\asayeed\\Downloads\\"
dst_dir0 = "C:\\Users\\asayeed\\Downloads\\testing.csv"
dst_dir = "Y:\\Sales Effectiveness\\AutoDownloaded\\AUTO - Agent List EA.csv" #change this to final file name

while not len(glob.glob('C:\\Users\\asayeed\\Downloads\\report*.csv'))!=0:
    print("waiting for file to download")

if len(glob.glob('C:\\Users\\asayeed\\Downloads\\report*.csv'))==1:
    print("file is available now")
    file_path = glob.glob('C:\\Users\\asayeed\\Downloads\\report*.csv')[0]
    os.rename(file_path, dst_dir0)
    shutil.move(dst_dir0, dst_dir)
else:
    raise ValueError(" There isn't a file in %s!" % src_dir)