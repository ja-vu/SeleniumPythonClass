from selenium import webdriver


class RunFFTests():
    def testMethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox()
        #executable_path="C:\\Workspace\\libs\\geckodriver-v0.24.0-win64\\geckodriver.exe"
        driver.get("http://www.letskodeit.com")


ff = RunFFTests()
ff.testMethod()