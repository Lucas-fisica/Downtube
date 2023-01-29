from requests import post, get


def pesquisa(url_yt):

    headers = {'authority': 'x2download.app',
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://x2download.app',
    'referer': 'https://x2download.app/pt25',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)',
    'x-requested-with': 'XMLHttpRequest',
    }

    data =  {'q': url_yt, 'vt': 'home',}
    response = post('https://x2download.app/api/ajaxSearch', headers=headers, data=data).json()
    return response


def convert_yt(url, tipo='mp3', quality='128'):
        
    headers =  {
    'authority': 'dd163.auadyyzzfaffa.xyz',
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://x2download.app',
    'referer': 'https://x2download.app/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)',
    'x-requested-key': 'de0cfuirtgf67a',
    }
    
    info_v = pesquisa(url_yt=url)

    if tipo == 'mp3':
        data = {
        'v_id': info_v['vid'],
        'ftype': tipo,
        'fquality': quality,
        'token': info_v['token'],
        'timeExpire': info_v['timeExpires'],
        'client': 'X2Download.app',
        }
        url = 'https://backend.svcenter.xyz/api/convert-by-45fc4be8916916ba3b8d61dd6e0d6994'
        response = post(url, headers=headers, data=data).json()['d_url']
    else:

        data = {
        'v_id': info_v['vid'],
        'ftype': tipo,
        'fquality': quality,
        'fname': info_v['fn'],
        'token': info_v['token'],
        'timeExpire': info_v['timeExpires'],
        }
        url = 'https://dd163.auadyyzzfaffa.xyz/api/json/convert'   

        response = post(url, headers=headers, data=data).json()['result']
    if response == 'Converting':
        response = post(url, headers=headers, data=data).json()['result']
    return response, info_v['title']

def download(url, tipo='mp4', quality='720p'):
    headers =  {
    'authority': 've142.aadika.xyz',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://x2download.app/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)',}

    params = {
        'f': 'X2Download.app',
    }

    resposta = convert_yt(url, tipo=tipo, quality=quality)

    with open(f'{resposta[1]}.{tipo}', 'wb') as f:
        f.write(get(url=resposta[0], headers=headers, params=params, stream=True).content)
    
download('https://youtu.be/shfs23epWgs')