import time
import re

from selenium.common import exceptions as EXCPT

from rumah123.settings import *
from rumah123.items import Item
from HomeScrapperSelenium.Scrapper import Scrapper, DriverType, STATUS_TYPE, PROPERTY_TYPE

START_URL = HOME_PAGE
BTN_MORE = 'div.relative.ui-molecules-toggle__selector.ui-molecules-toggle__selector--bottom'
HOME_DESCRIPTION = 'p.ui-atomic-text.ui-atomic-text--styling-default.ui-atomic-text--typeface-primary'

class Rumah123Scrapper(Scrapper):    
    def __init__(self, driver, url):
        Scrapper.__init__(self,driver,url)

    def get_information(self):
        information = {}
        current_elements = self.parse_css("div.flex.ui-molecules-tab-list-r123-detail > div div")
        
        for el in current_elements:
            el_child_label = self.get_element_child(el,'css','p[class*="ui-molecules-tab-list-r123-detail__attribute--label"]')
            el_child_value = self.get_element_child(el,'css','p[class*="ui-molecules-tab-list-r123-detail__attribute--value"]')

            if 'ID' in el_child_label.text:
                information.update({"ID": el_child_value.text})
            elif 'Tipe' in el_child_label.text:
                information.update({"property_type": el_child_value.text})
            elif 'Perabot' in el_child_label.text:
                information.update({"furniture": el_child_value.text})
            elif 'Kondisi' in el_child_label.text:
                information.update({"condition": el_child_value.text})
            elif 'Lantai' in el_child_label.text:
                information.update({"Lantai": el_child_value.text})
            elif 'Sertifikat' in el_child_label.text:
                information.update({"certificate": el_child_value.text})
            elif 'Daya' in el_child_label.text:
                information.update({"electricity": el_child_value.text})
            elif 'Tayang' in el_child_label.text:
                information.update({"publish_date": el_child_value.text})
        
        return information

    def get_by_location(self, location=''):
        print("Rumah123Scrapper -> get_by_location")
        current_elements = self.parse_css(BY_LOCATION_CSS_MORE_BTN)
        for element in current_elements:
            if 'banyak' in element.text:
                self.driver.execute_script('arguments[0].click()',element)

        current_elements = self.parse_css(BY_LOCATION_CSS)
        rumah_list = []

        for element in current_elements:
            cur_loc = element.get_attribute('title')
            cur_href = element.get_attribute('href')

            if location in cur_loc:                
                self.driver.execute_script('window.open(arguments[0],"_blank")',cur_href)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.execute_script('window.scrollTo(0,300)')
                
                print("current title:",self.driver.title)
                
                list_rumah = self.parse_css(BY_LOCATION_CSS_LIST)
                for rumah in list_rumah:
                    rumah_detail_el = self.get_element_child(
                        rumah, find_by='tag', token='a')
                    rumah_detail_href = rumah_detail_el.get_attribute('href')
                    
                    if 'baru' in rumah_detail_href:
                        continue
                    
                    self.driver.execute_script(
                        'window.open(arguments[0],"_blank")', rumah_detail_href)
                    self.driver.switch_to.window(
                        self.driver.window_handles[-1])

                    time.sleep(5)
                    print("rumah current title:", self.driver.title)

                    property_page = self.parse_css(
                        "div.ui-property-page__description.relative.ui-col-12")
                    btn_page_more = self.get_element_child(
                        property_page[0], find_by='css', token=BTN_MORE)
                    self.driver.execute_script(
                        'arguments[0].click()', btn_page_more)
                    description = self.get_element_child(
                        property_page[0], find_by='css', token=HOME_DESCRIPTION)
                    rumah_items = {"description": description.text}
                    
                    property_info = self.parse_css(
                        "div.ui-property-page__feature.relative.ui-col-12")
                    btn_page_more = self.get_element_child(
                        property_info[0], find_by='css', token=BTN_MORE)
                    self.driver.execute_script(
                        'arguments[0].click()', btn_page_more)

                    self.get_items(
                        rumah_detail_el, PROPERTY_BY_CSS_SELECTORS, rumah_items)
                    rumah_items.update(self.get_information())
                    
                    if 'agent_contact' not in rumah_items.keys():
                        agent_contact = self.parse_css('div.ui-organism-listing-inquiry-r123__container-wrapper > div > div > button > span.ui-atomic-button--children > div')
                        try:
                            rumah_items.update({"agent_contact": agent_contact[0].text})
                        except:
                            print("rumah agent contact not found")

                    items = self.conditioner(rumah_items)

                    print("rumah", rumah_items['property_name'])
                    print("posting to database")
                    try:
                        self.post_data(items,'http://127.0.0.1:8000/api/property/create/','miftah:123456')
                        print("success posting to database")
                    except:
                        print("fail posting to database")

                    self.driver.close()
                    self.driver.switch_to.window(
                        self.driver.window_handles[-1])
                exit()  # debuging

                self.driver.close()
                self.driver.switch_to.window(self.home_tab_handle)
                # exit() #debuging
                break #debugging
                time.sleep(2)

    def get_populars(self):
        current_elements = self.parse_css(POPULAR_CSS)
        popular_items = []

        for element in current_elements:
            try:
                self.driver.execute_script('window.open(arguments[0],"_blank")',element.get_attribute('href'))
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.execute_script('window.scrollTo(0,300)')

                print("current title:",self.driver.title)
                
                items_base = {}
                self.get_items(element,NEW_PROPERTY_CSS_SELECTORS,items_base)
                tabs = self.parse_css(NEW_PROPERTY_DETAIL_CSS)
                
                for tab in tabs:
                    print("action tab click debug:",tab.text)
                    
                    self.driver.execute_script('arguments[0].click()',tab)
                    time.sleep(1)
                    populars = self.parse_css(NEW_PROPERTY_DETAIL_OPEN_DIALOG_CSS)
                    for popular in populars:
                        self.driver.execute_script('arguments[0].click()',popular)
                        self.get_items(element,NEW_PROPERTY_DETAIL_SELECTORS,items_base)
                        items = self.conditioner(items_base)
                        popular_items.append(items)
                        # items_json = self.toJson(items)
                        # print(items_json)
            except EXCPT.ElementClickInterceptedException:
                print('Element is not clickable')
                continue
            except EXCPT.StaleElementReferenceException:
                print('Element is stale')
                continue
            
            self.driver.close()
            self.driver.switch_to.window(self.home_tab_handle)
            # exit() #debuging
            break #debugging
            time.sleep(2)
        
        return popular_items

    def conditioner(self,items):
        new_items = items.copy()
        new_items['property_name'] = items['property_name']+" - "+items['name']
        new_items['source_id'] = 1

        try:
            property_type = new_items['property_type'].lower()
            if 'apartem' in property_type:
                property_type = 'apartement'
            new_items['property_type'] = PROPERTY_TYPE[property_type]
        except KeyError:
            print("conditioner method. Error: Invalid property type")
        except:
            print("conditioner method. Error: Unknown property type error")

        try:
            status = new_items['status'].lower()
            if 'jual' in status:
                status = "jual"
            elif 'sewa' in status:
                status = "sewa"
            elif 'jual' in status and 'sewa' in status:
                status = "-"
            new_items['status'] = STATUS_TYPE[status]
        except KeyError:
            print("conditioner method. Error: Invalid status type")
        except:
            print("conditioner method. Error: Unknown status type error")

        LB = re.search(r'\d+',new_items['LB']).group()
        LT = re.search(r'\d+',new_items['LT']).group()
        new_items['LT'] = LT
        new_items['LB'] = LB

        new_items['developer'] = {'name': new_items['developer_name'],'contact': new_items['developer_contact']}
        new_items['agent'] = [{'name': new_items['agent_name'],'contact': new_items['agent_contact']}]

        del new_items['developer_name']
        del new_items['developer_contact']
        del new_items['agent_name']
        del new_items['agent_contact']

        '''sementara hapus dulu karena belum ada di database'''
        try:
            del new_items['electricity']
        except:
            print('no item electricity')
        try:
            del new_items['ID']
        except:
            print('no item ID')
        try:
            del new_items['condition']
        except:
            print('no item condition')
        try:
            del new_items['condition']
        except:
            print('no item condition')

        images_list = [{'url': image} for image in new_items['images']]
        new_items['images'] = images_list

        return new_items

    def get_recommends(self):
        current_elements = self.parse_css(RECOMMEND_CSS)

        for element in current_elements:
            try:
                element.click()
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                time.sleep(2)
                self.driver.execute_script('window.scrollTo(0,300)')
                print("current title:",self.driver.title)
                items = self.get_items(element,NEW_PROPERTY_CSS_SELECTORS)
                print(items)
            except EXCPT.ElementClickInterceptedException:
                print('Element is not clickable')
                continue
            except EXCPT.StaleElementReferenceException:
                print('Element is stale')
                continue
            
            self.driver.switch_to.window(self.home_tab_handle)
            time.sleep(2)

if __name__ == '__main__':
    print("init main rumah123")
