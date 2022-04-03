# Script to create the session content files for Hugo from a csv file.

import csv
import os
with open('speakers.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        title = row['title']
        slug = row['slug']
        image = row['image']
        bio = row['bio']
        designation = row['designation']
        twitter = row['twitter']
        linkedin = row['linkedin']

        dirname = "speakers/"+slug
        try:
            os.mkdir(dirname)
        except FileExistsError:
            print("Dir "+dirname+" exists")
        except OSError:
            print ("Creation of the directory "+dirname+" failed" )
        else:
            print ("Successfully created the directory "+dirname)

        filename = dirname+"/_index.md"

        with open(filename, "w") as f:

            f.write("---\n")
            f.write("title: \""+title+"\"\n")
            f.write("designation: \""+designation+"\"\n")
            f.write("image: "+image+"\n")
            f.write("twitter: \""+twitter+"\"\n")
            f.write("linkedin: \""+linkedin+"\"\n")
            f.write("---\n\n")
            f.write(bio)


