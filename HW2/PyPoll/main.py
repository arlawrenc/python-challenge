#import dependencies
import os
import csv

#define csv path
working_csv = os.path.join('Resources', 'election_data.csv')

#open csv
with open(working_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # as the csv file contains a header, read the header row first
    csv_header = next(csvreader)
#store lists
    voter_id_list = []
    county_list = []
    name_list = []
    khan_list = []
    correy_list = []
    li_list = []
    otooley_list = []
#set initial variables to zero
    row_count = 0
#loop through data
    for row in csv.reader(csvfile):
    #append the voter id list
        voter_id_list.append(row[0])
    #append the county list
        county_list.append(row[1])
    #append the candidate list
        name_list.append(row[2])
    #determine number of rows
        row_count += 1
    #append candidate votes to their corresponding list
        if (row[2] == "Khan"):
            khan_list.append(row[2])
        elif (row[2] == "Correy"):
            correy_list.append(row[2])
        elif (row[2] == "Li"):
            li_list.append(row[2])
        else:
            otooley_list.append(row[2])

#define totals
vote_total = len(voter_id_list)
khan_total = len(khan_list)
correy_total = len(correy_list)
li_total = len(li_list)
otooley_total = len(otooley_list)

# calculate percentage of votes for each candidate
khan_percent = khan_total / vote_total
correy_percent = correy_total / vote_total
li_percent = li_total / vote_total
otooley_percent = otooley_total / vote_total

#determine winner
if khan_total > correy_total and li_total and otooley_total:
 	election_winner = "Khan"
elif correy_total > li_total and otooley_total:
 	election_winner = "Correy"
elif li_total > otooley_total:
  	election_winner = "Li"
else:
  	election_winner = "O'Tooley"

# determine file path to write to
output_file = os.path.join('analysis', 'analysis.txt')

# write file
with open(output_file, 'w',) as txtfile:

# Output into text file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {vote_total}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Khan: {khan_percent:.3%} ({khan_total})\n")
    txtfile.write(f"Correy: {correy_percent:.3%} ({correy_total})\n")
    txtfile.write(f"Li: {li_percent:.3%} ({li_total})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%} ({otooley_total})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {election_winner}\n")
    txtfile.write(f"---------------------------\n")




# optional knowledge

# create a dictionary for candidate [key] and total votes for each [value]
#candidate_votes = {}

# loop through candidates, set total votes for each to 0
#for cand in candidates:
  #	candidate_votes[cand] = 0
    
# loop through candidates again, this time adding 1 vote each
#for vote in votes:
  	#candidate_votes[vote] += 1
    
# determine the winner based on key and value pair
#winner_votes = 0
#winner_name = ""
#for key, value in candidate_votes.item():
 # 	if value > winner_votes:
  #    	winner_votes = value
   #     winner_name = key

# print winner name
#print(f"Winner: {winner_name}")