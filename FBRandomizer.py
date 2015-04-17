#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: MaYaSeVeN
import random, time, urllib2, json, ctypes

print "\n=== Facebook Share Reward Randomizer ===\n"
print "\n!!! For PlearnGaming Tropico 4 Steam Special Edition !!! \n"
print "Original code by : MaYaSeVeN\n"

accessToken = "[USE YOUR OWN]" #Censor

posts = ["563057647168033"] #Array of post id

candidates = []

for postID in posts:
    candidatesLike = []
    candidatesShare = []
    candidatesFromPostShare = "https://graph.facebook.com/" + postID + "/sharedposts?limit=1000&access_token=" + accessToken
    candidatesShareJson = json.load(urllib2.urlopen(candidatesFromPostShare))
    for candidatesShareNumber in range(len(candidatesShareJson["data"])):
        nameOfCandidateShare = candidatesShareJson["data"][candidatesShareNumber]["from"]["name"]
        idOfCandidate = candidatesShareJson["data"][candidatesShareNumber]["from"]["id"]
        candidatesShare.append((nameOfCandidateShare, idOfCandidate))

    print "PostID = " + postID
    #candidates = candidates + [candidate for candidate in candidatesShare]
    candidates = candidatesShare

time.sleep(4)
print "\nTrying to choose the winners\n"

time.sleep(7)
print "Congratulations to \n"
winner = random.choice(candidates)
print "[+] " + winner[0] + "\n"
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(0, 'The winner is ' + winner[0] + ' FBID : ' + winner[1], '' , 0)
