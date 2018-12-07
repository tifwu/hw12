
import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []

def init():
    global entries, next_id
    next_id = 0
    
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def get_id():
    global next_id
    return next_id

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    
    max_id = 0
    if len(entries)!=0:
        for i in entries:
            if int(i['id']) > max_id:
                max_id = int(i['id'])
        next_id = max_id + 1
            
    
    entry = {"id": str(next_id), "author": name, "text": text, "timestamp": time_string}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
        

def delete_entry(delete_id):
    global entries, GUESTBOOK_ENTRIES_FILE
    
    entries = [d for d in entries if d.get('id') != delete_id]
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
            
