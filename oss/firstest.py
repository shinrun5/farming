from ossapi import Ossapi, UserLookupKey, GameMode, RankingType

client_id = 1234
client_secret = "Password"
api = Ossapi(client_id, client_secret)

user = api.user("ShinRun", key=UserLookupKey.USERNAME)
print(user.id)

top50 = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
#top50 = api.ranking("osu", "performance")

print(top50.ranking[0].user.username)