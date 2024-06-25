from testpage import OperationsHelper
import yaml, time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
password = testdata["password"]

def test_step1(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(name)
    testpage.enter_pass(password)
    testpage.click_login_button()
    time.sleep(2)

def test_step2(browser):
    testpage = OperationsHelper(browser)
    testpage.click_about_us()
    time.sleep(2)
    font_size = testpage.get_about_us_size()
    assert font_size == '32px'
