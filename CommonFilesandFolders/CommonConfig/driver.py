from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



def go_to(url, browser=None):
    if not browser:
        # create instance of Chrome driver the browser type is not specified
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser.lower() == 'firefox':
        # create instance of the Gecko driver if browser is mentioned as firefox
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        # raise exception if any other browser name is mentioned
        raise Exception("The browser type '{}' is not supported".format(browser))

    url = url.strip()
    driver.get(url)



    return driver
