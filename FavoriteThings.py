import os
import urllib
from slackclient import SlackClient

SLACK_TOKEN = "<Your Slack Tokenm, e.g. 'xoxp-...'>" # Or use env token: os.environ.get('SLACK_TOKEN')

slack_client = SlackClient(SLACK_TOKEN)


# Get all messags that are starred
def get_stared_messages():
    star_call = slack_client.api_call("stars.list")
    if (star_call.get('ok')):
        return star_call['items']
    return None

# Fix the string to work with AppleScript
def asquote(astr):
  "Return the AppleScript equivalent of the given string."
  astr = astr.encode('utf-8')
  astr = astr.replace('"', '" & quote & "')
  return '"{}"'.format(astr)

# Function to get the person who sent the message
def get_user_info(userId):
    user_call = slack_client.api_call("users.info", user=userId)
    if user_call.get('ok'):
        aUser = user_call['user']
        return aUser['real_name']
    return None

# Remove the star when done adding item
def unstar_message(channelId,messageTimestamp):
    unstar_call = slack_client.api_call("stars.remove",channel=channelId,timestamp=messageTimestamp)
    return None


if __name__ == '__main__':
    stars = get_stared_messages()
    if stars:
        for s in stars:
            if s['type'] == 'message':
                message = s['message']

                text = urllib.unquote(message['text'])
                user = get_user_info(message['user'])
                if user == None:
                    user = "Unknown User"
                
		title = text[:75]    
                fullTitle = "@" + user + ": " + text
                
                channelId = s['channel']
                ts = message['ts']
                notes = "slack://channel?team=<Slack Team ID>&id=" + channelId + "&message=" + ts
                notes = fullTitle + "\n" + notes
		ascript = """osascript <Path To Script>/FavoriteThings.scpt """ + format(asquote(title)) + """ """ + format(asquote(notes))
                os.system(ascript)
                
                unstar_message(channelId,ts)
    else:
        print("Unable to authenticate.")
