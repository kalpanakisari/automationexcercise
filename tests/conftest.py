import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(autouse=True, scope="class")
#@pytest.fixture(scope="class",autouse=True)
def setup(request):
    global driver #global variable declaration
    browser_name=request.config.getoption("--browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service_obj = Service("C:/Kalpana/Selenium with Python/Gitpython/NewFramework/driversfolder/chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=service_obj)
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.maximize_window()
        request.cls.driver = driver

    elif browser_name == "firefox":
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().download_and_install())
        service_obj = Service("C:/Kalpana/Selenium with Python/Gitpython/NewFramework/driversfolder/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        #driver.get("https://google.com")
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.maximize_window()
        request.cls.driver = driver

    elif browser_name == "edge":
        print("edge driver starts")
        #driver = webdriver.Edge(executable_path=EdgeDriverManager().install())
        service_obj = Service("C:/Kalpana/Selenium with Python/Gitpython/NewFramework/driversfolder/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.maximize_window()
        request.cls.driver = driver


    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()  # geeting the result of the testcase
    extra = getattr(report, 'extra', [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail) :
            timestamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
            file_name = report.nodeid.replace("::", "_")+ timestamp+".png"

            _capture_screenshot(file_name)
            print(file_name)
            if file_name:
                html = ('<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"'
                        'onclick="window.open(this.src)" align="right"/></div>')% file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    #print('ji')
    driver.get_screenshot_as_file(name)

    #pytest --browser_name=chrome
    

