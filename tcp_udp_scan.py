import nmap
def tcp_udp_scan():
    scanner = nmap.PortScanner()
    print("welcome,this is a simple nmap automation tool")
    print("<-------------------------------------------->")
    ip_addr=input("please enter ip address to scan: ")
    print("the ip you entered is: ", ip_addr)
    type(ip_addr)

    resp = input("""\n please enter the type of scan you want to run
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Comprehensive scan\n""")
    print("you have selected option: ", resp)

    if resp == '1':
        print("Nmap Version: ",scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024','-v -sS')
        print(scanner.scaninfo())
        print("IP status: ",scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ",scanner[ip_addr]['tcp'].keys())
    elif resp == '2':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("IP status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    elif resp == '3':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sS -sU -sC -A -O')
        print(scanner.scaninfo())
        print("IP status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    elif resp >= '4':
        print("please enter valid option")