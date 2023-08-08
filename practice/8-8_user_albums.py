def make_album(artist_name, album_title, songs_number=None):
    album = {'name': artist_name, 'title': album_title,}
    if songs_number:
        album['songs'] = songs_number
    return album

while True:
    print("Enter the album's artist name and title!")
    print("(enter 'q' anytime to quit)")
    
    a_name = input("Artist name: ")
    if a_name == 'q':
        break  
    a_title = input("Album's title: ")
    if a_title == 'q':
        break
    
    user_album = make_album(a_name, a_title)
    print(user_album)