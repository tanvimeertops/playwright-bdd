from behave import given,when,then  # type: ignore[reportMissingImports]
from playwright.sync_api import sync_playwright

@given("I navigate to drag and drop page")
def step_drag_drop(context):
    context.page.goto("https://practice.expandtesting.com/drag-and-drop")

@given("I navigate to drag drop circles page")
def step_drag_drop(context):
    context.page.goto("https://practice.expandtesting.com/drag-and-drop-circles")

@when("I drag box A to box B")  
def step_drag_drop(context):
    source=context.page.locator("#column-a")
    destination=context.page.locator("#column-b")
    source.drag_to(destination)

@then("Box A header should change to B")
def step_box_a_header_changed(context):
    header = context.page.locator("#column-a header").inner_text()
    assert "B" in header

@when("I drag red circle into target")
def step_drag_red_circle(context):
    source=context.page.locator(".red")
    target=context.page.locator("#target")
    source.drag_to(target)

@when("I drag green circle into target")
def step_drag_red_circle(context):
    source=context.page.locator(".green")
    target=context.page.locator("#target")
    source.drag_to(target)

@when("I drag blue circle into target")
def step_drag_red_circle(context):
    source=context.page.locator(".blue")
    target=context.page.locator("#target")
    source.drag_to(target)
@then("All circles should be inside target box")
def step_circle_inside_target_box(context):
    assert context.page.locator("#target .red").is_visible()
    assert context.page.locator("#target .green").is_visible()
    assert context.page.locator("#target .blue").is_visible()