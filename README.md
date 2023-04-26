# Instagram Follower Analysis

This Python script analyzes the followers and following data downloaded from an Instagram account to find out which accounts you follow that do not follow you back.

## Requirements

- Python 3.x
- BeautifulSoup4 library

## Usage

1. Download your data from Instagram. Go to settings, and then search download. Then request a download to your email.

2. Download the data from the email you get from instagram and un zip it.

3. Go into the `followers_and_following` folder and put the `follower_analysis.py` script into the directory.

4. Install the BeautifulSoup4 library by running the following command: `pip install beautifulsoup4`

5. Run the script by running the following command: `python3 follower_analysis.py`

6. The script will output a list of usernames of the accounts that you follow but do not follow you back.

## Notes

- If your downloaded HTML files have different names than `followers_1.html` and `following.html`, you can modify the file names in the `follower_analysis.py` script.

- The script uses the fact that all of the usernames are in hyperlink HTML tag, and takes all of the usernames in the hyperlink tags.
