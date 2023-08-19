# # # PyPoll # # #


# Import the os module (allows to create file paths across operating system)
import os

# Imports CVS module
import csv

# Imports currency and date formatting
import locale

# Follows the file path
election_path = os.path.join("PyPoll","Resourses","election_data.csv")


# Dictionary creation (to hold the cadidates names) + starting values
Candidate_votes = {}
Votes = 0

# Open and read csv
with open(election_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Read the header row first
    header = next(csv_reader)

    # Foor loop trough the rows
    for row in csv_reader:
        Votes += 1
        if row[2] not in Candidate_votes :
            Candidate_votes [row[2]] = 1
        else:
            Candidate_votes [row[2]] += 1  

winner = max(Candidate_votes, key=Candidate_votes.get)


# PRINTS THE FOLLOWING VALUES TO TERMINAL:
'''
    The total number of votes cast
    A complete list of candidates who received votes
    The percentage of votes each candidate won
    The total number of votes each candidate won
    The winner of the election based on popular vote
'''

print(f"""Election Result
----------------------------
Total Votes: {Votes}
-------------------------""")
for candidate, votes in Candidate_votes.items():
        print(candidate + ": " + "{:.3%}".format(votes/Votes) + "   (" +  str(votes) + ")")

print(f"""----------------------------
Winner: {winner}
----------------------------
""")

# EXPORTS RESULTS TO TEXT FILE:

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(Votes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in Candidate_votes.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/Votes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
