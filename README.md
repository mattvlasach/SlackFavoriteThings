# Summary
This script will run every 5 minutes to import an Slack message that have been "Starred" in Slack into Things 3.

It uses a LaunchAgent scheduler to query the Slack REST API, fetch the starred message contents, create the To Do in Things (via AppleScript), then Un-star the message.

The created To Do is added to yout inbox, tagged with "Slack", and includes a link to the specific starred message for quick recall via your browser, desktop or mobile Slack app. 

The goal of the project is to add Slack messages to your task management workflow so everything is centralized and responses don't fall through the cracks.

Hope you find it helpful!

# Requirements
* macOS 10.4 or later
* Slack API Token (get from Slack settings)
* Python installed
* Slack Python SDK installed

# Installation
1. Download repository to your mac
2. Move "FavoriteThings.py" and "FavoriteThings.scpt" to a good spot on your machine (e.g. `~/Library/Documents/Slack`)
3. Edit "FavoriteThings.py" and replace the placeholder strings surrounded by `< >`.  This includes the `SLACK_TOKEN`, `team` in `notes`, and path to "FavoriteThings.scpt" in `ascript`. 
4. Edit "com.vlasach.FavoriteThings.plist" and modify the path parameter to include the full path leading to "FavoriteThings.py"
5. Move "com.vlasach.FavoriteThings.plist" into ~/Library/LaunchAgents/
6. In Terminal, set the LaunchAgent to occur at startup and start running immediately: `launchctl load ~/Library/LaunchAgents/com.vlasach.FavoriteThings.plist`

# Testing
After modifying the above files, you can test things are working by starring a message in Slack then excuting the Python script manually: `python FavoriteThings.py`.  

If all goes well the To Do will be created in Things and message will be Un-starred.

