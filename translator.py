import json
import time
import sys


l_to_e = {}
e_to_l = {}
language = ""
auto_load = False
file = open("config.txt", "r")
data = file.read()
file.close()
exec(data)
if language == "none set":
    language = input("hello! sorry to bother, but no language has been set yet!\nplease enter a language (you will only have to do this once)\nlanguage: ")
    file = open("config.txt", "w")
    file.write("language = '" + language + "'\nauto_load = " + str(auto_load))
    file.close()
    print(language + " is now your language!")
def load_json():
    global l_to_e
    global e_to_l
    file = open("library.json", "r")
    data = file.read()
    file.close()
    l_to_e = json.loads(data)
    for language, english in l_to_e.items():
        e_to_l[english] = language
def load():
    print("loading data")
    try:
        load_json()
        print("sucsess")
    except Exception:
        print("an error occured while loading data!\nfile probably has been tamperd with")
        time.sleep(3)
        print("giving up", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".")
        print("goodbye!")
        time.sleep(1)
        sys.exit(1)
if auto_load:
    load()
while True:
    rq = input("->")
    keyword = rq.split(" ")[0]
    if rq == "load data" or rq == "load":
        load()
    if keyword.lower() == "find":
        sucsess = False
        string = ""
        word = rq.split()
        loop = 0
        word.remove(word[0])
        for char in word:
            loop += 1
            string = string + char
            if not loop == len(word):
                string = string + " "
        word = string
        for key, val in l_to_e.items():
            if word == key:
                print(key + " = " + val)
                sucsess = True
        for key, val in e_to_l.items():
            if word == key:
                print(key + " = " + val)
                sucsess = True
        if not sucsess:
            print("no matches found!")
    if keyword.lower() == "add":
        eng = input("word in english = ")
        lang = input("word in " + language + " = ")
        e_to_l[eng] = lang
        l_to_e[lang] = eng
        file = open("library.json", "w")
        file.write(json.dumps(l_to_e))
        file.close()
    if rq.lower() == "change language":
        language = input("please enter the name of the language you wish to change to\n--|")
        file = open("config.txt", "w")
        file.write("language = '" + language + "'\nauto_load = " + str(auto_load))
        file.close()
        print("language sucsessfully changed to " + language)
    if rq.lower() == "help":
        print("commands:\n'add' - add a new word\n'find (word)' checks for matches in your database, does not matter if the word is in english or you're language\n'load' - this loads your data, does not matter unless auto load is off\n'change language' - changes your language")