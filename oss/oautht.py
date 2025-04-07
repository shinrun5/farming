from ossapi import Ossapi, Scope

client_id = *
client_secret = "*"
callback_url = "*"
scopes = [Scope.PUBLIC, Scope.FORUM_WRITE]
api = Ossapi(client_id, client_secret, callback_url, scopes=scopes)
forum = api.forum_topic(2062514)
print()