#!/usr/bin/env python3

import os

from selenium import webdriver
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException, WebDriverException)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from lib.globals import Globals


def findElementsBy(self: (WebElement,webdriver),by=By.ID, value=None):    
    try:
        # return self.find_elements(by,value)
        return WebDriverWait(Globals.Test.Browser, 10).until(EC.presence_of_all_elements_located((by,value)))
    except NoSuchElementException:
        return WebElement(self,id(self))
    except TimeoutException:
        return WebElement(self,id(self))
    except StaleElementReferenceException:
        return WebElement(self,id(self))
    except WebDriverException:
        return WebElement(self,id(self))

def findElementBy(self: (WebElement,webdriver),by=By.ID, value=None):    
    try:
        # return self.find_element(by,value)
        return WebDriverWait(Globals.Test.Browser, 10).until(EC.presence_of_element_located((by,value)))
    except NoSuchElementException:
        return WebElement(self,id(self))    
    except StaleElementReferenceException:
        return WebElement(self,id(self))
    except WebDriverException:
        return WebElement(self,id(self))
    
    
def isDisplayed(self: WebElement):
    try:
        if self is not None:
            return self.is_displayed()
        else:
            return False
    except NoSuchElementException:
        return False
    except WebDriverException:
        return False
    except Exception:
        return False

def Clear(self: WebElement):
    try:
        if self is not None:
            self.clear()
        else:
            return False
    except NoSuchElementException:
        return False
    except WebDriverException:
        return False
    except Exception:
        return False

def sendKeys(self: WebElement, *value):
    try:
        if self is not None:
            self.clear()
            self.send_keys(value)
        else:
            return False
    except NoSuchElementException:
        return False
    except WebDriverException:
        return False
    except Exception:
        return False

def Click(self: WebElement):
    try:
        if self is not None:
            self.click()
        else:
            return False
    except NoSuchElementException:
        return False
    except WebDriverException:
        return False
    except Exception:
        return False

def isSelected(self: WebElement):
    try:
        if self is not None:
            return self.is_selected()
        else:
            return False
    except NoSuchElementException:
        return False
    except WebDriverException:
        return False
    except Exception:
        return False

def isEnabled(self: WebElement):
    try:
        if self is not None:
            return self.is_enabled()
        else:
            return False
    except NoSuchElementException:
        return False
    except WebDriverException:
        return False
    except Exception:
        return False




def waitUntilHidden(self:WebElement,timeout:int=5):
    try:        
        elm = None
        elm = WebDriverWait(Globals.Test.Browser, timeout, 1, (StaleElementReferenceException,NoSuchElementException)).until(EC.invisibility_of_element(self))
        if elm is not None :
            return True
        else:
            return False
    except TimeoutException:
        return False
    except Exception:
        return False
    
def waitUntilDisplay(self:WebElement,timeout:int=5):
    try:        
        elm = None
        elm = WebDriverWait(Globals.Test.Browser, timeout, 1, (StaleElementReferenceException,NoSuchElementException)).until(EC.visibility_of(self))
        if elm is not None :
            return True
        else:
            return False
    except TimeoutException:
        return False
    except Exception:
        return False

def waitUntilExistInDOM(self:WebElement,timeout:int=5):
    try:
        elm = None
        elm = WebDriverWait(Globals.Test.Browser, timeout, 1, (StaleElementReferenceException,NoSuchElementException)).until(EC.presence_of_element_located(self))
        if elm is not None:
            return True
        else:
            return False
    except TimeoutException:
        return False
    except Exception:
        return False


def multi_select(self:WebElement, options):
      try:

        if self is not None:            
            select = Select(self)
            for option in options:
                select.select_by_visible_text(option)
        else:
            return False
        
      except NoSuchElementException:
          return False
      except WebDriverException:
          return False
      except Exception:
          return False

def select(self:WebElement, option):
      try:

        if self is not None:            
            select = Select(self)
            select.select_by_visible_text(option)
        else:
            return False
        
      except NoSuchElementException:
          return False
      except WebDriverException:
          return False
      except Exception:
          return False

WebDriver.findElementBy = findElementBy
WebDriver.findElementsBy = findElementsBy


WebElement.multi_select = multi_select
WebElement.select = select
WebElement.findElementBy = findElementBy
WebElement.findElementsBy = findElementsBy
WebElement.isEnabled = isEnabled
WebElement.isSelected = isSelected
WebElement.Click = Click
WebElement.sendKeys = sendKeys
WebElement.Clear = Clear
WebElement.isDisplayed = isDisplayed
WebElement.waitUntilHidden = waitUntilHidden
WebElement.waitUntilExistInDOM = waitUntilExistInDOM
WebElement.waitUntilDisplay = waitUntilDisplay

