import requests
headers={
'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'statistics_clientid=me; ganji_uuid=5409032012509921300548; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A68120954659%7D; __utma=32156897.817441245.1554288921.1554288921.1554288921.1; __utmc=32156897; __utmz=32156897.1554288921.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); citydomain=bj; ganji_xuuid=19b7e9f5-2172-4b36-d7d0-081dc2b1cf74.1554288921826; GANJISESSID=1ggpb0r6bj70ectg8ehgsic1qn; _wap__utmganji_wap_caInfo_V2=%7B%22ca_name%22%3A%22-%22%2C%22ca_source%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%7D; lg=1; xzfzqtoken=IQ3qKnwqGn%2Bm8bBmtx8bGzM6qr3z4zwfaILqO3V8RhCWIGYoGJ8y5aev6ugH8jNXin35brBb%2F%2FeSODvMgkQULA%3D%3D; ganji_login_act=1554289883826; __utmb=32156897.10.10.1554288921',
'Host':'bj.ganji.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

}
response=requests.get("http://bj.ganji.com/bomeiquan/",headers=headers)


