
import wikipedia
import sqlite3

#wikipedia searches
userinput = raw_input("Which famous person are you looking for?\n")
def search(value):
  return wikipedia.search(value, results=1)

research = wikipedia.suggest(userinput)
if research == None:
    research = search(userinput)
    
else:
    print("I don't know this person. Did you mean " + research + " ?\n")
    research = search(research)
    

print("Here is what we found: " + str(research))
summary = wikipedia.summary(research) 

#database queries
def sendtodb(research, summary):
    try:
        con = sqlite3.connect('wiki.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS famous_people
                    (name TEXT, summary TEXT)""")
        cur.execute("""INSERT INTO famous_people(name, summary)
                    VALUES(?, ?)""", (research, summary))
        con.commit()
        cur.close()
        print("Amazing, " + research + " has been added!")

    except sqlite3.Error as error:
        print("Oops it seems there was an error while sending data...", error)

    finally:
        if con:
            con.close()
            print("End of process")

sendtodb(research[0], summary)
