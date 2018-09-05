#get em ready
import os
import csv
election_data=os.path.join('election_data.csv')

   #The total number of votes cast
with open (election_data,newline="") as totalcast_csv:
    totalcast_reader=csv.reader(totalcast_csv,delimiter=",")
    next(totalcast_reader,None)
    value=len(list(totalcast_reader))

#Rewrite CSV 2 be clean 2 read 
VoterID=[]
Candidate=[]
with open(election_data,newline="") as rewrite_csv:
    rewrite_reader=csv.reader(rewrite_csv,delimiter=",")
    for row in rewrite_reader:
        VoterID.append(row[0])
        Candidate.append(row[2])
cleaned_csv=zip(VoterID,Candidate)
output_file=os.path.join("clean_election_data")
with open(output_file,"w",newline="") as datafile:
    writer=csv.writer(datafile)
    writer.writerows(cleaned_csv)

#A complete list of candidates who received votes
candidates_captured=csv.reader(cleaned_csv,delimiter=",")
candidate_output=(row[1])
for x in names:
    if x not in candidate_output:

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

