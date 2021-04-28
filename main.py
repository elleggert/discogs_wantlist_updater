import discogs_client

# Will need to pass the user-specific token to the app to function accordingly
# Token can be generated under https://www.discogs.com/settings/developers


print("Please enter your Discogs User-Token:")
userToken = input()

client = discogs_client.Client('WantlistEditor', user_token=userToken)
results = client.search('Phylyps Trak II', type='release')
print(results.pages)
artist = results[0].artists[0]
print(artist.name)

