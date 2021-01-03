from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.keys import Keys


scenarios('../features/pokedex.feature')


@given('the pokedex page')
def pokedex_page(browser):
    browser.get('https://pokedex.org/')


@when('the user searches for "<text>"')
def search_pokemon_name(browser, text):
    search_input = browser.find_element_by_id('monsters-search-bar')
    search_input.send_keys(text, Keys.ENTER)


@then('the "<pokemon>" information is shown')
def results_have_one(browser, pokemon):
    results = browser.find_elements_by_id('monsters-list')

    assert len(results) > 0
    assert pokemon in results[0].text
