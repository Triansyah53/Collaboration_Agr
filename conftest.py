import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Choptions
from selenium.webdriver.firefox.options import Options as Ffoptions


@pytest.fixture(scope="class")
def init_driver(request):
    """
        Initializes a WebDriver for automated testing with supported browsers.

        This fixture sets up and tears down the WebDriver based on the specified browser
        environment variable. If the browser is not supported or not specified, an Exception
        will be raised.

        Supported browsers: 'ch' (Chrome), 'ff' (Firefox), 'headlesschrome', 'headlessfirefox'.

        Usage:
            @pytest.mark.usefixtures('init_driver')
            def test_example():
                # Your test code here

        Args:
            request: pytest request object

        Yields:
            WebDriver: The initialized WebDriver instance

        Raises:
            Exception: If the specified browser is not supported or not specified.

        """
    supported_browsers = ['ch', 'ff', 'headlesschrome', 'headlessfirefox']
    browser = os.environ.get('BROWSER', None)
    if browser is None:
        raise Exception("The Environment variable 'BROWSER' must be set.")
    # browser=browser.lower()

    if browser not in supported_browsers:
        raise Exception(
            f"Provided browser {browser} is not one of the supported browsers. Supported browsers are: {', '.join(supported_browsers)}")

    if browser in ('ch'):
        chrome_options = Choptions()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = Choptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('headlessfirefox'):
        ff_options = Ffoptions()
        ff_options.add_argument('--disable-gpu')
        ff_options.add_argument('--headless')
        driver = webdriver.Firefox(options=ff_options)
    else:
        raise Exception("Unknown browser specified")

    request.cls.driver = driver
    yield
    driver.quit()
