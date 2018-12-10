from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
driver.get('https://accounts.google.com/ServiceLogin?passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26next%3D%252Fuser%252Ftseries%26hl%3Den-GB&service=youtube&uilel=3&hl=en-GB')

# wait till User signsIn
while True:
    if driver.current_url=='https://www.youtube.com/user/tseries':
        break

print('User signed in')

# wait till T-Series YouTube channel loads
while not driver.execute_script('return document.readyState;'):
    pass

print('T-Series loaded')

subscribe_btn = driver.find_element_by_xpath('//*[@id="subscribe-button"]')
subscribe_btn.click()

print('Subscribed to T-Series')


