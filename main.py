import sys
import time

from config import *
import api_bot
import selenium_bot

def main_menu():
    while True:
        clear_logo()
        print(f" {opt_labels[0]} API Automation (Fast)")
        print(f" {opt_labels[1]} Driver Automation (Selenium)")
        print(f" {opt_labels[2]} Exit")
        print(f"{LINE}")

        choice = input(f"{GREEN} [{RED}●{GREEN}] Select Option {EKL} ").strip()

        if choice in ['1', '01']:
            api_bot.run()
        elif choice in ['2', '02']:
            selenium_bot.run()
        elif choice in ['3', '03']:
            print(f"\n{GREEN} [{RED}●{GREEN}] Exiting...")
            time.sleep(1)
            sys.exit(0)
        else:
            print(f"\n{RED} Invalid Option! Please try again.")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()
