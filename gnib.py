#!/usr/bin/env python
# coding=utf-8
# File Name: gnib.py
# Author: liucheng
# Created Time: 四  8/24 11:16:39 2017
import urllib2
import urllib
import cookielib
import re
import time
from splinter import Browser
from twilio.rest import Client
account_sid = "XXXXXXXXXXX"
auth_token = "XXXXXXXXXXX"
client = Client(account_sid, auth_token)
Month={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
browser=Browser('chrome')
class gnib:
    def __init__(self, Category,SubCategory,ConfirmGNIB,GNIBNo,GNIBExDT,GivenName,SurName,DOB,Email,PPNo):
        self.Category=Category
        self.SubCategory=SubCategory
        self.ConfirmGNIB=ConfirmGNIB
        self.GNIBNo=GNIBNo
        self.GNIBExDT=GNIBExDT
        self.GivenName=GivenName
        self.SurName=SurName
        self.DOB=DOB
        self.Email=Email
        self.PPNo=PPNo
    
    def start_gnib(self):
        page="https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/AppSelect?OpenForm"
        browser.visit(page)
        time.sleep(2)
        browser.find_by_id('Category').first.select(self.Category)
        browser.find_by_id('SubCategory').first.select(self.SubCategory)
        browser.find_by_id('ConfirmGNIB').first.select(self.ConfirmGNIB)
        browser.find_by_id('GNIBNo').fill(self.GNIBNo)
        browser.find_by_id('GNIBExDT').click()
        browser.find_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr/td/span[text()='"+self.GNIBExDT[6:10]+"']").click()
        browser.find_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td/span[text()='"+Month[int(self.GNIBExDT[3:5])]+"']").click()
        for i in range(1,7):
            if browser.find_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr["+str(i)+"]/td[text()='"+str(int(self.GNIBExDT[0:2]))+"']").is_empty() is False:
                browser.find_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr["+str(i)+"]/td[text()='"+str(int(self.GNIBExDT[0:2]))+"']").click()
                break 
        #browser.find_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[3]/td[text()='15']").click()
        browser.find_by_id('UsrDeclaration').click()
        browser.find_by_id('GivenName').fill(self.GivenName)
        browser.find_by_id('SurName').fill(self.SurName)
        browser.find_by_id('DOB').click()
        browser.find_by_xpath('/html/body/div[2]/div[3]/table/thead/tr/th[1]').click()
        browser.find_by_xpath('/html/body/div[2]/div[3]/table/thead/tr/th[1]').click()
        browser.find_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr/td/span[text()='"+self.DOB[6:10]+"']").click()
        browser.find_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td/span[text()='"+Month[int(self.DOB[3:5])]+"']").click()
        for i in range(1,7):
            if browser.find_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr["+str(i)+"]/td[text()='"+str(int(self.DOB[0:2]))+"']").is_empty() is False:
                browser.find_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr["+str(i)+"]/td[text()='"+str(int(self.DOB[0:2]))+"']").click()
                break 
        browser.find_by_xpath("//*[@id='Nationality']/option[41]").click()
        browser.find_by_id('Email').fill(self.Email)
        browser.find_by_id('EmailConfirm').fill(self.Email)
        browser.find_by_xpath("//*[@id='FamAppYN']/option[3]").click()
        browser.find_by_xpath("//*[@id='PPNoYN']/option[2]").click()
        browser.find_by_id('PPNo').fill(self.PPNo)
        browser.find_by_id('btLook4App').click()
        time.sleep(2)
        browser.find_by_xpath("//*[@id='AppSelectChoice']/option[3]").click()
        browser.find_by_id('btSrch4Apps').click()
        time.sleep(5)
        count=0
        run=True
        while run:
            if browser.find_by_xpath("//*[@id='dvAppOptions']/table/tbody/tr/td[text()='No appointment(s) are currently available']").is_empty() is True:
                haha=browser.find_by_xpath("//div[@class='appOption']/table/tbody/tr/td[2]")
                for id in haha:
                    print(id.text)
                    if id.text!="" and int(id.text.split(' ')[0])>=14:
                        run =False
                        break
            count=count+1
            print("Search Time: "+str(count))
            time.sleep(10)
            if run==True:
                browser.find_by_id('btSrch4Apps').click()
        message = client.messages.create(to="Receive Number",from_="Sent Number in Twilio",body="Hurry UP!!! Look at the computer!!!!")


if __name__=='__main__':
    #dic={"Category":"Work","SubCategory":"3rd Level Graduate Scheme ","ConfirmGNIB":"Renewal"}
    #dic={"Category":"Study","SubCategory":"Masters","ConfirmGNIB":"Renewal"}
    dic={"Category":"Study","SubCategory":"Degree","ConfirmGNIB":"Renewal"}
    f = open('a.txt', 'r')
    for line in f.readlines():
        dic[line.split('=')[0]] = line.split('=')[1]
    a=gnib(dic["Category"],dic["SubCategory"],dic["ConfirmGNIB"],dic["GNIBNo"],dic["GNIBExDT"],dic["GivenName"],dic["SurName"],dic["DOB"],dic["Email"],dic["PPNo"])
    a.start_gnib()
