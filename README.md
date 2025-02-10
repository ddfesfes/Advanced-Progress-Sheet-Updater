<h1 align="center">Progress Sheet Updater</h1>
<p align="center">
    <img width="300" alt="Screenshot" src="readmeimages/screenshot.gif">
</p>

## About

This tool can update your Voltaic Benchmark Progress Sheet for both [Aimlab](https://docs.google.com/spreadsheets/d/11PMV6ACarUZKk16oSumx-3rZHGihOc89l-nrpcZ9qfM) and [Kovaaks](https://docs.google.com/spreadsheets/d/1qUzF2KHcfs_FgsaDFRfGsLgHhoC1Md5bzMOUbsYzSjg) with high scores and averages of completed tasks/scenarios.

Run it before checking your progress sheet, or leave it running in the background to keep your sheet up-to-date as you play.

If you use multiple configs, you can just drag them into the .exe to make your life easier.

Easily keep track of additional scenarios beyond the scope of the Voltaic Benchmarks through the configuration file (Kovaaks only).

## Updating

If you want to update to a newer release, all you have to do is download the newest one. Then unzip the files and move them over into your old folder.  

## Quickstart Guide

####    This guide is also available as a [video](https://www.youtube.com/watch?v=awBoG9Jy8CY) (please make sure to check the pinned comment of the video for further information).

1. Make a copy of the Voltaic Benchmark Progress Sheet for [Aimlab](https://docs.google.com/spreadsheets/d/11PMV6ACarUZKk16oSumx-3rZHGihOc89l-nrpcZ9qfM), [Kovaaks](https://docs.google.com/spreadsheets/d/1qUzF2KHcfs_FgsaDFRfGsLgHhoC1Md5bzMOUbsYzSjg) or both if you don't already have them. This requires a Google account.

2. Download and extract the latest release of this tool from [here](https://github.com/VoltaicHQ/Progress-Sheet-Updater/releases). I recommend [7zip](https://www.7-zip.org/) for extracting zip files.

3. Go [here](https://developers.google.com/workspace/guides/create-project), and ensure you are logged in to the same Google Account that owns your progress sheet. Then:  

    1. Click the link `Go to create a Project` in step 1.
    2. Type any name you like in the `Project Name` field and click the `CREATE` button under the `Location` field.
    3. Wait until a green check mark shows up in the notification window at the top right of the window indicating that the creation of your project is complete. Then click APIs & Services on the menu to the left.
    4. Click the project you just created.
    5. The Google Sheets API might show up in the list at the bottom - click it if it does. If not, click the `ENABLE APIS AND SERVICES` button at the top. Click the `Search for APIs & Services` text field and type `Google Sheets API`. Click the `Google Sheets API` box. Click `Enable` and wait for it to open.
    6. Click `Credentials` on the menu to the left.
    7. Click the `Create Credentials` button near the top and select `OAuth client ID`.
    8. Click the `CONFIGURE CONSENT SCREEN` button on the right.
    9. Select the `External` option and click the `CREATE` button underneath it.
    10. In the `App information` section—in the `App name` field, type whatever you want to name your app. In the `User support email` field, type the email address for the Google account that owns your progress sheet. In the `Developer contact information` section near the bottom of the page—in the `Email addresses` field, type the email address for the Google account that owns your progress sheet.
    11. Click the `SAVE AND CONTINUE` button at the bottom of the page.
    12. Click the `ADD OR REMOVE SCOPES` button.
    13. In the `Update selected scopes` menu that opens on the right side of the screen, at the bottom, under the `Manually add scopes` section, paste ht<span>tps://ww</span>w.googleapis.com/auth/spreadsheets in the text box and click the `ADD TO TABLE` button underneath.
    14. Click the `UPDATE` button at the bottom of the menu, then click the `SAVE AND CONTINUE` button at the bottom.
    15. Click the `ADD USERS` button, type the email address for the Google account that owns your progress sheet into the text box on the right and click the `ADD` button underneath it.
    16. Click the `SAVE AND CONTINUE` button.
    17. Click `Credentials` on the left menu.
    18. Click the `CREATE CREDENTIALS` button at the top and select `OAuth client ID`.
    19. Click the `Application type` drop-down menu and select `Desktop application`.
    20. In the `Name` field, write whatever name you want and click the `Create` button at the bottom.
    21. Click the `OK` button.
    22. Under the `OAuth 2.0 Client IDs` section, your ID will be listed. Click the download icon on the far right of the row of your newly created ID.
    23. Name it `credentials.json` and save it in the folder with the rest of the program.
    
<p align="center">
    <img alt="Folder contents before oauth" src="readmeimages/folder_contents_before_auth.png">
</p>

4. Run `ProgressSheetUpdater.exe`. A GUI will open. This GUI is used to edit the configuration of the program.

5. Choose between Kovaaks or Aimlab via the tabs at the top left.
    #### Kovaaks
    1. Click the `Browse`-Button on the top right and navigate to your Kovaak's stats folder.  
    2. Paste the link to your Kovaaks Progress Sheet into the entryfield.  
    3. Check the settings that you wish to use:  
        `Number of runs to average`: Amount of runs used to calculate the averages.  
        `Run Mode`: Types of updating the scores.  
         1. `watchdog`: Program will update sheet once a new score is added.  
        `Add/Remove Range`: Used to add/remove scenarios to track, it is recommended to not change this setting unless you know what you are doing.  
    
    #### Aimlab
    1. Paste the link to your Aimlab Progress Sheet into the entryfield.
    2. Check the settings that you wish to use:  
        `Number of runs to average`: Amount of runs used to calculate the averages.  
        `Run Mode`: Types of updating the scores.  
         1. `watchdog`: Program will update sheet once a new score is added.  

6. The first time you run the program, you will be prompted to:

        1. Choose the account that owns your progress sheet.
        2. Click `Advanced` in the bottom-left, then `Go to Quickstart (unsafe)`.
        3. Click `Allow`.
        4. Click `Allow` again. A file called `token.pickle` will be saved to avoid future prompts.

- If you are encountering errors trying to go through the authentication flow when running the program for the first time (e.g. Google's `Something went wrong` error), this may be due to errors with cookies. Browsers like Firefox, as well as any extensions preventing cookie tracking, may end up preventing the authentication flow from fully completing. If this occurs, try doing the authentication flow through Chrome, and disabling any extensions that prevent cookie tracking.
        
## Build It Yourself

Windows with Python 3.7+,

```bash
$ git clone https://github.com/VoltaicHQ/Progress-Sheet-Updater
$ cd Progress-Sheet-Updater
$ pip install -r requirements.txt
```

Edit the paths in `main.spec` to match your setup:

```bash
$ pyinstaller main.spec main.py
```
