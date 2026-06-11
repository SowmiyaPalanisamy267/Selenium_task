
class Locators:
    #login locators
    username_textbox = "input[placeholder='Enter your mail']"
    password_textbox = "input[placeholder='Enter your password ']"
    login_button = "button:has-text('Sign in')"
    close_button = "//button[@class='custom-close-button' and @aria-label='Close popup']"


    #Dashboard
    dashboard_text="//p[text()='Dashboard']"


    #logout locators
    logout_menu = "//div[@class='profile-click-icon-div']"
    logout = "//div[contains(text(),'Log out')]"