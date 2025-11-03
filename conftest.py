import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", 
        action="store", 
        default="chrome",
        help="Choose browser: chrome or firefox"
    )
    parser.addoption(
        "--language", 
        action="store", 
        default="en",
        help="Choose language: en, ru, fr, es, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    print(f"\nStarting {browser_name} browser with language: {user_language}")
    
    if browser_name == "chrome":
        # Chrome настройки языка
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        
    elif browser_name == "firefox":
        # Firefox настройки языка
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nQuit browser..")
    browser.quit()