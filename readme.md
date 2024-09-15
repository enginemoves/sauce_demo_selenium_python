
```md
# Selenium Python E2E Automation Project

This project is an end-to-end (E2E) test automation suite for the [Sauce Demo website](https://www.saucedemo.com/) using **Selenium WebDriver** in Python. The test suite covers user authentication, product selection, and the checkout process.

## Project Structure

```bash
.
├── data_elements/
│   ├── __init__.py
│   └── elements.py          # Contains element locators for the login, product, and checkout pages
├── e2e/
│   └── sauce_demo.py        # The main script that executes the test cases
├── pageObjects/
│   └── sauceDemo.py         # Contains actions to interact with the SauceDemo page (POM-based structure)
└── resource/
│    └── test_script.py       # The raw script where the tests are first written
└── requirements.txt

```

### 1. `data_elements/elements.py`

This file contains the element locators, organized into classes based on the pages and actions:

- **LoginPageElements**: Locators for login and logout actions.
- **productElements**: Locators for product page elements, such as sorting, selecting products, and product descriptions.
- **addProductToCart**: Contains locators to add specific products to the cart.
- **removeProduct**: Locators to remove products from the cart.
- **checkOut**: Locators for filling out the checkout form and completing the purchase.

### Example:

```python
class LoginPageElements:
    usernameField = "input#user-name"
    passwordField = "input#password"
    loginButton = "input#login-button"
    standardUser = "standard_user"
    lockedOutUser = "locked_out_user"
    problemUser = "problem_user"
    glitchUser = "performance_glitch_user"
    errorUser = "error_user"
    visualUser = "visual_user"
    password = "secret_sauce"
    hamburgerIcon = "button#react-burger-menu-btn"
    logOutButton = "a#logout_sidebar_link"
```

### 2. `pageObjects/sauceDemo.py`

The `Actions` class encapsulates the methods required to interact with the Sauce Demo website, including login, sorting products, adding items to the cart, and completing the checkout process.

**Methods**:
- `visit_url()`: Navigates to the SauceDemo website.
- `login()`: Logs in as a user.
- `signed_in()`: Verifies the user is logged in by checking the visibility of page elements.
- `sort_by_price_low_to_high()`: Sorts products by price.
- `add_sauce_labs_onesie_to_cart()`, `add_sauce_labs_backpack_to_cart()`, etc.: Adds different products to the cart.
- `proceed_to_checkout()`: Fills in checkout details and completes the purchase.
- `close_browser()`: Closes the browser after the test execution.

### Example:

```python
class Actions:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def visit_url(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, el.usernameField).clear()
        self.driver.find_element(By.CSS_SELECTOR, el.usernameField).send_keys(el.standardUser)
        self.driver.find_element(By.CSS_SELECTOR, el.passwordField).clear()
        self.driver.find_element(By.CSS_SELECTOR, el.passwordField).send_keys(el.password)
        self.driver.find_element(By.CSS_SELECTOR, el.loginButton).click()

    def signed_in(self):
        try:
            self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.titleProduct)))
            print("user is logged in and title is visible")
            self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.logo)))
            print("logo is visible")
        except TimeoutError:
            print("Element not visible")
```

### 3. `e2e/sauce_demo.py`

This script is the entry point for running the end-to-end test cases. It initializes the `Actions` class and sequentially executes all test methods for logging in, adding products to the cart, and checking out.

### Example:

```python
from pageObjects.sauceDemo import Actions

execute = Actions()

execute.visit_url()
execute.login()
execute.signed_in()
execute.sort_by_price_low_to_high()
execute.add_sauce_labs_onesie_to_cart()
execute.add_sauce_labs_backpack_to_cart()
execute.add_sauce_labs_bike_light_to_cart()
execute.add_sauce_labs_fleece_jacket_to_cart()
execute.add_sauce_labs_bolt_tshirt_to_cart()
execute.add_test_all_the_things()
execute.proceed_to_checkout()
execute.close_browser()
```

## Requirements

Ensure you have the following dependencies installed to run the project:


```bash
pip install selenium
```
```bash
pip install webdriver-manager
```

You will also need to install install thedependencies in the requirements.txt file
```bash
pip install -r requirements.txt
```

## Running the Tests

To run the test suite, execute the following command from the project root:

```bash
python e2e/sauce_demo.py
```

This will:
- Visit the Sauce Demo website.
- Log in as the standard user.
- Sort products by price.
- Add various products to the cart.
- Proceed through the checkout process.
- Complete the purchase and close the browser.

