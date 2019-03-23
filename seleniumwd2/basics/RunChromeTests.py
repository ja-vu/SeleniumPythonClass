from selenium import webdriver
import os


class RunChromeTests():
    def test(self):
        driverLocation = "C:\\Workspace\\libs\\chromedriver_win32_73\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation       # **** VERY IMPORTANT ****

        # Initiate the driver instance
        driver = webdriver.Chrome(driverLocation)

        driver.get("http://www.letskodeit.com")


chrometest = RunChromeTests()
chrometest.test()