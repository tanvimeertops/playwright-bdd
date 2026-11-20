from behave import given,when,then  # type: ignore[reportMissingImports]
from playwright.sync_api import sync_playwright

browser=None
page=None
playwright=None

@given("user is on saas login page")
def step_open_login_page(context):
    global browser,page,playwright
    playwright=sync_playwright().start()
    browser=playwright.chromium.launch(headless=False,slow_mo=1000)
    page=browser.new_page()

    page.goto("https://www.saucedemo.com/")


@when("user enters username")
def step_enter_username(context):
    page.locator('[data-test="username"]').fill('standard_user')

@when("user enters password")
def step_enter_password(context):
    page.locator('[data-test="password"]').fill('secret_sauce')

@when("user clicks login button")
def step_click_login(context):
    page.locator('[data-test="login-button"]').click()
    
@then("user should be logged in successfully")
def step_verify_login(context):
    assert page.url=="https://www.saucedemo.com/inventory.html"