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
