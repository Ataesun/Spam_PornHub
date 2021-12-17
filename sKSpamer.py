#++++++++++ lib ++++++++++#
from art import *
import os
import sys
import time
from selenium import webdriver
import time
from prettytable import PrettyTable
#----------#
#!
#?
#!
#++++++++++ Loading ++++++++++#
os.system('cls')
tprint("Loading…")
time.sleep(1)
os.system('cls')
tprint("Loading…")
print("10%")
print("███▒▒▒▒▒▒▒")
time.sleep(1)
os.system('cls')
tprint("Loading…")
print("30%")
print("█████▒▒▒▒▒")
time.sleep(1)
os.system('cls')
tprint("Loading…")
print("50%")
print("███████▒▒▒")
time.sleep(1)
d = webdriver.Firefox()
time.sleep(0.2)

os.system('cls')
tprint("LOADING...")
print("██████████████]99% ")
os.system('cls')
#++++++++++ Loading ++++++++++#


myTable = PrettyTable(["opttion", "RuleNumb", "about"])
myTable.add_row(["SignUp", "1", "Create new account"])
myTable.add_row(["Login", "2", "use account "])
print(myTable)
login = input("Tell urStepbro-> ")

os.system('cls')#!


print ("Yes,daddy:) ")
usr = input("user name -> ")
print(usr)
pas = input("type pass -> ")
print (pas)
os.system('cls')#!

    # ! SignUp
if login=="1": #signup
    email = input("type tempmail -> ")
    d.get("https://www.pornhub.com/signup")
    os.system('cls')#!

    em = d.find_element_by_css_selector(".formStepOne > input:nth-child(3)")
    em.send_keys(email)
    ##?

    user = d.find_element_by_css_selector(".formStepOne > input:nth-child(5)")
    user.send_keys(usr)
    # ?

    p = d.find_element_by_css_selector(".formStepOne > input:nth-child(7)")
    p.send_keys(pas)
    
    time.sleep(3)
    log = d.find_element_by_css_selector("input.buttonBase")
    log.click()

    os.system('cls')#!
    time.sleep(3)
    l=input ("when you verf Press Enter..!")

    # ! done

if login=="2": #login
    d.get("https://www.pornhub.com/login")
    
    userr = d.find_element_by_class_name("js-signinUsername")
    userr.send_keys("devasex1")

    ps = d.find_element_by_class_name("js-signinPassword")
    ps.send_keys("TwixoNTop")

    time.sleep(3)
    b=d.find_element_by_css_selector("#submit")
    b.click()

os.system('cls')#!
link = d.get("https://www.pornhub.com/view_video.php?viewkey=ph60f576d9ef8ca")
#d.execute_script("window.scrollTo(0,document.body.scrollHeight)")
urcom = input("comment->: ")
hm = 1
for x in range(50):
    os.system('cls')#!
    print (hm + 1)
    time.sleep(2)

    d.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    com=d.find_element_by_xpath("/html/body/div[7]/div[2]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/form/div[1]/div[2]")
    com.click()
    com.clear()
    com.send_keys(urcom)


    btn = d.find_element_by_xpath("/html/body/div[7]/div[2]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/form/div[2]/button")
    btn.click()


    nex = d.find_element_by_xpath("/html/body/div[7]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/video-element/div/div[1]/div[1]/div[2]/div")
    nex.click()
    