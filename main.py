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

# Querying some the releases from the song database
results = client.search(song_database[0][0], artist=song_database[0][1], type='release')

master_id_set = set()

# For each result of a query, find the master release ID and add to a set of ids, this avoids iterating through the same
# master several times

for result in results:
    #Getting all the releases
    release = client.release(result.id)
    if release.master != None:
        release_master_id = release.master.id
        master_id_set.add(release_master_id)

    for release_version in release.master.versions:
        print(release_version)
        release_format = release_version.formats[0]
        print(release_format["name"])

print(master_id_set)

'''
    me = client.identity()
    print(me.name, me.username, me.location)
    print(len(me.wantlist))
    print(me.wantlist)
    '''
