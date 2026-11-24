from behave import given,when,then  # type: ignore[reportMissingImports]
from playwright.sync_api import sync_playwright
import time
@given("I navigate to the windows page")
def step_navigate_iframe(context):
    context.page.goto("https://practice.expandtesting.com/windows")

@when('I click on the "Click Here" link')
def step_click_link(context):
    context.page.get_by_text("Click Here").click()
    context.new_page=context.page.context.pages[-1]

@then("I should switch to new window and validate content")
def step_switch_new_window(context):
    context.new_page.wait_for_load_state()
    text=context.page.locator("h1").text_content()
    print(f"child page text : {text}")
    assert "new window" in text
    time.sleep(5)

@then("I close the child window and switch back to parent")
def step_close_window(context):
    context.new_page.close()
    context.page.bring_to_front()
    assert "/windows" in context.page.url