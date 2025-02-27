# 🎯 spriteCloud TA Assignment 2025

## 📜 Table of Contents
- [🔍 Overview](#overview)
- [🛠 Technologies Used](#technologies-used)
- [📝 Test Scenarios](#test-scenarios)
  - [🖥 UI Tests](#ui-tests)
  - [🔌 API Tests](#api-tests)
- [🚀 Execution](#execution)
- [📊 Reports](#reports)
- [🤔 Assumptions](#assumptions)
- [🤖 AI Usage Disclosure](#ai-usage-disclosure)

---

## 🔍 Overview
This repository contains the implementation of UI and API automation tests for the **spriteCloud TA Assignment 2025**. The UI tests are implemented using **Selenium** with **pytest**, and the API tests utilize **requests** with **pytest**. 

The objectives of this automation suite are:
- ✅ Perform UI testing on [SauceDemo](https://www.saucedemo.com/).
- ✅ Validate API functionality of [ReqRes](https://reqres.in/).
- ✅ Provide test reports for validation.
- ✅ Fully automated execution using **GitHub Workflows**.


---

## 📂 Project Structure
```
📦 SpriteCloud-TA-Assignment
├── 📂 api_tests                # API Automation Tests
│   ├── 📂 tests                # API test cases
│   │   ├── test_auth.py        # Tests for authentication
│   │   ├── test_negative.py    # Negative test cases
│   │   ├── test_performance.py # Performance tests
│   │   ├── test_users.py       # User-related tests
│   ├── 📂 utils                # Utilities for API automation
│   │   ├── __init__.py
│   │   ├── api_client.py       # API client for making requests
│   │   ├── schemas.py          # JSON schema validation
│
├── 📂 pages                    # Page Object Model (POM) for UI tests
│   ├── base_page.py            # Base class for all pages
│   ├── cart_page.py            # Page object for cart actions
│   ├── checkout_page.py        # Page object for checkout process
│   ├── inventory_page.py       # Page object for inventory (products) page
│   ├── locators.py             # Centralized locators for UI elements
│   ├── login_page.py           # Page object for login functionality
│   ├── product_page.py         # Page object for product-related actions
│
├── 📂 ui_tests                 # UI Automation Tests
│   ├── test_checkout.py        # Test case for checkout functionality
│   ├── test_login.py           # Test case for login functionality
│   ├── test_sorting.py         # Test case for sorting functionality
│
├── conftest.py                 # Pytest configurations and fixtures
├── custom_style.css            # Custom styling for reports
├── pytest.ini                  # Pytest configuration file
├── README.md                   # Project documentation
├── requirements.txt            # List of dependencies
```



---

## 🛠 Technologies Used
- 🐍 **Python 3.x**
- 🌐 **Selenium** (for UI testing)
- 🧪 **pytest** (for test execution and reporting)
- 📡 **requests** (for API testing)
- 📜 **pytest-html** (for generating HTML reports)
- ⚙️ **GitHub Actions** (for CI/CD automation)
- 🖥 **webdriver-manager** (for managing browser drivers)

---

## 📝 Test Scenarios

### 🖥 UI Tests
The following UI test cases are automated for [SauceDemo](https://www.saucedemo.com/):

1. **🛒 Checkout Flow**: 
   - Add at least two items to the cart.
   - Proceed to checkout.
   - Validate that the final price is correct.
   
2. **🔀 Sorting Validation**:
   - Sort items from **Z to A**.
   - Validate that the sorting is correctly applied.
   
3. **🚫 Failed Login Validation**:
   - Attempt login with incorrect credentials.
   - Validate the error message.

### 🔌 API Tests
The following API test cases are automated for [ReqRes](https://reqres.in/):

1. **📂 Retrieve List of Users** (GET `/api/users`)
2. **🔑 Perform a Successful Login** (POST `/api/login`)
3. **✏️ Update User Information** (PUT `/api/users/2`)
4. **🗑 Delete a User** (DELETE `/api/users/2`)
5. **❌ Negative Scenarios:**
   - Invalid login attempt.
   - Requesting a non-existent user.
6. **⏳ Parameterized Delayed Request** (GET `/api/users?delay=3`)
   - Validate that response time is within the expected range.

---

## 🚀 Execution
Tests are fully automated and executed via **GitHub Actions**. No manual setup is required if you rely on CI/CD. However, if someone wants to run tests **locally**, follow these steps:

### 🏗 Running Tests Locally
1. **Clone the repository**
   ```sh
git clone https://github.com/yourname/spritecloud-ta-assignment-2025.git
cd spritecloud-ta-assignment-2025
```

2. **Set up a virtual environment (optional but recommended)**
   ```sh
python -m venv venv
source venv/bin/activate    # macOS/Linux
.\venv\Scripts\activate    # Windows
```

3. **Install dependencies**
   ```sh
pip install -r requirements.txt
```

4. **Run the tests**
   ```sh
pytest ui_tests/ --html=ui_report.html --self-contained-html
pytest api_tests/ --html=api_report.html --self-contained-html
```

### 🎯 GitHub Actions CI/CD
This project runs UI & API tests automatically using GitHub Actions. The workflow generates a report as an artifact, which can be downloaded from the GitHub Actions run page.

🔹 **How to Trigger Tests Manually**
- Go to GitHub → Actions
- Select **UI & API Test Automation Workflow**
- Click **Run workflow**
- Go to GitHub → Actions
- Select **UI & API Test Automation Workflow**
- Click **Run workflow**

---

## 📊 Reports
Test execution generates HTML reports for easy validation. The reports are available in the **GitHub Actions artifacts** after test execution.

---

## 🤔 Assumptions
- 🏗 UI selectors are stable and not frequently changing.
- 📜 API response structure remains consistent as per ReqRes documentation.
- 🛠 The GitHub environment has all necessary dependencies pre-installed.
- 🌍 Internet access is available for API requests and test execution.

---

## 🤖 AI Usage Disclosure
I used AI to help structure this README.md file, but the actual implementation was written and reviewed manually to ensure accuracy. I also got some help with setting up the GitHub workflow file.

---
