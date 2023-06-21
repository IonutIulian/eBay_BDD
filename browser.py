from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


class Browser():
    driver  = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.delete_all_cookies()
        self.driver.quit()