import json, requests, sys
print ("Delete all messages from specific channel")
 
username1 = "Ratio"
username2 = "Ratio#1618"
auth_token = "console > application > local > discord > token"
channel_id = "lol"
delete_from_all_users = "False"
 
def get_all_messages(auth, id, last="", prev=[]):
    if not last:
        messages = json.loads(requests.get("http://canary.discordapp.com/api/v6/channels/" + id + "/messages", headers={"authorization": auth}, params={"limit": 100}).content)
    else:
        messages = json.loads(requests.get("http://canary.discordapp.com/api/v6/channels/" + id + "/messages", headers={"authorization": auth}, params={"before" : last, "limit" : 100}).content)
 
    prev = prev + messages
 
    if len(messages) < 100:
        print ("Got to end of channel at " + str(len(prev)) + " messages")
        return prev
    else:
        oldest = sorted(messages, key=lambda x: x["timestamp"], reverse=True)[-1]
        return get_all_messages(auth, id, last=oldest["id"], prev=prev)
 
def delete_all(auth, id, user1, user2, messages):
    print ("Trying to delete all messages in " + id + " from username " + user1)
    for message in messages:
        if (message["author"]["username"] == user1):
            print(message["author"]["username"])
            requests.delete("http://canary.discordapp.com/api/v6/channels/" + id + "/messages/" + message["id"],headers={"authorization": auth})
    print ("All messages were deleted")
 
delete_all(auth_token, channel_id, username1, username2, get_all_messages(auth_token, channel_id))
