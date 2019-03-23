from selenium import webdriver
import os


class RunIETests():
    def test(self):
        driverLocation = "C:\\Workspace\\libs\\IEDriverServer_x64_3.14.0\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation       # **** VERY IMPORTANT ****

        # Initiate the driver instance
        driver = webdriver.Ie(driverLocation)

        driver.get("http://www.letskodeit.com")


chrometest = RunIETests()
chrometest.test()