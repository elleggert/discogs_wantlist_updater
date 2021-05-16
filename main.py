import discogs_client
import xml.etree.ElementTree as ET

# Will need to pass the user-specific token to the app to function accordingly
# Token can be generated under https://www.discogs.com/settings/developers




# ==========Parsing Apple Music Library as XML

# Creating an XML Parsetree
tree = ET.parse('MusicEE2.xml')
root = tree.getroot()


#Extracting all information from the XML on every song
song_database_full = []

for child1 in root:
    for child2 in child1:
        for child3 in child2:
            song = []
            for child4 in child3:
                song.append(child4.text)

            song_database_full.append(song)



# Reduce the information to only hold title and artist
song_database = []


for item in song_database_full:
    song = []
    for i in range(len(item)):
        if item[i] == "Name":
            song.append(item[i+1])
        if item[i] == "Artist":
            song.append(item[i+1])

    if len(song) == 2:
        song_database.append(song)



print("Please enter your Discogs User-Token:")
userToken = input()


# Establishing an API connection and enabling API limiting
client = discogs_client.Client('WantlistEditor', user_token=userToken)
client.backoff_enabled = True

# Generate a set with all release ids of a users wantlist
wantlist_ids = set()
me = client.identity()
for item in me.wantlist:
    wantlist_ids.add(item.id)


for i in range(5):
    # Querying some the releases from the song database
    print(song_database[i])
    results = client.search(song_database[i][0], artist=song_database[i][1], type='master')



    for master_release in results:

    # Iterating through master releases and adding all those that are vinyl to the wantlist, if they are not yet in it
        for release_version in master_release.versions:
            if release_version.id in wantlist_ids:
                continue
            release_format = release_version.formats[0]
            if release_format["name"] == "Vinyl":
                me.wantlist.add(release_version)

    exit()


