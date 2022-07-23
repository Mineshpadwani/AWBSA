import sqlite3
from os import path, listdir
import csv
def browser_function():
    def chrome():
        data_path = path.expanduser('~') + r"\AppData\Local\Google\Chrome\User Data\Default"
        # files = listdir(data_path)
        history_db = path.join(data_path, 'history')

        try:
            c = sqlite3.connect(history_db)
            cursor = c.cursor()
            select_statement = "SELECT distinct urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
            cursor.execute(select_statement)
            results = cursor.fetchall()
            for url in results:
                # print(url)
                with open('chrome_history.csv', 'w', encoding='utf-8') as chrome:
                    file = csv.writer(chrome, delimiter=',', quoting=csv.QUOTE_ALL)
                    file.writerows(results)

        except sqlite3.OperationalError:
            print('Please Close the Chrome Browser Windows First')
            print('Chrome Database is Locked! Permission Denied.')


    def firefox():
        data_path = path.expanduser('~') + "\AppData\Roaming\Mozilla\Firefox\Profiles\ws0kadzo.default"
        # files = listdir(data_path)
        history_db = path.join(data_path, 'places.sqlite')

        try:
            c = sqlite3.connect(history_db)
            cursor = c.cursor()
            select_statement = "SELECT moz_places.url, moz_places.title FROM moz_places;"
            cursor.execute(select_statement)
            results = cursor.fetchall()
            for url in results:
                with open('firefox_history.csv', 'w', encoding='utf-8') as firefox:
                    file = csv.writer(firefox, delimiter=',', quoting=csv.QUOTE_ALL)
                    file.writerows(results)

        except sqlite3.OperationalError:
            print('Please Close the firefox Browser Windows First')
            print('Firefox Database is locked! Permission Denied.')


    def microsoft_edge():
        data_path = path.expanduser('~') + r"\AppData\Local\Microsoft\Edge\User Data\Default"
        # files = listdir(data_path)
        history_db = path.join(data_path, 'history')

        try:
            c = sqlite3.connect(history_db)
            cursor = c.cursor()
            select_statement = "SELECT urls.url, urls.visit_count FROM urls;"
            cursor.execute(select_statement)
            results = cursor.fetchall()
            for url in results:
                with open('micrsoft-egdes_history.csv', 'w', encoding='utf-8') as microsoft_edge:
                    file = csv.writer(microsoft_edge, delimiter=',', quoting=csv.QUOTE_ALL)
                    file.writerows(results)

        except sqlite3.OperationalError:
            print('Please Close the Microsoft Edge Browser Windows First')
            print('Microsoft Edge Database is locked! Permission Denied.')

    while True:
        print("\n Select the browser to fetch the url from history \n" \
              "1. chrome \n" \
              "2. firefox \n" \
              "3. microsoft edge \n")
        browser = str(input("Enter the browser name you want to fetch url from: "))
        if browser=="chrome":
            print(chrome())
        elif browser=="firefox":
            print(firefox())
        elif browser=="microsoft edge":
            print(microsoft_edge())
        else:
            print("no browser found")

        if input("\n Do you want to fetch another browser history? y/n :")=="y":
            continue
        else:
            break