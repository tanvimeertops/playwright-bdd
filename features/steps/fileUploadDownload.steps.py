from behave import given,when,then  # type: ignore[reportMissingImports]
from playwright.sync_api import sync_playwright

@given("I navigate to upload page")
def step_navigate_to_upload_page(context):
    context.page.goto("https://practice.expandtesting.com/upload")

@when("I upload a file")
def step_upload_file(context):
    context.page.set_input_files("#fileInput","D:/N+/OSI.txt")

@when("I click on upload button")
def step_click_upload_button(context):
    context.page.locator("#fileSubmit").click()


@then("File should be uploaded successfully")
def step_file_uploaded_successfully(context):
    heading=context.page.locator("h1").text_content()
    assert "File Uploaded!" in heading        

@then("Uploaded file name should be displayed")
def step_uploaded_file_name_displayed(context):
    uploaded_txt=context.page.locator("#uploaded-files").text_content()
    assert "OSI" in uploaded_txt 