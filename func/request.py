from selenium import webdriver

def find_element(driver):
    element = (driver.find_element_by_id('branding')
                 .find_element_by_class_name('main_width')
                 .find_element_by_id('search')
                 .find_element_by_css_selector('form#search-box')
                 .find_element_by_css_selector('span#search_wrap > input#main_search'))
    return element


def results_count(self):
    count = self.find_element_by_css_selector('div#ipbwrapper'
                                              '> div#content'
                                              '> div.ipsLayout.ipsLayout_withleft.clearfix'
                                              '> div.ipsLayout_content'
                                              '> div.clearfix'
                                              '> div.pagination.clearfix.left'
                                              '> ul.ipsList_inline.left.pages'
                                              '> li#anonymous_element_1'
                                              '> a').text

    return int(count[-1])

def page_next(driver, page):
    page_next = driver.find_element_by_css_selector('div#ipbwrapper'
                                                    '>div#content'
                                                    '>div.ipsLayout.ipsLayout_withleft.clearfix'
                                                    '>div.ipsLayout_content:last-child'
                                                    '>div.clearfix'
                                                    '>div.pagination.clearfix.left'
                                                    '> ul.ipsList_inline.left.pages'
                                                    f'> li.page > a[title = "{str(page)}"]'
                                                    )
    page_next.click()


def parse_page(driver, rows):
    data = {}
    for row in range(1, rows + 1):
        to_search = driver.find_element_by_xpath(f'//table[@id = "forum_table"]/tbody/tr[{row}]/td[2]/h4/a')

        text = to_search.text
        link = to_search.get_attribute('href')
        data[text] = link
    return data

