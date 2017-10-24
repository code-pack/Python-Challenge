import os
import csv

# request file names for input and output, declair the subfolder for holding the data
# If i had time I would add an IF statement to prompt again if file not found

input_file = input(" Please enter the name of the data file: ")
csvpath = os.path.join("raw_data", input_file)

# open the data file into the csv reader

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#initiate the dictionary that will hold the vote count

    candidates = {}

# loop through the data, adding the candidates and running a vote count 
# for each (held as value to the candidate Key)

    for row in csvreader:
        if row[2] not in candidates.keys():
            candidates[row[2]] = 0
        candidates[row[2]] = candidates[row[2]] + 1
        
    # set a total vote variable and count the votes for each candidate in the dictionary 
    # probably more efficient to run this in the loop that loads the data, but due to the 
    # limited size of the dictionary I wanted to keep the steps seperated         

    total_votes=0

    for votes in candidates.values():
        total_votes = total_votes + votes

   # Output formating for the election results 

    print(" ")
    print("  ")
    print("         Election Results")
    print("------------------------------------------")
    print("   Total Votes : " + str(total_votes))
    print("------------------------------------------")

   # calculate and format the candidates percentage of total votes

    for each, votes in candidates.items():
        rate = votes/total_votes
        print(each + " : " + '{:.1%}'.format(votes/total_votes) + " ( " + str(votes) + ")")
    print("------------------------------------------")
    print("  ")

   # to determin the winner, loop through the candidates setting the candidate
   # with the most votes as the winner

    most_votes = 0
    for politician in candidates.keys():
        if candidates[politician] > most_votes:
            winner = politician
            most_votes= candidates[politician]

    print('The winner is : ' + winner) 
    print(" ")       
    print("------------------------------------------")
    print("  ")