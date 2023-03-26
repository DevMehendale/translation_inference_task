from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from langdetect import detect
import numpy as np

import multiprocessing
import os

def get_url_func(browser,url):
    try:
        browser.get(url)
        browser.refresh()
    except:
        browser.get(url)
        browser.refresh()
        
def get_sentences(browser,url,language,is_lang_selected):
    get_url_func(browser,url)

    browser.implicitly_wait(10)

    if is_lang_selected==0:
        time.sleep(3)
        browser.implicitly_wait(10)
        try:
            element = browser.find_element('xpath',"//div[@class='language-dropdown dropdown-menu']")
        except:
            browser.refresh()
            time.sleep(3)
            element = browser.find_element('xpath',"//div[@class='language-dropdown dropdown-menu']")

        browser.implicitly_wait(10)

        browser.execute_script("arguments[0].style.display = 'block';", element)

        browser.implicitly_wait(10)

        button = browser.find_element('xpath',"//button[text()='{}']".format(language))

        browser.implicitly_wait(10)
        time.sleep(3)

        ActionChains(browser).move_to_element(button).click(button).perform()


        browser.implicitly_wait(10)
        
    browser.refresh()
    time.sleep(3)
    
    # Use Bs to Parse
    soup = BeautifulSoup(browser.page_source, 'html5lib')
    #print(soup.prettify())
    
    return soup.body.get_text('-_-_-', strip=True).split('-_-_-')

def get_data_text(language):
    # Setup
    print(language)
    options = Options()
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #--| Parse or automation
    url = "https://www.poshantracker.in/"
    
    sentences = get_sentences(browser,url,language,0)
    
    # Access other pages through href links
    soup = BeautifulSoup(browser.page_source, 'html5lib')
    for link in soup.findAll('a'):
        link_temp=link.get('href')
        #rint(link_temp)
        if link_temp!=None:
            if link_temp[0]=='/' and len(link_temp)>1:
                #rowser.close()
                #rowser.get(url)
                sentences.extend(get_sentences(browser,url+link_temp[1:],language,1))
                
    print('Predicted language:',detect(soup.body.get_text(' ', strip=True)),'  Actual language:',language)
            
    browser.quit()

    
    return sentences