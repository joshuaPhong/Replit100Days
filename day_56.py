# Read in the data.

# Categorize the songs by artist, like this:

# Create one empty folder per artist.

# Create one blank text file per song by that artist in the relevant folder. The file name of the text file should be
# the name of the song.

# import the csv library
import csv
import os

# read the file in
with open("100MostStreamedSongs.csv", encoding="utf-8") as mss:
    songs = csv.DictReader(mss)
    for row in songs:
        # create the artist and song variables
        artist = row["Artist(s)"].title()
        print(artist)
        song = row["Song"]
        print(song)
        # check if there is an artist folder in the directory
        if artist not in os.listdir():
            # create an artist folder

            os.mkdir(artist)

        # save the song to the folder
        path = os.path.join(f"{artist}/", song)
        file = open(path, "w")
        file.close()
