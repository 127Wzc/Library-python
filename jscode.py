import ssl
import re
import requests
import execjs
import url

requests.adapters.DEFAULT_RETRIES = 5
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()
requests_with_session = requests.Session()

def obtain_js(html):
    js = '<script src="(.*?)"'
    href = re.compile(js, re.S).findall(html)
    return href

def obtain_code(js_code):
    hexch_js_code = requests.get(js_code, verify=False)
    hexch_js_code.encoding = 'utf8'
    ajax_url = re.compile(r'(?<=[A-Z]\.ajax_get\().*?(?=,)').search(hexch_js_code.text).group(0).replace('AJAX_URL',url.AJAX_URL_s)
    lista=ajax_url.split("+")
    mm=lista[4]
    l=mm.split("(")[1].split(")")[0]
    one = mm.split("(")
    code=""
    if len(one[0]) > 1:
        send = mm
        hexch_js_code = re.sub(r'[A-Z]\.ajax_get', 'return ' + send + ' ; T.ajax_get', hexch_js_code.text)
        code = execjs.compile(hexch_js_code).call('reserve_seat', "", "")
    else:
        send = l
        hexch_js_code = re.sub(r'[A-Z]\.ajax_get', 'return ' + send + ' ; T.ajax_get', hexch_js_code.text)
        str_code = execjs.compile(hexch_js_code).call('reserve_seat', "","")
        code = execjs.compile(hexch_js_code).call(one[0], str_code)
    return code