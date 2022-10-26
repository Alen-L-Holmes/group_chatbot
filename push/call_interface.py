import requests


# 摸鱼日历 return url
def get_slack_off_calendar():
    get_url = 'https://api.vvhan.com/api/moyu?type=json'
    try:
        res = requests.get(get_url, timeout=30)
        return res.json()['url']
    except requests.exceptions.RequestException:
        return '暂时无法获取今日摸鱼人日历，请稍后再试'
