import os
import csv
voter_id=[]
candidate=[]
candidate_list=[]
total_votes=0
candidate_votes=[]
winner=""
election_data=os.path.join('election_data.csv')
with open (election_data,newline="") as election_csv:
    election_reader=csv.reader(election_csv,delimiter=",")
    next(election_reader,None)
    for row in election_reader:
        total_votes +=1
        voter_id.append(row[0])
        candidate.append(row[2])
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
#number of candidates
candidate_1=[name for name in candidate if name == candidate_list[0]]
candidate_2=[name for name in candidate if name == candidate_list[1]]
candidate_3=[name for name in candidate if name == candidate_list[2]]
candidate_4=[name for name in candidate if name == candidate_list[3]]

#candidate total/percentage
candidate_1_total=len(candidate_1)
candidate_votes.append(candidate_1_total)
candidate_1_percent=float((candidate_1_total/total_votes)*100)
candidate_2_total=len(candidate_2)
candidate_votes.append(candidate_2_total)
candidate_2_percent=float((candidate_2_total/total_votes)*100)
candidate_3_total=len(candidate_3)
candidate_votes.append(candidate_3_total)
candidate_3_percent=float((candidate_3_total/total_votes)*100)
candidate_4_total=len(candidate_4)
candidate_votes.append(candidate_4_total)
candidate_4_percent=float((candidate_4_total/total_votes)*100)

#find winner
if max(candidate_votes)==candidate_1_total:
    winner=candidate_list[0]
elif max(candidate_votes)==candidate_2_total:
    winner=candidate_list[1]
elif max(candidate_votes)==candidate_3_total:
    winner=candidate_list[2]
else:
    winner=candidate_list[3]

#print em up 
print("Election Results")
print("--------------------")
print(f"Total Votes: {total_votes}")
print(f"{candidate_list[0]}: {candidate_1_percent} % ({candidate_1_total})")
print(f"{candidate_list[1]}: {candidate_2_percent} % ({candidate_2_total})")
print(f"{candidate_list[2]}: {candidate_3_percent} % ({candidate_3_total})")
print(f"{candidate_list[3]}: {candidate_4_percent} % ({candidate_4_total})")
print(f"Winner: {winner}")