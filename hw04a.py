import requests
import json
from urllib.request import urlopen


def userrepos(username):
    if not isinstance(username, str):
        return "Username is not valid"
    url="https://api.github.com/users/USER/repos"
    newurl= url[:29]+ username+url[33:]
    try:
        userdata = urlopen(newurl)
        repolist=[]
        data = json.loads(userdata.read())
        for i in data:
            repolist.append(str(i['name']))
        return repolist
    except:
        return("User Does Not Exist Error")



def repocommits(username, repo):
    if not isinstance(repo, str):
        return "Repo is not valid"
    url="https://api.github.com/repos/USER/repos/commits"
    newurl= url[:29]+ username+url[33]+repo+url[39:]
    try:
        userdata = urlopen(newurl)
        commitlist=[]
        data = json.loads(userdata.read())
        for i in data:
            commitlist.append(str(i['commit']))
        numcommits=len(commitlist)
        return("Number of commits: " ,numcommits)
    except:
        return("Repo does not exist")

def combined(username,repo):
    if(userrepos(username)=="User Does Not Exist Error"):
        return "User Does Not Exist Error"
    return repocommits(username,repo)

