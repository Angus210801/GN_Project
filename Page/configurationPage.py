

def isElementExist(self,element):

    flag = True
    try:
        self.find_element_by_css_selector(element)
        return flag
    except:
        flag = False
        return flag

def isInputExist(self,element):
    try:
        self.find_element_by_css_selector(element)
        return True
    except:
        return False

def isUploadButton(self,element):
    try:
        self.find_element_by_css_selector(element)
        return True
    except:
        return False

def isLanguageSetExist(self,element):
    try:
        self.findElement_by_xpath_selector(element)
        return True
    except:
        return False
