from  Database_fetch_url import browser_function
from webscrap import webscrapping
from tcp_udp_scan import tcp_udp_scan

print("Welcome to forencis tools")
while True:
    print("\n Select the task\n" \
              "1. Fetch Browser history \n" \
              "2. Web Scrapping \n" \
              "3. TCP/UDP Scan \n")
    task=int(input("Enter the choice number to perform above task: "))
    if task==1:
        browser_function()
    elif task==2:
        webscrapping()
    elif task==3:
        tcp_udp_scan()
    elif task>=4:
        print("\n Invalid Input")
    else:
        pass

    if input("\n Do you wish to continue the tasks? y/n ") == "y":
        continue
    else:
        break