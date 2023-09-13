from selenium.webdriver.common.by import By


class NavigationLocators:
    DOCSTORE_L = (By.CLASS_NAME, 'css-1uccc91-singleValue')
    DOCSTORE_FIELD_L = (By.CSS_SELECTOR, 'input[type="text"][aria-autocomplete="list"]')
    MENU_ADMINISTRATON_L = (By.CLASS_NAME, 'nav-link.nav-dropdown-toggle')
    SUBMENU_PROGRAM_L=(By.CSS_SELECTOR, 'a[href*="programmanagement"]')



    # # dropdown & IDR
    # dropdown = driver.find_element(By.XPATH, '//div[contains(text(), "Type to Select")]').click()
    # driver.find_element(By.CSS_SELECTOR, '#react-select-5-input').send_keys("IDR", Keys.ENTER)
    #
    # # click slider Collaboration,Buyer,Multiple Buyer,Seller
    # enabuy = driver.find_element(By.CSS_SELECTOR, '[name="enable"] + span.switch-slider').click()
    # multibuy = driver.find_element(By.CSS_SELECTOR, '[name="buyerMultiple"] + span.switch-slider').click()
    # enasel = driver.find_element(By.CSS_SELECTOR,
    #                              'input[name="enable"][aria-checked="false"]+span.switch-slider').click()
    # time.sleep(1)
    # collab = driver.find_element(By.CSS_SELECTOR,
    #                              'form>:nth-child(4)>div>div>:nth-child(2)>.mx-1>.switch-input+span').click()
    #
    # # Quote
    # q_ena = driver.find_element(By.CSS_SELECTOR, '[name="quoteEnabled"]+span.switch-slider').click()
    # q_liti = driver.find_element(By.CSS_SELECTOR, '[name="quoteLitigationEnabled"]+span.switch-slider').click()
    # q_invcheck = driver.find_element(By.CSS_SELECTOR, '[name="inventoryChecking"]+span.switch-slider').click()
    # q_lir = driver.find_element(By.CSS_SELECTOR, '[name="lineItemRevision"]+span.switch-slider').click()
    # q_disaprov = driver.find_element(By.CSS_SELECTOR,
    #                                  '[name="quoteDiscountApprovalEnabled"]+span.switch-slider').click()
    # # q_pricecor=
    # q_logo = driver.find_element(By.ID, 'react-select-6-input')
    # q_logo.click()
    # q_logo.send_keys('supp', Keys.ENTER)
    #
    # # Order
    # # ord=driver.find_element(By.XPATH,'//li/div[contains(text(),"Order")]').click()
    # ord = driver.find_element(By.CSS_SELECTOR, 'ul.list-group>li.align-items-center:nth-child(2)').click()
    # o_ena = driver.find_element(By.CSS_SELECTOR, '[name="orderEnabled"]+span.switch-slider').click()
    # o_logo = driver.find_element(By.ID, 'react-select-6-input').send_keys('supp', Keys.ENTER)
    # o_liti = driver.find_element(By.CSS_SELECTOR, '[name="orderLitigationEnabled"]+span.switch-slider').click()
    #
    # # DA
    # # da='//div[2]/div/ul/li[3]'
    # da = driver.find_element(By.CSS_SELECTOR, 'li.align-items-center:nth-child(3)').click()
    # da_pda = driver.find_element(By.CSS_SELECTOR, '[name="partlyDespatchAdvice"]+span.switch-slider').click()
    # da_dgc = driver.find_element(By.CSS_SELECTOR, '[name="despatchGoodsConfirmation"]+span.switch-slider').click()
    # da_invenc = driver.find_element(By.CSS_SELECTOR,
    #                                 '[name="despatchAdviceInventoryChecking"]+span.switch-slider').click()
    # da_sig = driver.find_element(By.CSS_SELECTOR, '[name="activated"]+span.switch-slider').click()
    # da_addsig = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-sm')
    # da_addsig.click()
    # da_addsig.click()
    # da_logo = driver.find_element(By.ID, 'react-select-6-input').send_keys('supp', Keys.ENTER)
    # da_tesxtsig = driver.find_element(By.CSS_SELECTOR, 'td input.form-control[type="text"][name="name"]').send_keys(
    #     'Sender', Keys.TAB, Keys.TAB, 'Receiver')
    #
    # # RA
    # driver.execute_script("window.scrollTo(0, 0);")
    # ra = driver.find_element(By.CSS_SELECTOR, 'li.align-items-center:nth-child(4)').click()
    # ra_logo = driver.find_element(By.ID, 'react-select-6-input').send_keys('buy', Keys.ENTER)
    #
    # # PI
    # pi = driver.find_element(By.CSS_SELECTOR, 'li.align-items-center:nth-child(5)').click()
    # piena = driver.find_element(By.CSS_SELECTOR, '[name="proformaInvoiceEnabled"]+span.switch-slider').click()
    #
    # # INV
    # inv = driver.find_element(By.CSS_SELECTOR, 'li.align-items-center:nth-child(6)').click()
    # inv_sig = driver.find_element(By.CSS_SELECTOR, '[name="activated"]+span').click()
    # inv_addsig = driver.find_element(By.CSS_SELECTOR, 'td>button.btn>i.fa').click()
    # inv_textsig = driver.find_element(By.CSS_SELECTOR, 'td>[name="name"]').send_keys('Board of Director')
    # inv_logo = driver.find_element(By.ID, 'react-select-12-input').send_keys('supp', Keys.ENTER)
    #
    # # save
    # save = driver.find_element(By.ID, 'btn-save-program').click()