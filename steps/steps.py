import time
from behave import *
from CommonFilesandFolders.CommonConfig import linkconfig
from CommonFilesandFolders.CommonConfig import driver
from CommonFilesandFolders.CommonConfig import testparameters
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


@given('I go to the site "{site}" website')
def step_impl(context, site):
    """
    :type context: behave.runner.Context
    """
    url = linkconfig.LINKCONFIG.get(site)
    print(url)

    context.driver = driver.go_to(url)

@step('Verify page "{pagetitle}" is present')
def step_impl(context, pagetitle):
    """
    :param pagetitle:
    :type context: behave.runner.Context
    """
    #getting page title from linkconfig file
    expectedtitle = linkconfig.LINKCONFIG.get(pagetitle)

    #getting page title after website launch
    actualtitle = context.driver.title

    assert expectedtitle == actualtitle, "The title is not as expected." \
                                         " Expected: {}, Actual: {}".format(expectedtitle, actualtitle)
    print("The page title is as expected.")


@when('I click on "adduser" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    addbutton = context.driver.find_element_by_xpath("//button[@type='add']")
    addbutton.click()
    time.sleep(5)

@then('Verify "savebutton" is disabled and "closebutton" is enabled')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    closebutton = context.driver.find_element_by_xpath("//button[@ng-click='close()']")
    if closebutton.is_displayed():
        print("Close Button is visible")
    else:
        print('Close Button enabled is not displayed')
    savebutton = context.driver.find_element_by_xpath("//button[@ng-click='save(user)']")
    if savebutton.is_enabled() == False:
        print("Save button is disabled")
    else:
        print('Close Button is enabled and not displayed')

@then('Enter "{FirstName}" "{LastName}" "{UserName}" "{Password}" "{Email}" and "{CellPhone}"')
def step_impl(context, FirstName,LastName,UserName,Password,Email,CellPhone):
    """
    :type context: behave.runner.Context
    """
    fname = testparameters.USERCONFIG.get(FirstName)
    fnameelement = context.driver.find_element_by_xpath("//input[@type='text' and @name='FirstName']")
    fnameelement.send_keys(fname)

    lname = testparameters.USERCONFIG.get(LastName)
    lnameelement = context.driver.find_element_by_xpath("//input[@type='text' and @name='LastName']")
    lnameelement.send_keys(lname)

    uname = testparameters.USERCONFIG.get(UserName)
    unameelement = context.driver.find_element_by_xpath("//input[@type='text' and @name='UserName']")
    unameelement.send_keys(uname)

    password = testparameters.USERCONFIG.get(Password)
    passwordelement = context.driver.find_element_by_xpath("//input[@type='password' and @name='Password']")
    passwordelement.send_keys(password)

    email = testparameters.USERCONFIG.get(Email)
    emailelement = context.driver.find_element_by_xpath("//input[@type='email' and @name='Email']")
    emailelement.send_keys(email)

    phone = testparameters.USERCONFIG.get(CellPhone)
    phoneelement = context.driver.find_element_by_xpath("//input[@type='text' and @name='Mobilephone']")
    phoneelement.send_keys(phone)

    time.sleep(5)

@then("Select Role")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    roleselect = Select(context.driver.find_element_by_xpath("//*[@name='RoleId']"))
    roleselect.select_by_value('0')

    time.sleep(5)

@then('I click on "save" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    savebutton = context.driver.find_element_by_xpath("//button[@ng-click='save(user)']")
    savebutton.click()

    time.sleep(10)

@step('Verify "{UserName}" is displayed')
def step_impl(context, UserName):
    """
    :type context: behave.runner.Context
    """
    uname = str(testparameters.USERCONFIG.get(UserName))
    unameelement = context.driver.find_element_by_xpath("// *[contains(text(), '"+ uname +"')]")
    if unameelement.is_displayed() == True:
        print("Newly added user found")
    else:
        print("Newly added user not found")

@then('Search for user "{DeleteUsername}" on homepage and click on "deletebutton"')
def step_impl(context,DeleteUsername):
    """
    :param DeleteUsername:
    :type context: behave.runner.Context
    """
    duname = testparameters.USERCONFIG.get(DeleteUsername)
    duneleme = context.driver.find_element_by_xpath("//*[contains(text(), '"+ duname +"')]")
    if duneleme.is_displayed()==True:
        dunameelement = context.driver.find_element_by_xpath("//*[contains(text(), '"+ duname +"')]/..//I[@class='icon icon-remove']")
        dunameelement.click()
    else:
        print('Element not displayed')

    time.sleep(5)

@then('Click on "OKbutton" from deletescreen')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    okbutton = context.driver.find_element_by_xpath("//*[@ng-click='close(btn.result)' and contains(text(), 'OK')]")
    okbutton.click()
    time.sleep(10)

@step('Verify "{DeleteUsername}" is deleted')
def step_impl(context, DeleteUsername):
    """
    :type context: behave.runner.Context
    """
    duname = testparameters.USERCONFIG.get(DeleteUsername)
    try:
        if context.driver.find_element_by_xpath("//*[contains(text(), '" + duname + "')]"):
            print("Element not Deleted")
    except NoSuchElementException:
        print("Element deleted")