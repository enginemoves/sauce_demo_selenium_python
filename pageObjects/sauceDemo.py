from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from data_elements.elements import LoginPageElements as el
from data_elements import elements as sel


class Actions:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def visit_url(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        print("website url launched")

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, el.usernameField).clear()
        self.driver.find_element(By.CSS_SELECTOR, el.usernameField).send_keys(el.standardUser)
        self.driver.find_element(By.CSS_SELECTOR, el.passwordField).clear()
        self.driver.find_element(By.CSS_SELECTOR, el.passwordField).send_keys(el.password)
        self.driver.find_element(By.CSS_SELECTOR, el.loginButton).click()
        print("log in succesful")

    def signed_in(self):

        try:
            self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.titleProduct)))
            print("user is logged in and title is visible")
            self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.logo)))
            print("logo is visible")
        except TimeoutError:
            print("Element not visible")

    def sort_by_price_low_to_high(self):
        sortIcon = Select(self.driver.find_element(By.CSS_SELECTOR, sel.productElements.sortIcon))

        sortIcon.select_by_visible_text("Price (low to high)")
        print("product filtered")
        # sortIcon.select_by_visible_text("Name (Z to A)")
        # sortIcon.select_by_visible_text("Price (high to low)")
        #
        # sortIcon.select_by_visible_text("Name (A to Z)")

    def add_sauce_labs_onesie_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, sel.productElements.sauceLabsOnesie).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
        self.driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
        self.driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
        print("onsies added to cart")
        self.driver.back()

    def add_sauce_labs_backpack_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, sel.productElements.sauceLabsBackpack).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
        self.driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
        # driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
        print("backpack added to cart")
        self.driver.back()

    def add_sauce_labs_bike_light_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, sel.productElements.saucelabsBikeLight).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
        self.driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
        print("bike light added to cart")
        # self.driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
        self.driver.back()

    def add_sauce_labs_fleece_jacket_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, sel.productElements.sauceLabsFleeceJacket).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
        self.driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
        # self.driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
        print("fleece jacket added to cart")
        self.driver.back()

    def add_sauce_labs_bolt_tshirt_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, sel.productElements.sauceLabsBoltTShirt).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
        self.driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
        # self.driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
        print("bolt tshirt added to cart")
        self.driver.back()

    def add_test_all_the_things(self):
        self.driver.find_element(By.CSS_SELECTOR, sel.productElements.testallTheThings).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
        self.driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
        # self.driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
        print("all the things added to cart")
        self.driver.back()

    def proceed_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, sel.productElements.cartIcon).click()
        self.driver.find_element(By.CSS_SELECTOR, sel.checkOut.checkoutButton).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.checkOut.continueButton)))
        self.driver.find_element(By.CSS_SELECTOR, sel.checkOut.continueButton).click()
        print("Continue to check out")
        self.driver.find_element(By.CSS_SELECTOR, sel.checkOut.firstNameField).send_keys(sel.checkOut.firstName)
        self.driver.find_element(By.CSS_SELECTOR, sel.checkOut.lastNameField).send_keys(sel.checkOut.lastName)
        self.driver.find_element(By.CSS_SELECTOR, sel.checkOut.zipCodeField).send_keys(sel.checkOut.zipCode)
        self.driver.find_element(By.CSS_SELECTOR, el.cancelErrorMessageButton).click()
        print("Customer details entered successfully")
        self.driver.find_element(By.CSS_SELECTOR, sel.checkOut.continueButton).click()
        self.driver.find_element(By.CSS_SELECTOR, sel.checkOut.finishButton).click()
        print("Checkout complete")
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.checkOut.thankYouScreen)))
        self.driver.find_element(By.CSS_SELECTOR, sel.checkOut.backToHomeButton).click()
        print("Returned to home page")

    def close_browser(self):
        self.driver.quit()

