#get em ready
import os
import csv
election_data=os.path.join('election_data.csv')

#The total number of votes cast
with open (election_data,newline="") as totalcast_csv:
    totalcast_reader=csv.reader(totalcast_csv,delimiter=",")
    next(totalcast_reader,None)
    value=len(list(totalcast_reader))

#A complete list of candidates who received votes
with open (election_data,newline="") as candidates_csv:
    candidates_reader=csv.reader(candidates_csv,delimiter=",")
    next(candidates_reader,None)
    

#The percentage of votes each candidate won
#with open (election_data,newline="") as percentagewon_csv:
   #percentagewon_reader=csv.reader(percentagewon_csv,delimiter=",")
   #next(percentagewon_reader,None)

#The total number of votes each candidate won
#with open (election_data,newline="") as totalwon_csv:
    #totalwon_reader=csv.reader(totalwon_csv,delimiter=",")
    #next(totalwon_reader,None)

#The winner of the election based on popular vote.
#print em up 
print("Election Results")
print("--------------------")
print(f"Total Votes: {value}")

