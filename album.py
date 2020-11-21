def make_album(artist_name,album_title,tracks=0):
    """Return a dictonary of information about an album."""
    album = {'name' : artist_name ,'title' : album_title }
    if tracks:
        album['tracks'] = tracks
    return album    

album = make_album('chester','linkin park')
print(album)

album = make_album('bettew','kiss')
print(album)

album = make_album('naina','prem',9)
print(album)