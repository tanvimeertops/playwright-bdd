from behave import given,when,then  # type: ignore[reportMissingImports]
from playwright.sync_api import sync_playwright

@given("I navigate to the dynamic table page")
def step_dynamic_table_page(context):
    context.page.goto(
      "https://practice.expandtesting.com/dynamic-table",
      wait_until="domcontentloaded",
  )


@when("I fetch CPU value for Chrome from the table")
def step_fetch_val_from_table(context):
    headers=(context.page.locator('//*[@id="core"]/div/div/div[2]/div/div[2]/table/thead/tr').all_inner_texts()[0].split())
    print(f"header {headers}")
    cpu_col_index=headers.index("CPU")
    rows=context.page.locator('//*[@id="core"]/div/div/div[2]/div/div[2]/table/tbody/tr')
    row_count=rows.count()
    cols=context.page.locator('//*[@id="core"]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td')
    col_count=cols.count()
    for i in range(row_count):
        row_cells = [c.strip() for c in rows.nth(i).locator("td").all_inner_texts()]
        if "Chrome" in row_cells:
            for j in range(col_count):
                data=(
                    rows.nth(i)
                        .locator("td")
                        .nth(j)
                        .text_content()
                        .strip()
                )
                if j==cpu_col_index:
                    context.cpu_value=data
                    print(f"Chrome CPU value: {context.cpu_value}")
                    break
            break
            

@when("I fetch CPU value from the label")
def step_fetch_value_from_label(context):
    label_text = context.page.locator("#chrome-cpu").text_content() 
    print(f"Label text: {label_text}")  #
    context.label_value = label_text.split(":")[1].strip()  
    print(f"Extracted label value: {context.label_value}")

@then("both values should match")
def step_match_val(context):
    assert (
      context.cpu_value == context.label_value
    ), f"Mismatch! Table: {context.cpu_value}, Label: {context.label_value}"  
    print("Validation passed")