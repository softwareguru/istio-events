# Script to create the session content files for Hugo from a csv file.

import csv
with open('sessions.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        slot = row['slot'].lower()
        title = row['title']
        url = row['url']
        speakers = row['speakers'].split(", ")
        time_start = row['start_utc']
        time_end = row['end_utc']
        session_type = row['type']
        language = row['language']
        abstract = row['abstract']


        filename =  "sessions/"+slot+".md"
        with open(filename, "w") as f:
            f.write("---\n")
            f.write("id: "+slot+"\n")
            f.write("title: \""+title+"\"\n")
            f.write("url: "+url+"\n")
            f.write("speakers:\n")
            for s in speakers:
                f.write(" - "+s+"\n")
            f.write("time_start: "+time_start+"\n")
            f.write("time_end: "+time_end+"\n")
            f.write("block: "+slot[0:1]+"\n")
            f.write("slot: "+slot[1:2]+"\n")
            f.write("format: "+session_type+"\n")
            f.write("language: "+language+"\n")
            f.write("---\n\n")
            f.write(abstract)


