#!/usr/bin/python 

import sys, signal, time, getpass, os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sig_handler(sig, frame) -> None: os.remove(os.path.join(os.getcwd(), 'qr.png')); sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

driver_options = Options()
driver_options.add_argument("--headless")
browser = webdriver.Firefox(options=driver_options)

url: str = "https://web.whatsapp.com/send?phone="

def main() -> None:
    start_time = time.time()
    if len(sys.argv) != 4: print("\t[?] usage:\n\t\t%s <phone number with country code> <number of messages> <message>" % (sys.argv[0]))
    else:
        browser.get("%s%d" % (url, int(sys.argv[1])))
    
        time.sleep(10)
        browser.save_screenshot('qr.png')
        os.system('kitten icat qr.png')
        a = getpass.getpass(prompt="\n[*] Type any key after scan the QR: ")
        
        try:
            WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.x12lumcd > div:nth-child(1) > div:nth-child(1)')))
        finally:
            time.sleep(10)
            print("\n[*] Starting attack\n")
            for i in range(int(sys.argv[2])):
                browser.find_element(By.CSS_SELECTOR, '.x12lumcd > div:nth-child(1) > div:nth-child(1)').send_keys(str(sys.argv[3]))
                browser.find_element(By.CSS_SELECTOR, 'button.x1c4vz4f').click()

        browser.quit()
        end_time = time.time()
        os.remove(os.path.join(os.getcwd(), 'qr.png'))
        print("\n[*] Process finished in: %d s\n" % ((end_time - start_time)))

if __name__ == '__main__':
    main()

