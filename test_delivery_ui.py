import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize(
    ("area", "amount", "expected"),
    [
        ("city", "5000", "Стоимость доставки: 1000 ₸."),
        ("city", "9999", "Стоимость доставки: 1000 ₸."),
        ("city", "10000", "Доставка бесплатная."),
        ("city", "15000", "Доставка бесплатная."),
        ("region", "5000", "Стоимость доставки: 2000 ₸."),
        ("region", "9999", "Стоимость доставки: 2000 ₸."),
        ("region", "10000", "Доставка бесплатная."),
        ("region", "15000", "Доставка бесплатная."),
    ],
)
def test_delivery_calculation(page, delivery_url, area, amount, expected):
    page.goto(delivery_url)
    page.locator("#area").select_option(area)
    page.locator("#amount").fill(amount)
    page.locator("#calculate").click()
    expect(page.locator("#result")).to_have_text(expected)

def test_page_has_title(page, delivery_url):
    page.goto(delivery_url)
    expect(page).to_have_title("Расчёт доставки")

def test_calculate_button_is_visible(page, delivery_url):
    page.goto(delivery_url)
    expect(page.locator("#calculate")).to_be_visible()

def test_invalid_negative_amount(page, delivery_url):
    page.goto(delivery_url)
    page.locator("#amount").fill("-1")
    page.locator("#calculate").click()
    expect(page.locator("#result")).to_have_text("Введите корректную сумму заказа.")
    expect(page.locator("#result")).to_have_attribute("data-price", "invalid")

def test_zero_amount_city(page, delivery_url):
    page.goto(delivery_url)
    page.locator("#area").select_option("city")
    page.locator("#amount").fill("0")
    page.locator("#calculate").click()
    expect(page.locator("#result")).to_have_text("Стоимость доставки: 1000 ₸.")
