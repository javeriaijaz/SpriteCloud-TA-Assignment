import pytest
from selenium import webdriver
import chromedriver_autoinstaller
import ssl
from config import Config

ssl._create_default_https_context = ssl._create_unverified_context

# Automatically install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

@pytest.fixture(scope="function")
def setup():
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--verbose")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_html_report_title(report):
    """Customize the report title"""
    report.title = "Test Automation Results"

def pytest_html_results_table_header(cells):
    """Modify table headers to include Test Name, Steps, and Expected Result"""
    cells.insert(1, "<th>Test Name</th>")  # Rename test name header
    cells.insert(2, "<th>Steps</th>")
    cells.insert(3, "<th>Expected Result</th>")

def pytest_html_results_table_row(report, cells):
    """Modify table rows to format test names, include steps, and expected results"""
    metadata = getattr(report, "metadata", {})

    # Extract test function name
    full_test_name = report.nodeid.split("::")[-1]  # Extracts only the function name

    # Format the test name into a readable sentence
    formatted_test_name = (
        "Test " + full_test_name.replace("_", " ").title()  # Capitalize each word
    ).replace("Test Test ", "Test ")  # Avoid "Test Test" if function name starts with "test_"

    print(f"DEBUG: report.nodeid -> {report.nodeid}")  # Debugging line to check nodeid

    steps = "<br>".join(metadata.get("steps", ["No steps provided"]))
    expected = metadata.get("expected", "No expected result")

    # Insert formatted test name in a separate column
    cells.insert(1, f"<td>{formatted_test_name}</td>")
    cells.insert(2, f"<td>{steps}</td>")
    cells.insert(3, f"<td>{expected}</td>")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to extract metadata from test cases and attach it to the report object"""
    outcome = yield
    report = outcome.get_result()

    # Extract metadata from test case
    metadata = {}
    for marker in item.iter_markers(name="test_metadata"):
        metadata["steps"] = marker.kwargs.get("steps", [])
        metadata["expected"] = marker.kwargs.get("expected", "")

    report.metadata = metadata  # Attach metadata to the report

