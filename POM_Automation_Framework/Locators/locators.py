class Locators:
    #login locators
    username_textbox = "//input[@placeholder='Enter your mail']"
    password_textbox = "//input[@type='password']"
    login_button = "//button[@class='primary-btn sign-in-pad']"
    close_button = "//button[@class='custom-close-button' and @aria-label='Close popup']"
    #logout locators
    logout_menu = "//div[@class='profile-click-icon-div']"
    logout = "//div[contains(text(),'Log out')]"