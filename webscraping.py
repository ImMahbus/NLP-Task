from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os

dirname = os.path.dirname(__file__)
PATH = os.path.join(dirname, 'env\chromedriver.exe')
driver = webdriver.Chrome(PATH)

driver.get("https://www.pathologyoutlines.com/")

results = driver.find_element(
    By.CLASS_NAME, 'home_content.clearfix').find_elements(By.TAG_NAME, "a")

ans = {}


wait = WebDriverWait(driver, 30)
for i in range(0, len(results)):
    wait.until(EC.visibility_of_all_elements_located(
        (By.CLASS_NAME, 'home_content.clearfix')))
    link_test = driver.find_element(
        By.CLASS_NAME, 'home_content.clearfix').find_elements(By.TAG_NAME, "a")[i].text
    driver.find_element(
        By.CLASS_NAME, 'home_content.clearfix').find_elements(By.TAG_NAME, "a")[i].click()
    try:
        wait.until(EC.visibility_of_all_elements_located(
        (By.CLASS_NAME, 'toc_subsection.toc_links')))
    except:
        driver.back()
        continue
    values = driver.find_elements(
        By.CLASS_NAME, 'toc_subsection.toc_links')
    f_value = ""
    for value in values:
        f_value+=value.text
    ans[link_test] = f_value
    print(link_test)
    driver.back()
    

json.dump(ans, open('organ.json','w'))

# df = pd.DataFrame.from_dict(ans)

# df.to_csv('organ.csv')
    
# driver.quit()
