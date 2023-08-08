def make_album(artist_name, album_title, songs_number=None):
    album = {'name': artist_name, 'title': album_title,}
    if songs_number:
        album['songs'] = songs_number
    return album

mj = make_album('michael jackson', 'billie jeans')
print(mj)

eraser_heads = make_album('eraser heads', 'alapaap')
print(eraser_heads)

parokya_ni_edgar = make_album('edgar', 'buloy', 20)
print(parokya_ni_edgar)