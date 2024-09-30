from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

width = 1920
height = 1080

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.set_window_size(width, height)

# Login to website
driver.get("https://identity.infare.net/account/login?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dportal-web-prod%26redirect_uri%3Dhttps%253A%252F%252Fcustomerportal.infare.net%26response_type%3Dcode%26scope%3Doffline_access%2520openid%2520profile%2520email%2520infare%253Aaccount-id%2520infare%253Acity-code%2520infare%253Aimpersonation-id%2520portal-validation-api%26state%3D96be0fcade1a4a93bd964d160ea01a2c%26code_challenge%3DPc-3CJB7LDOrpeUJPV8l3nQVWYZ3U6YlR-Q7zhX1YNA%26code_challenge_method%3DS256%26response_mode%3Dquery")

username = driver.find_element(By.ID, "Username")
username.send_keys("liemjack@airasia.com")

password = driver.find_element(By.ID, "Password")
password.send_keys("qwertyuiop")

submit = driver.find_element(By.ID, "loginButton")
submit.click()
time.sleep(5)

# Navigate to overview
driver.get("https://customerportal.infare.net/overview")

# Handle pop up element
pop = WebDriverWait(driver, 20).until(
  EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div/div[2]/button"))
)
if pop.is_displayed():
  pop.click()
  time.sleep(10)

pharos = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div"))
)
if pharos.is_displayed():
  pharos.click()
  time.sleep(20)

view = WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.CLASS_NAME, "NavSideMenu__arrow"))
)
if view.is_displayed():
  view.click()
  time.sleep(10)

iframe = driver.find_element(By.CLASS_NAME, "Pharos__iframe")
driver.switch_to.frame(iframe)

route = WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-routes-page/div/pharos-trip-prices/div/div[1]/pharos-route-header/div[1]"))
)
route.click()
time.sleep(5)

routeSearch = driver.find_element(By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-routes-page/pharos-route-selector/pharos-route-search/div/div/input")
routeSearch.send_keys("cgkdps")

od = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-routes-page/pharos-route-selector/div/pharos-tabs/div/pharos-tab[1]/div/pharos-my-routes/div/div/pharos-my-list-routes/div/div/div/cdk-virtual-scroll-viewport/div[1]/div/div[2]"))
)
od.click()
time.sleep(5)

connection = WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-routes-page/pharos-filters-features/pharos-tabs/div/pharos-tab[1]/div/pharos-filter-settings/div/pharos-scroll-shadow/div/div/pharos-filter-setting-editor/div[1]/pharos-connections-filter/pharos-drop-down-menu/div"))
)
connection.click()
time.sleep(3)

connectionSelect = driver.find_element(By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-routes-page/pharos-filters-features/pharos-tabs/div/pharos-tab[1]/div/pharos-filter-settings/div/pharos-scroll-shadow/div/div/pharos-filter-setting-editor/div[1]/pharos-connections-filter/pharos-drop-down-menu/div/p-dropdown/div/p-overlay/div/div/div/div/ul/p-dropdownitem[1]/li")
connectionSelect.click()
time.sleep(3)

feature = driver.find_element(By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-routes-page/pharos-filters-features/pharos-tabs/div/ul/li[2]")
feature.click()
time.sleep(2)

exportData = driver.find_element(By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-routes-page/pharos-filters-features/pharos-tabs/div/pharos-tab[2]/div/pharos-features-panel/div[1]/pharos-button-feature-item[1]/div/div/pharos-button/button")
exportData.click()
time.sleep(2)

delimitter = WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-dialog/div/p-dialog/div/div/div[2]/pharos-export-data-dialog-content/div/div[3]/pharos-drop-down-menu/div/p-dropdown/div"))
)
delimitter.click()
time.sleep(1)

delimitterSelect = driver.find_element(By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-dialog/div/p-dialog/div/div/div[2]/pharos-export-data-dialog-content/div/div[3]/pharos-drop-down-menu/div/p-dropdown/div/p-overlay/div/div/div/div/ul/p-dropdownitem[3]")
delimitterSelect.click()
time.sleep(2)

exportBtn = driver.find_element(By.XPATH, "/html/body/pharos-root/pharos-app-shell/div/pharos-dialog/div/p-dialog/div/div/div[3]/p-footer/div/pharos-button/button")
exportBtn.click()

time.sleep(10)

driver.quit()