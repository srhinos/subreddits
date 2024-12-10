# Subreddits

## popular.txt ([link](https://jeffreyca.github.io/subreddits/popular.txt))
List of popular subreddits retrieved using [Reddit's popular subreddits API](https://www.reddit.com/dev/api/#GET_subreddits_{where}). Updated weekly.

To generate the list yourself, you'll need a Reddit app client ID and secret, which you can get by following these steps:

1. Sign into your Reddit account and go to https://reddit.com/prefs/apps
2. Click the `are you a developer? create an app...` button
3. Fill in the fields
    - Name: *anything*
    - Choose `Script`
    - Description: *anything*
    - About url: *anything*
    - Redirect uri: *anything* (e.g. `https://example.com`)

4. Click `create app`
5. After creating the app you'll get a **client ID** as well as a **secret**, which will both be a random string of characters.

### Generate using GitHub Actions
1. Set the following repository secrets ([guide](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)) to the values from previous step:
    - `REDDIT_CLIENT_ID`
    - `REDDIT_CLIENT_SECRET`
2. The GitHub Action "Update popular subreddits" is configured to run at 00:00 UTC on Sundays, but you can also manually trigger it.

### Generate from local machine
1. Install Python 3
2. `pip install -r requirements.txt`
3. Set the `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` environment variables
4. `python gen_popular.py`

## trending-apollo.txt ([link](https://jeffreyca.github.io/subreddits/trending-apollo.txt))
Original list of trending subreddits used by Apollo iOS app, extracted from `trending-subreddits.plist`. Last updated 2023-09-09.

## trending-reddstats-weekly.txt ([link](https://jeffreyca.github.io/subreddits/trending-reddstats-weekly.txt))
List of trending subreddits, sourced from [reddstats.com](https://reddstats.com/ranking/relative?over18=False&period=weekly&subscriber_classification=50001-100000).

* Growth period: weekly
* Subscribers: 10001-50000, 50001-100000, 100001-1000000
