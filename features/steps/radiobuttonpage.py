import time

from behave import *


@When('I click the Radio Button link')
def step_impl(context):
    context.radiobutton_page.radio_button_link()


@When('I am redirected to the Radio Button page')
def step_impl(context):
    expected_url = "https://formy-project.herokuapp.com/radiobutton"
    assert context.browser.get_current_url() == expected_url


@When('I click Radio button 2')
def step_impl(context):
    radio2 = context.radiobutton_page.select_radio_button_two()
    radio2.click()
    time.sleep(2)


@then('Radio button 2 is selected')
def step_impl(context):
    assert context.radiobutton_page.select_radio_button_two().is_selected()



