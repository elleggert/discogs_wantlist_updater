import discogs_client
import xml.etree.ElementTree as ET

# Will need to pass the user-specific token to the app to function accordingly
# Token can be generated under https://www.discogs.com/settings/developers



'''
print("Please enter your Discogs User-Token:")
userToken = input()


# Establishing an API connection and enabling API limiting
client = discogs_client.Client('WantlistEditor', user_token=userToken)
client.backoff_enabled = True

# Querying some example releases
results = client.search('Phylyps Trak II', type='release')
print(results.pages)
artist = results[0].artists[0]
print(artist.name)

me = client.identity()
print(me.name, me.username, me.location)
print(len(me.wantlist))
print(me.wantlist)
'''

# ==========Parsing Apple Music Library as XML

tree = ET.parse('MusicEE.xml')
root = tree.getroot()

song_database = []

for child1 in root:
    for child2 in child1:
        for child3 in child2:
            count = 0
            song = []
            for child4 in child3:
                if count == 3 or count == 5 or count == 9 or count == 50:
                    song.append(child4.text)
                count += 1

            print(song)

    exit()


# Find out how i can only acccess certain columns by name of the XML --> extract artist, title and album, nothing more

