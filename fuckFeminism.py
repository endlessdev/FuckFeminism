import tweepy
import time

API_KEY = ''
API_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

oAuth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oAuth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth_handler = oAuth, api_root = '/1.1')

motherFuckers = api.search(u"한남")

cnt = 0

while(True):
    time.sleep(1)
    for fuckFeminachi in motherFuckers:
        cnt+=1
        print(fuckFeminachi)
        api.create_block(fuckFeminachi.user.id)
        print("%d 명의 메갈 처치 완료." % cnt)