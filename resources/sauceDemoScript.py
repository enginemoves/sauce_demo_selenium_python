from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from data_elements.elements import LoginPageElements as el
from data_elements import elements as sel
from time import sleep
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
#
# driver.find_element(By.CSS_SELECTOR, el.usernameField).send_keys(el.problemUser)
# driver.find_element(By.CSS_SELECTOR, el.passwordField).send_keys(el.password)
# driver.find_element(By.CSS_SELECTOR, el.loginButton).click()
# sleep(2)
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.hamburgerIcon)))
# driver.find_element(By.CSS_SELECTOR, el.hamburgerIcon).click()
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.logOutButton)))
# driver.find_element(By.CSS_SELECTOR, el.logOutButton).click()
# sleep(1)
#
# # problem user
# driver.find_element(By.CSS_SELECTOR, el.usernameField).clear()
# driver.find_element(By.CSS_SELECTOR, el.usernameField).send_keys(el.lockedOutUser)
# driver.find_element(By.CSS_SELECTOR, el.passwordField).clear()
# driver.find_element(By.CSS_SELECTOR, el.passwordField).send_keys(el.password)
# driver.find_element(By.CSS_SELECTOR, el.loginButton).click()
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.lockeOutErrorMessage)))
# driver.find_element(By.CSS_SELECTOR, el.cancelErrorMessageButton).click()
#
# sleep(2)
# # problem glitch user
# driver.find_element(By.CSS_SELECTOR, el.usernameField).clear()
# driver.find_element(By.CSS_SELECTOR, el.usernameField).send_keys(el.problemUser)
# driver.find_element(By.CSS_SELECTOR, el.passwordField).clear()
# driver.find_element(By.CSS_SELECTOR, el.passwordField).send_keys(el.password)
# driver.find_element(By.CSS_SELECTOR, el.loginButton).click()
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.hamburgerIcon)))
# driver.find_element(By.CSS_SELECTOR, el.hamburgerIcon).click()
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.logOutButton)))
# driver.find_element(By.CSS_SELECTOR, el.logOutButton).click()
# sleep(2)
#
# # sign in as error user
# driver.find_element(By.CSS_SELECTOR, el.usernameField).clear()
# driver.find_element(By.CSS_SELECTOR, el.usernameField).send_keys(el.errorUser)
# driver.find_element(By.CSS_SELECTOR, el.passwordField).clear()
# driver.find_element(By.CSS_SELECTOR, el.passwordField).send_keys(el.password)
# driver.find_element(By.CSS_SELECTOR, el.loginButton).click()
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.hamburgerIcon)))
# driver.find_element(By.CSS_SELECTOR, el.hamburgerIcon).click()
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.logOutButton)))
# driver.find_element(By.CSS_SELECTOR, el.logOutButton).click()
# sleep(3)

# # sign in as visual
# driver.find_element(By.CSS_SELECTOR, el.usernameField).clear()
# driver.find_element(By.CSS_SELECTOR, el.usernameField).send_keys(el.visualUser)
# driver.find_element(By.CSS_SELECTOR, el.passwordField).clear()
# driver.find_element(By.CSS_SELECTOR, el.passwordField).send_keys(el.password)
# driver.find_element(By.CSS_SELECTOR, el.loginButton).click()
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.hamburgerIcon)))
# driver.find_element(By.CSS_SELECTOR, el.hamburgerIcon).click()
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, el.logOutButton)))
# driver.find_element(By.CSS_SELECTOR, el.logOutButton).click()
# sleep(3)

# sign in as normal user
driver.find_element(By.CSS_SELECTOR, el.usernameField).clear()
driver.find_element(By.CSS_SELECTOR, el.usernameField).send_keys(el.standardUser)
driver.find_element(By.CSS_SELECTOR, el.passwordField).clear()
driver.find_element(By.CSS_SELECTOR, el.passwordField).send_keys(el.password)
driver.find_element(By.CSS_SELECTOR, el.loginButton).click()

try:
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.titleProduct)))
    print("user is logged in and title is visible")
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.logo)))
    print("logo is visible")
except TimeoutError:
    print("Element not visible")


sortIcon = Select(driver.find_element(By.CSS_SELECTOR, sel.productElements.sortIcon))


sortIcon.select_by_visible_text("Price (low to high)")
# sortIcon.select_by_visible_text("Name (Z to A)")
# sortIcon.select_by_visible_text("Price (high to low)")
#
# sortIcon.select_by_visible_text("Name (A to Z)")

# add sauceLabsOnesie to cart
driver.find_element(By.CSS_SELECTOR, sel.productElements.sauceLabsOnesie).click()
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
driver.back()

# add sauceLabsBackpack to cart
driver.find_element(By.CSS_SELECTOR, sel.productElements.sauceLabsBackpack).click()
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
# driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
driver.back()

# add sauce labs  bike light to cart
driver.find_element(By.CSS_SELECTOR, sel.productElements.saucelabsBikeLight).click()
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
# driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
driver.back()

# add sauce Labs Fleece Jacket to cart
driver.find_element(By.CSS_SELECTOR, sel.productElements.sauceLabsFleeceJacket).click()
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
# driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
driver.back()

# add sauce Labs Bolt T-Shirt to cart
driver.find_element(By.CSS_SELECTOR, sel.productElements.sauceLabsBoltTShirt).click()
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
# driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
driver.back()

# add sauce Labs Bolt T-Shirt
driver.find_element(By.CSS_SELECTOR, sel.productElements.testallTheThings).click()
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.productElements.productDescription)))
driver.find_element(By.CSS_SELECTOR, sel.addProductToCart.addToCartButton).click()
# driver.find_element(By.CSS_SELECTOR, sel.removeProduct.removeProductFromCart)
driver.back()

# open cart
driver.find_element(By.CSS_SELECTOR, sel.productElements.cartIcon).click()
driver.find_element(By.CSS_SELECTOR, sel.checkOut.checkoutButton).click()
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.checkOut.continueButton)))
driver.find_element(By.CSS_SELECTOR, sel.checkOut.continueButton).click()
driver.find_element(By.CSS_SELECTOR, sel.checkOut.firstNameField).send_keys(sel.checkOut.firstName)
driver.find_element(By.CSS_SELECTOR, sel.checkOut.lastNameField).send_keys(sel.checkOut.lastName)
driver.find_element(By.CSS_SELECTOR, sel.checkOut.zipCodeField).send_keys(sel.checkOut.zipCode)
driver.find_element(By.CSS_SELECTOR, el.cancelErrorMessageButton).click()
driver.find_element(By.CSS_SELECTOR, sel.checkOut.continueButton).click()
driver.find_element(By.CSS_SELECTOR, sel.checkOut.finishButton).click()
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sel.checkOut.thankYouScreen)))
driver.find_element(By.CSS_SELECTOR, sel.checkOut.backToHomeButton).click()
sleep(5)
driver.quit()
