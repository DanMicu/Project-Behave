from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RadioButtonPage(BasePage):

    URL = "https://formy-project.herokuapp.com/radiobutton"

    def radio_button_link(self):
        radio_button_selector = self.driver.find_element(By.XPATH, "/html/body/div/div/li[12]/a")
        return radio_button_selector.click()

    def select_radio_button_two(self):
        radio_button2 = (By.CSS_SELECTOR, "input[value='option2']")
        return self.driver.find_element(*radio_button2)


