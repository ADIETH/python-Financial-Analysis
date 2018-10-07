# First part should be importing the OS module to create mechanism to create file path across op
import os 

# call module to read CSv files
import csv

# provide location to load the source data for analysis and to store the analysis report
Pypoll = os.path.join('Resources', 'election_data.csv')
Out_put_file = os.path.join('Report', 'election_results.txt')


# create list to store data
Count = 0
Candidate_List = []
Unique_Candidate = []
Vote_Count = []
Vote_Percent = []

# extract the data from CSV file and assign it into a list of Dictionaries
with open(Pypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 

    # Conduct the count 
    for row in csvreader:
        # count the total votes
        Count = Count + 1
        # Add candidate name to candidate name list
        Candidate_List.append(row[2])
        # create a set from the candidate list to get the unique candidate name
    for A in set(Candidate_List):
        Unique_Candidate.append(A)
        # B represent total number of votes for each candidate
        B = Candidate_List.count(A)
        Vote_Count.append(B)
        # C represent percent of total votes for each candidate
        C = (B/Count)*100
        Vote_Percent.append(C)
        # Calculate winner and winning vote
        Winning_Vote_Count = max(Vote_Count)
        Winner = Unique_Candidate[Vote_Count.index(Winning_Vote_Count)]


print("------------------------------")
print("Election Results")
print("------------------------------") 
print("Total Votes:" + str(Count))
print("------------------------------")
for i in range(len(Unique_Candidate)):
            print(Unique_Candidate[i] + ": " + str(Vote_Percent[i]) +"%  (" + str(Vote_Count[i])+ ")")
print("-----------------------------")
print("Winner :" + Winner)
print("-----------------------------")   


#  Open the result file

with open(Out_put_file, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(Count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(Unique_Candidate))):
        text.write(Unique_Candidate[i] + ": " + str(Vote_Percent[i]) +"% (" + str(Vote_Count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write(" winner : " + Winner + "\n")
    text.write("---------------------------------------\n")
