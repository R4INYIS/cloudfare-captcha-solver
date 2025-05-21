import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#? Constants

URL: str = "https://2captcha.com/es/demo/cloudflare-turnstile"  # Demo page with Cloudflare Turnstile


#* Driver configuration
driver = uc.Chrome(log_level=0)               # Start undetected Chrome driver
driver.get(URL)                               # Open the demo page
wait = WebDriverWait(driver, 10)              # Explicit wait for elements

#! Captcha solving
outer_host = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#cf-turnstile > div')))  # Wait till the shadow host is present (normally ID cf-turnstile)
outer_root = outer_host.shadow_root  # Get the shadow root of the outer host
iframe = outer_root.find_element(By.CSS_SELECTOR, 'iframe')  # Find the iframe inside the shadow root
driver.switch_to.frame(iframe)  # Switch to the iframe

inner_host = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))  # Wait till the inner host is present (normally in the body)
inner_root = inner_host.shadow_root  # Get the shadow root of the inner host
inner_input = inner_root.find_element(By.CSS_SELECTOR, 'input')  # Find the input inside the shadow root
driver.execute_script("arguments[0].click();", inner_input)  # Click the input element with JavaScript to bypass the clickjacking protection


sleep(10)

