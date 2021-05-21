# discogs_wantlist_updater

Small Automation Program automatically adding music from your Itunes Library into your Discogs Wantlist to facilitate Online Record Shopping on Discogs.

Program parses the Library exported as XML, extracts information on artists and title and gets the users current wantlist. 

Afterwards, master releases that contain the titles from the Itunes Library are queried from the Discogs API and every Vinyl Release is added to the wantlist.

Note: Only works with Apple Music or Itunes so far, no spotify compatibility.
