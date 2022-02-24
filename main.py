from selenium import webdriver

import time


NEW_PASSWORD = 'Tinhanhem12345@'

class openseaBot():
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_extension('metamask.crx')
        self.driver = webdriver.Chrome('./chromedriver', options=chrome_option)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def login_metamask(self):
        self.driver.find_element_by_xpath('//button[text()="Get Started"]').click()
        self.driver.find_element_by_xpath('//button[text()="Create a Wallet"]').click()
        self.driver.find_element_by_xpath('//button[text()="No Thanks"]').click()

        #fill password
        time.sleep(1)
        inputs = self.driver.find_elements_by_xpath('//input[@type="password"]')
        inputs[0].send_keys(NEW_PASSWORD)
        inputs[1].send_keys(NEW_PASSWORD)
        self.driver.find_element_by_css_selector('.first-time-flow__checkbox').click()
        self.driver.find_element_by_xpath('//button[text()="Create"]').click()

        time.sleep(5)
        self.driver.find_element_by_xpath('//button[text()="Next"]').click()

        time.sleep(1)
        self.driver.find_element_by_css_selector('.reveal-seed-phrase__secret').click()
        secretRecoveryPhrase = self.driver.find_element_by_css_selector('.reveal-seed-phrase__secret-words').text
        
        time.sleep(0.1)
        self.driver.find_element_by_xpath('//button[text()="Next"]').click()

        time.sleep(0.1)
        confirmSecret = self.driver.find_elements_by_css_selector('.confirm-seed-phrase__seed-word.confirm-seed-phrase__seed-word--sorted')
        
        #find the button that matches secret recovery
        for secretRecovery in secretRecoveryPhrase.split():
            for secret in confirmSecret:
                if secretRecovery == secret.text:
                    secret.click()
                    continue

        self.driver.find_element_by_xpath('//button[text()="Confirm"]').click()
        time.sleep(0.1)
        self.driver.find_element_by_xpath('//button[text()="All Done"]').click()
        time.sleep(0.1)
        self.driver.find_element_by_css_selector('.popover-header__button').click()

    def login_opensea(self):
        self.driver.get('https://opensea.io/')
        main_page = self. driver.current_window_handle 

        time.sleep(0.1)
        self.driver.find_element_by_xpath('//a[@href="/account"]').click()

        time.sleep(0.5)
        listWallet = self.driver.find_element_by_css_selector('.ConnectCompatibleWallet--wallet-list')
        itemsWallets = listWallet.find_elements_by_tag_name("li")
        itemsWallets[0].click()

        # find and check current handle then switch to handle open new login with metamask
        time.sleep(3)
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
        self.driver.switch_to.window(login_page)
        self.driver.find_element_by_xpath('//button[text()="Next"]').click()
        self.driver.find_element_by_xpath('//button[text()="Connect"]').click()
        self.driver.switch_to.window(main_page)

    def main(self):
        self.login_metamask()
        
        time.sleep(0.5)
        self.login_opensea()


opensea = openseaBot()
opensea.main()