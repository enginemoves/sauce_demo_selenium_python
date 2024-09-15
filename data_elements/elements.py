class LoginPageElements:
    """
    Login elements/locators are stored here
    """
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
    cancelHamburgerSideNav = "button#react-burger-cross-btn"
    logOutButton = "a#logout_sidebar_link"
    lockeOutErrorMessage = ".error.error-message-container"
    cancelErrorMessageButton = ".error-button"


class productElements:
    logo = ".app_logo"
    titleProduct = ".title"
    sortIcon = ".product_sort_container"
    aboutButton = "a#about_sidebar_link"
    allItemButton = "a#inventory_sidebar_link"
    cartIcon = "div#shopping_cart_container > .shopping_cart_link"
    sauceLabsBackpack = "[data-test='item-4-title-link'] [data-test]"
    saucelabsBikeLight = "[data-test='item-0-title-link'] [data-test]"
    sauceLabsBoltTShirt = "[data-test='item-1-title-link'] [data-test]"
    sauceLabsFleeceJacket = "[data-test='item-5-title-link'] [data-test]"
    sauceLabsOnesie = "[data-test='item-2-title-link'] [data-test]"
    testallTheThings = "[data-test='item-3-title-link'] [data-test]"
    productDescription = ".inventory_details_desc_container"


class addProductToCart:
    """
    add products on the home page to cart
    """
    addToCartButton = "button#add-to-cart"
    addSauceLabBackpackToCart = "button#add-to-cart-sauce-labs-backpack"
    addSauceLabsBikeLightToCart = "button#add-to-cart-sauce-labs-bike-light"
    addSauceLabsBoltTShirtToCart = "button#add-to-cart-sauce-labs-bolt-t-shirt"
    addSauceLabsFleeceJacketToCart = "button#add-to-cart-sauce-labs-fleece-jacket"
    addSauceLabsOnesieToCart = "button#add-to-cart-sauce-labs-onesie"
    addTestallTheThingsToCart = "button#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)"


class removeProduct:
    """
    remove item from cart on the home page
    """
    removeProductFromCart = "button#remove"
    removeSauceLabBackpackToCart = "button#remove-to-cart-sauce-labs-backpack"
    removeSauceLabsBikeLightToCart = "button#remove-to-cart-sauce-labs-bike-light"
    removeSauceLabsBoltTShirtToCart = "button#remove-to-cart-sauce-labs-bolt-t-shirt"
    removeSauceLabsFleeceJacketToCart = "button#remove-to-cart-sauce-labs-fleece-jacket"
    removeSauceLabsOnesieToCart = "button#remove-to-cart-sauce-labs-onesie"
    removeTestallTheThingsToCart = "button#remove-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)"


class checkOut:
    """
    elements to complete check out process
    """
    checkoutButton = "button#checkout"
    firstNameField = "input#first-name"
    firstName = "Armstrong"
    lastNameField = "input#last-name"
    lastName = "Prince"
    zipCodeField = "input#postal-code"
    zipCode = "1001"
    continueButton = "input#continue"
    finishButton = "button#finish"
    thankYouScreen = "div#checkout_complete_container"
    backToHomeButton = "button#back-to-products"
