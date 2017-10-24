import os
import csv

# Files to load and output (Remember to change these)
csvpath = os.path.join("raw_data", "test.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    candidates = {}

    for row in csvreader:
        if row[2] not in candidates.keys():
            candidates[row[2]] = 0
        candidates[row[2]] = candidates[row[2]] + 1
        
    #print(candidates)        

    total_votes=0

    for votes in candidates.values():
        total_votes = total_votes + votes
    print(" ")
    print("  ")
    print("         Election Results")
    print("------------------------------------------")
    print("   Total Votes : " + str(total_votes))
    print("------------------------------------------")

    for each, votes in candidates.items():
        rate = votes/total_votes
        print(each + " : " + '{:.1%}'.format(votes/total_votes) + " ( " + str(votes) + ")")
    print("------------------------------------------")
    print("  ")
    
    most_votes = 0
    for politician in candidates.keys():
        if candidates[politician] > most_votes:
            winner = politician
            most_votes= candidates[politician]
    print('The winner is : ' + winner) 
    print(" ")       
    print("------------------------------------------")
    
    
    
    
    
    print("  ")