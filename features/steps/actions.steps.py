from behave import given,when,then  # type: ignore[reportMissingImports]
from playwright.sync_api import sync_playwright

@given("I navigate to the hover page")
def step_navigate_hover(context):
    context.page.goto("https://practice.expandtesting.com/hovers")

@given("I navigate to the context menu page")
def step_navigate_context_menu(context):
    context.page.goto("https://practice.expandtesting.com/context-menu")

@given("I navigate to the dropdown page")
def step_navigate_drop_down(context):
    context.page.goto("https://practice.expandtesting.com/dropdown")

@given("I navigate to the autocomplete page")
def step_navigate_autcomplete(context):
    context.page.goto("https://practice.expandtesting.com/autocomplete")


@when("I hover over user 1")
def step_hover_user1(context):
    context.page.get_by_test_id("img-user-1").hover()

@then("I should see the user name")
def step_see_user_name(context):
    heading=context.page.get_by_text("name: user1 View profile").text_content()
    assert "name: user1" in heading

@when("I right click on the box")
def step_right_click_box(context):
    context.page.once(
        "dialog",
        lambda dialog: (
        setattr(context,"alert_msg",dialog.message),
        dialog.accept()
        ),
    )
    context.page.locator("#hot-spot").click(button="right")

@then("I should see the context menu alert")
def step_see_context_menu_alert(context):
    assert "You selected a context menu" in context.alert_msg

@when("I select option from dropdown")
def step_select_dropdown(context):
    dropdown=context.page.locator("select").first
    dropdown.select_option(label="Option 1")
    

@then("option should be selected")
def step_option_selected(context):
    dropdown=context.page.locator("select").first
    assert dropdown.input_value()=="1"

@when("I type country name")
def step_type_country_name(context):
    country_input=context.page.locator("#country")
    country_input.fill("India")

@when("I select India from suggestion")
def step_select_india_suggestion(context):
    context.page.get_by_text("India").first.click()

@then("India should be selected")
def step_india_selected(context):
  assert context.page.locator("#country").input_value() == "India"