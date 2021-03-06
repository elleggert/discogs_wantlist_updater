import discogs_client
import xml.etree.ElementTree as ET
import argparse

# Will need to pass the user-specific token to the app to function accordingly
# Token can be generated under https://www.discogs.com/settings/developers

parser = argparse.ArgumentParser(description='Discogs Wantlist Updater',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', '--path_to_data', default='ra_june.xml', metavar='', type=str,
                        help='path to the  file containing the XML exported from Itunes')

parser.add_argument('-d', '--discogs_api_token', default='NA', metavar='', type=str,
                        help='discogs API token, if not provided, will be queried as user input')

args = vars(parser.parse_args())
path_to_xml = args['path_to_data']
userToken = args['discogs_api_token']

# ==========Parsing Apple Music Library as XML

# Creating an XML Parsetree
tree = ET.parse(path_to_xml)
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


if userToken == 'NA':
    print("Please enter your Discogs User-Token:")
    userToken = input()


# Establishing an API connection and enabling API limiting
client = discogs_client.Client('WantlistEditor', user_token=userToken)
client.backoff_enabled = True

# Generate a set with all release ids of a users wantlist
wantlist_ids = set()
me = client.identity()


songs_added_count = 0
for i in range(len(song_database)):
    # Querying some the releases from the song database
    results = client.search(song_database[i][0], artist=song_database[i][1], type='master')


    index = 0
    for master_release in results:

        if index > 5:
            break
    # Iterating through master releases and adding all those that are vinyl to the wantlist, if they are not yet in it
        for release_version in master_release.versions:
            if release_version.id in wantlist_ids:
                continue
            try:
                release_format = release_version.formats[0]
            except:
                continue
            if release_format["name"] == "Vinyl":
                songs_added_count += 1
                me.wantlist.add(release_version)

        index += 1


    if (i % 25 == 0):
        print(i, "of ", len(song_database), "songs parsed")
        print(songs_added_count)
