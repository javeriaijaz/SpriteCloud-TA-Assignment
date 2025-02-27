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
Tests are fully automated and executed via **GitHub Actions**. No manual setup is required.

### ▶️ Running Tests via GitHub Actions:
🎯 GitHub Actions CI/CD
This project runs UI & API tests automatically using GitHub Actions.

🔹 How to Trigger Tests Manually
- Go to GitHub → Actions
- Select UI & API Test Automation Workflow
- Click Run workflow

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
AI assistance was used in structuring this **README.md** file and refining the test scenarios for clarity and completeness. The actual implementation was manually written and reviewed to ensure accuracy and correctness.

---

### 👨‍💻 Author
Developed by **[Your Name]** | QA Engineer 🚀
