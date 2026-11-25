from behave import given,when,then  # type: ignore[reportMissingImports]
from playwright.sync_api import sync_playwright

def close_popup_if_present(context):
  close_btn = context.page.locator(
      "button.close, .modal .btn-close, [aria-label='Close']"
  )
  if close_btn.count() > 0 and close_btn.first.is_visible():
    close_btn.first.click()


def scroll_to_table(context):
  context.page.locator("table").first.scroll_into_view_if_needed()


@given("I navigate to pagination table page")
def step_navigate_pagination_table(context):
  context.page.goto("https://practice.expandtesting.com/dynamic-pagination-table")
  close_popup_if_present(context)


@when("I select 5 entries from dropdown")
def step_select_5_entries(context):
  scroll_to_table(context)
  context.page.select_option('select[name="example_length"]', "5")
  context.page.wait_for_timeout(3000)


@when("I select 10 entries from dropdown")
def step_select_10_entries(context):
  scroll_to_table(context)
  context.page.select_option('select[name="example_length"]', "10")
  context.page.wait_for_timeout(3000)


@then("I should see 5 rows in the table")
def step_see_5_rows(context):
  rows = context.page.locator("table tbody tr")
  row_count = rows.count()
  print(f"Row count: {row_count}")
  assert row_count == 5, f"Expected 5 rows, but got {row_count}"
  context.page.wait_for_timeout(3000)

@then("I should see entries text updated correctly")
def step_entries_text_updated(context):
  info_text = context.page.locator("#example_info").text_content() or ""
  print(f"Entries text: {info_text}")
  context.page.wait_for_timeout(3000)
  assert "1 to 5" in info_text, f"Expected '1 to 5' in '{info_text}'"

@when("I sort Student Name column")
def step_sort_student_name(context):
  scroll_to_table(context)
  context.page.get_by_text("Student Name").click()
  context.page.wait_for_timeout(3000)


@then("the column should be sorted correctly")
def step_column_sorted_correctly(context):
  values = context.page.locator(
      "table tbody tr td:nth-child(1)"
  ).all_text_contents()
  print(f"Before Click: {values}")

  asc = sorted(values)
  desc = sorted(values, reverse=True)

  if values == asc:
    print("Already Ascending")
    context.page.get_by_text("Student Name").click()
    new_values = context.page.locator(
        "table tbody tr td:nth-child(1)"
    ).all_text_contents()
    print(f"After Click (Descending): {new_values}")
    assert new_values == desc, f"Expected {desc}, got {new_values}"
  else:
    print("Currently Descending")
    context.page.get_by_text("Student Name").click()
    new_values = context.page.locator(
        "table tbody tr td:nth-child(1)"
    ).all_text_contents()
    print(f"After Click (Ascending): {new_values}")
    assert new_values == asc, f"Expected {asc}, got {new_values}"


@when("I search for Bob Williams")
def step_search_bob_williams(context):
  context.page.locator('input[type="search"]').fill("Bob")
  context.page.wait_for_timeout(3000)


@then("only matching records should be displayed")
def step_only_matching_records(context):
  rows = context.page.locator("table tbody tr")
  count = rows.count()

  for i in range(count):
    text = rows.nth(i).text_content() or ""
    assert (
        "Bob Williams" in text
    ), f"Expected 'Bob Williams' in row {i}, got '{text}'"


@then("pagination buttons should be disabled")
def step_pagination_buttons_disabled(context):
  next_class = context.page.locator("#example_next").get_attribute("class") or ""
  prev_class = context.page.locator("#example_previous").get_attribute("class") or ""
  assert "disabled" in next_class, f"Expected Next button to be disabled, got class: '{next_class}'"
  assert "disabled" in prev_class, f"Expected Previous button to be disabled, got class: '{prev_class}'"