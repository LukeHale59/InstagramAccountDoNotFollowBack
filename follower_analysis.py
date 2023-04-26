from bs4 import BeautifulSoup

# Read the HTML data from the files
with open('followers_1.html', 'r') as f:
    followers_html = f.read()
with open('following.html', 'r') as f:
    following_html = f.read()

# Parse the HTML data with Beautiful Soup
followers_soup = BeautifulSoup(followers_html, 'html.parser')
following_soup = BeautifulSoup(following_html, 'html.parser')

# Extract the usernames from the parsed HTML data
followers = [a.text for a in followers_soup.find_all('a')]
following = [a.text for a in following_soup.find_all('a')]

# Find the usernames who you follow but don't follow you back
not_following_back = set(following) - set(followers)

# Output the results
print('You are following {} accounts.'.format(len(following)))
print('{} accounts do not follow you back:'.format(len(not_following_back)))
for username in not_following_back:
    print(username)
