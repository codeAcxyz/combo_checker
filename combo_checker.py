import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

token = "5518056932:AAGstUiVjzrGx3IbmCg1_O7lyX4qASUnDK0"
chat_id = "1120121505"


def send_msg(text):
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    requests.get(url_req)


url = "https://nitestats.com/codes-checker"
combos = open('combo.txt', 'r')
success = open('success.txt', 'a+')
lst = []
for acc in combos:
    if acc != "\n":
        lst.append(acc)
lst = list(map(str.strip, lst))
length_of_combos = len(lst)
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe", options=options)
driver.get(url)
driver.maximize_window()


def wait_and_find(findind_value, number):
    if number == 1:
        while 1:
            try:
                element = driver.find_element_by_class_name(findind_value)
                return element
            except:
                pass
    elif number == 2:
        while 1:
            try:
                element = driver.find_element_by_xpath(findind_value)
                return element
            except:
                pass

    elif number == 3:
        while 1:
            try:
                element = driver.find_element_by_id(findind_value)
                return element
            except:
                pass


def find_combos(arr):
    for combo in arr:
        status = wait_and_find(combo, 3)
        print(status)
        if status.text[23:32] != "Not_Found":
            success.write(status.text)

            send_msg("Found Combo -----> " + status.text)


def is_process_done():
    data = wait_and_find("statusData", 3)
    while 1:
        print(data.text)
        if str(data.text) == "100%":
            return True
        else:
            time.sleep(5)


def is_valid():
    data = wait_and_find("validData", 3)
    if int(data.text) > 0:
        return True
    else:
        return False


def is_inactiveData():
    data = wait_and_find("inactiveData", 3)
    if int(data.text) > 0:
        return True
    else:
        return False


def for_tab(arr, start, end, step):
    global driver
    driver.refresh()
    data = ""
    for i in range(len(arr)):
        data = data + arr[i] + "\n"
    wait_and_find("codesForm", 3).send_keys(data)
    while 1:
        try:
            wait_and_find("ccStart", 3).click()
            break
        except:
            driver.execute_script("window.scrollTo(0, 600);")
    is_process_done()
    if is_valid() or is_inactiveData():
        success.write(data)
        send_msg("found_something please check success file")
    print("step " + str(step) + " done ----> " + str(start) + " , " + str(end))
    send_msg("step " + str(step) + " done ----> " + str(start) + " , " + str(end))


# driver.switch_to.window(driver.window_handles[-1])


if __name__ == '__main__':
    steps = length_of_combos / 500
    lst[515]="XV4Q3-D67LS-47LKB-8WD3W"
    print("Total_combos - " + str(length_of_combos) + " Total_steps - " + str(steps))
    send_msg("Total_combos - " + str(length_of_combos) + " Total_steps - " + str(steps))
    end_index = 500
    for i in range(int(steps)):
        if i == 0:
            s_index = 0
            end_index = 500
        else:
            s_index = end_index
            end_index = end_index + 500
        for_tab(lst[s_index:end_index], s_index, end_index, i)

    # t1 = threading.Thread(target=genrating_tabs, args=(lst[0:500],))
    # t2 = threading.Thread(target=genrating_tabs, args=(lst[500:1000],))
    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()
