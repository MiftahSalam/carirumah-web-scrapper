import datetime
import time
import json
import base64
import urllib
import sys
from urllib import request
from pathlib import Path
from enum import IntEnum

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common import exceptions as EXCPT

from .settings import CHROME_DRIVER_PATH
from .Item import Item

STATUS_TYPE = {
    'jual':'JL',
    'sewa':'SW',
    '-':'JS',
}

PROPERTY_TYPE = {
    'rumah':'RM',
    'tanah':'TN',
    'apartement':'AP',
}

class DriverType(IntEnum):
    CHROME = 1,
    FIREFOX = 2

class Scrapper:
    def __init__(self, driver, url):
        self.driver_type = driver

        if self.driver_type == DriverType.CHROME: 
            opt = Options()
            # opt.add_argument('--log-level=3')
            # self.driver = ''
            caps = DesiredCapabilities().CHROME
            caps['pageLoadStrategy'] = "normal"
            # caps['pageLoadStrategy'] = "none" #do not wait until page fully loaded
            print("Scrapper init: load webdriver")
            if sys.platform == 'linux':
                self.driver = webdriver.Chrome(options=opt, desired_capabilities=caps)
            else:
                self.driver = webdriver.Chrome(CHROME_DRIVER_PATH,options=opt,desired_capabilities=caps)

        self.driver.maximize_window()
        self.url = url
        self.start_scrapping()
    
    def post_data(self,payload,url,credential):
        credential_b64 = base64.b64encode(credential.encode("ascii")).decode("ascii")
        req = request.Request(url)
        data = json.dumps(payload)
        data_byte = data.encode('utf-8')
        req.add_header('Method','POST')
        req.add_header('Authorization', 'Basic '+credential_b64)
        req.add_header('Content-Type', 'application/json')
        req.add_header('User-Agent', 'PostmanRuntime/7.26.10')
        req.add_header('Accept', '*/*')
        req.add_header('Content-Length',len(data_byte))

        try:
            res = request.urlopen(req,data_byte)
            print("Posting data", payload['property_name'], "succesed")
        except urllib.error.HTTPError as e:
            print("Posting data:", payload['property_name'], "with error:",e.read().decode('utf-8','ignore'))

    def toJson(self,items):
        return json.dumps(items)
    
    def conditioner(self,items):
        pass

    def start_scrapping(self):
        print("Scrapper start scrapping. url:",self.url)
        self.driver.get(self.url)
        self.current_page_source = self.driver.page_source
        self.home_tab_handle = self.driver.current_window_handle
        time.sleep(5)

    def stop_scrapping(self):
        self.driver.close() 
    
    def get_element_child(self, parent_el, find_by, token):
        el = None
        if find_by == 'id':
            try:
                el = parent_el.find_element_by_id(token)
                # print("get_element_child by id. El text:", el.text)
            except EXCPT.NoSuchElementException:
                print("get_element_child by id error. No such elemen")
            except:
                print("get_element_child by id error. Unknown error")
        elif find_by == 'css':
            try:
                el = parent_el.find_element_by_css_selector(token)
                # print("get_element_child by css. El text:", el.text)
            except EXCPT.NoSuchElementException:
                print("get_element_child by css error. No such elemen")
            except:
                print("get_element_child by css error. Unknown error")
        elif find_by == 'tag':
            try:
                el = parent_el.find_element_by_tag_name(token)
                # print("get_element_child by tag. El text:", el.text)
            except EXCPT.NoSuchElementException:
                print("get_element_child by tag error. No such elemen")
            except:
                print("get_element_child by tag error. Unknown error")
        else:
            print("Token not supported")
            raise BaseException;

        return el

        
    def parse_css(self,css_selector):
        # print("parse css selector: ", css_selector)

        try:
            elements = WebDriverWait(self.driver,15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,css_selector)))
            return elements
        except EXCPT.TimeoutException:
            print("Finding element reach timeout")
        except:
            print("Unknown error. Failed to get element")

        return None
    
    def get_items(self, current_page_el, css_selector, current_items={}):
        for key in css_selector:
            value = css_selector[key]
            if type(css_selector[key]) != dict:
                # print("searching :","(",key,"->",css_selector[key],")")
                if value == '':
                    current_items.update({key: '-'})
                    continue
                
                try:
                    current_el = WebDriverWait(self.driver,15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,value)))
                    time.sleep(2)
                    if 'action' in key:
                        # action procedure
                        if 'click' in key:
                            print('action click')
                            try:
                                for el in current_el:
                                    self.driver.execute_script('arguments[0].click()',el)
                                    time.sleep(2)
                            except EXCPT.ElementClickInterceptedException:
                                print('element not clickable:',key)
                            except:
                                print('Unknown error for element:',key)
                        elif 'download' in key:
                            print('downloading...')
                    elif '__attr__' in key:
                        attr = key.split('__')[-1]
                        key_name = key.split('__')[0]
                        print('get item by attribute:',attr)
                        el_list = []
                        for el in current_el:
                            el_list.append(el.get_attribute(attr))
                        current_items.update({key_name: el_list})
                        print("item found.",key_name,". size elements:",len(current_items[key_name]))
                    else:
                        current_items.update({key: el.text for el in current_el if el.text != ''})
                        # print("item found.",key,":",current_items[key])
                except EXCPT.TimeoutException:
                    print('get_items: Timeout')
            else:
                print("nested",key)
                self.get_items(current_page_el,value,current_items)

    def save_to_file(self,
        content,
        location=str(Path(__file__).resolve().parent),
        filename=datetime.datetime.now().strftime('%d %m %Y %H %M %S')+".txt",
        ):
       
        separator = ''
        if sys.platform == 'linux':
            separator = "/"
        else:
            separator = "\\"
        
        f = location+separator+filename
        with open(f,'w') as file:
            file.write(content)
