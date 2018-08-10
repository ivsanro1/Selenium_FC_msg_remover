from selenium import webdriver
import time
import numpy as np
import sys
import getpass

_USER = input("Username:\n")
_PASS = getpass.getpass()

browser = webdriver.Firefox()

# Login
browser.get("https://www.forocoches.com/foro/forumdisplay.php?f=2")

el = browser.find_element_by_id('navbar_username')
el.clear()
el.send_keys(_USER)

el = browser.find_element_by_id('navbar_password')
el.clear()
el.send_keys(_PASS)

browser.find_element_by_xpath("//input[@value='Acceder']").click()


# Message deletion loop
while(True):
    try:
        time.sleep(3)

        link_to_profile = browser.find_element_by_xpath("//a[contains(@href,'member.php?u=')]")
        link_to_profile.click()

        stats_tab = browser.find_element_by_id('stats_tab')
        stats_tab.click()

        link_to_usr_msgs = browser.find_elements_by_xpath("//a[contains(@href,'do=finduser')]")[0]
        link_to_usr_msgs.click()

        links_to_messages = browser.find_elements_by_xpath("//a[contains(@href,'highlight=#')]")
        chosen_message = np.random.choice(len(links_to_messages))
        links_to_messages[chosen_message].click()

        time.sleep(1)
        browser.find_element_by_xpath('//*[@title="Editar/Borrar Mensaje"]').click()
        time.sleep(1)

        browser.find_element_by_id('vB_Editor_QE_1_delete').click()

        browser.find_element_by_id('rb_del_soft').click()

        browser.find_element_by_id('quickedit_dodelete').click()
        time.sleep(1)


    except:
        pass