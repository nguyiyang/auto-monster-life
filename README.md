# auto-monster-life
Auto Monster Life is an automation tool that removes the need to manually fuse for monsters in MapleStory's monster life which can take up to several hours.
MapleStory's monster life involves visiting other players' farms with specific monsters to fuse for.

## How to gather information on which farms contains specific monsters
This personal project consists of Google Sheets API to gather data on available farms for monsters from a Google Sheets document managed by the player community.
It also hosts a database online which updates itself periodically everyday using Github Actions cron job.

### Reasons for using database instead of polling data from Google Sheets document straight when running the script
1. Google Sheets API takes quite some time to return the tables which can slow down the script
2. Using a database provides a clearer way to query for data with filters
3. I can practice writing SQL statements and learn to automate tasks at fixed schedules using cron

## The script
Wrote a simple gui using tkinter for user to input the monsters they have as well as the monster they wish to fuse for.
The app then queries the database for a list of farms to visit.
Given the list of farms, the app uses AutoHotPy to inject keystrokes to visit each farm and fuse with monsters.
The app uses pyautogui and preloaded set of images so that it knows where to click and navigate through the game.

## Things to work on:
1. Improve the ui
2. The app releases all monsters that are not in the selected list of monsters to fuse for. However some of the monsters fused along the way are also useful but released.
The app should consider this possibility and logic to keep these monsters should be implemented.
