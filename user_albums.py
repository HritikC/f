def make_album(artist_name,album_title,tracks=0):
    """Return a dictonary of information about an album."""
    album = {'name' : artist_name.title() ,'title' : album_title.title() }
    if tracks:
        album['tracks'] = tracks
    return album    

while True:
    title = input("\nWhat album are you thinking of ")
    if title == 'quit':
        break
    artist = input("who's the artist?")
    if artist == 'quit':
        break

    album = make_album(artist,title)
    print(album)

print("\nThanks for responding!")    s