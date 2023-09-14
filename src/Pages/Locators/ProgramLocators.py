from selenium.webdriver.common.by import By
import random


class ProgramLocators:
    ADD_PROGRAM_BUTTON_L = (By.CSS_SELECTOR, 'button.btn-primary i.fa-plus')
    PROGRAM_NAME_FIELD_L = (By.NAME, 'name')
    PROGRAM_DESC_FIELD_L = (By.NAME, 'description')
    CURRENCIES_L = (By.XPATH, '//div[contains(text(),"Type to Select")]')
    INPUT_CURRENCIES_L = (By.XPATH, '//form/div[3]/div[2]/div/div[1]/div[1]/div/div/input')

    ENABLE_SELLER_L = (By.CSS_SELECTOR, '.col:nth-child(2) .text-center:nth-child(1) .switch-slider')
    ENABLE_BUYER_L = (By.CSS_SELECTOR, '.text-center:nth-child(1) .switch-slider')
    ENABLE_MULTIPLE_BUYER_L = (By.CSS_SELECTOR, '.text-center:nth-child(2) .switch-slider')

    ENABLE_COLLABORATION_L = (By.CSS_SELECTOR, '.col:nth-child(2) > label >.switch-slider')

    QS_ENABLED_L = (By.CSS_SELECTOR, '[name="quoteEnabled"]+span.switch-slider')
    QS_LITIGATION_L = (By.CSS_SELECTOR, '[name="quoteLitigationEnabled"]+span.switch-slider')
    QS_INVENTORY_CHECKING = (By.CSS_SELECTOR, '[name="inventoryChecking"]+span.switch-slider')
    QS_LINE_ITEM_REV = (By.CSS_SELECTOR, '[name="lineItemRevision"]+span.switch-slider')
    QS_DISCOUNT_APPROV = (By.CSS_SELECTOR, '[name="quoteDiscountApprovalEnabled"]+span.switch-slider')
    QS_LOGO_FIELD_L = (By.CSS_SELECTOR, 'div.select-sm input[aria-autocomplete="list"]')

    OS = (By.CSS_SELECTOR, 'ul.list-group>li.align-items-center:nth-child(2)')
    OS_ENABLED_L = (By.CSS_SELECTOR, '[name="orderEnabled"]+span.switch-slider')
    OS_LITIGATION_L = (By.CSS_SELECTOR, '[name="orderLitigationEnabled"]+span.switch-slider')
    OS_LOGO_DROPDOWN_L = (By.CSS_SELECTOR, '.select-sm>.css-yk16xz-control > .css-1hwfws3')
    OS_LOGO_FIELD_L = (By.CSS_SELECTOR, 'div.select-sm input[autocapitalize="none"]')

    DA = (By.CSS_SELECTOR, 'li.align-items-center:nth-child(3)')
    DA_PARTIAL_L = (By.CSS_SELECTOR, '[name="partlyDespatchAdvice"]+span.switch-slider')
    DA_DGOODS_CONFIRMATION_L = (By.CSS_SELECTOR, '[name="despatchGoodsConfirmation"]+span.switch-slider')
    DA_INVEN_CHECK_L = (By.CSS_SELECTOR, '[name="despatchAdviceInventoryChecking"]+span.switch-slider')
    DA_SIGNATURES_L = (By.CSS_SELECTOR, '[name="activated"]+span.switch-slider')
    DA_ADD_SIGNATURES_L = (By.CSS_SELECTOR, 'button.btn.btn-primary.btn-sm')
    DA_SIGNATURES_FIELD_1 = (By.CSS_SELECTOR, '.table-borderless tr:nth-child(8) tr:nth-child(1) input')
    DA_SIGNATURES_FIELD_2 = (By.CSS_SELECTOR, '.table-borderless tr:nth-child(8) tr:nth-child(2) input')
    DA_LOGO_DROPDOWN_L = (By.CSS_SELECTOR, '.select-sm .css-tlfecz-indicatorContainer')
    DA_LOGO_FIELD_L = (By.CSS_SELECTOR, '.select-sm input[autocapitalize="none"]')

    RA = (By.CSS_SELECTOR, 'li.align-items-center:nth-child(4)')
    RA_LOGO_DROPDOWN_L = (By.CSS_SELECTOR, '.select-sm .css-19bqh2r')
    RA_LOGO_FIELD_L = (By.CSS_SELECTOR, '.select-sm input[autocapitalize="none"]')

    INV = (By.CSS_SELECTOR, 'li.align-items-center:nth-child(6)')
    INV_SIGNATURES_L = (By.CSS_SELECTOR, '[name="activated"]+span.switch-slider')
    INV_ADD_SIGNATURES_L = (By.CSS_SELECTOR, 'tr .btn')
    INV_SIGNATURES_FIELD_L = (By.CSS_SELECTOR, 'td [name="name"]')
    INV_LOGO_DROPDOWN_L = (By.CSS_SELECTOR, '.select-sm .css-tlfecz-indicatorContainer')
    INV_LOGO_FIELD_L = (By.CSS_SELECTOR, 'tr:nth-child(7) [autocapitalize="none"]')

    COLLABORATION_CL_L=(By.CSS_SELECTOR,'[name="collaborationCreditLimit"]+.switch-slider')

    SAVE_PROGRAM_BUTTON_L=(By.ID,'btn-save-program')
    IS_PROGRAM_CREATED_L=(By.CSS_SELECTOR,'div:nth-child(1)> .col-12 > p')