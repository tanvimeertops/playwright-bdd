from behave import given, when


@given("user is on SauceDemo login page")
def step_on_saucedemo_login_page(context):
  context.page.goto("https://www.saucedemo.com/")


@when('user enters "{username}" and "{password}"')
def step_enter_credentials(context, username, password):
  context.page.locator("#user-name").fill(username)
  context.page.locator("#password").fill(password)


@when("user clicks on login button")
def step_click_login_button(context):
  context.page.locator("#login-button").click()