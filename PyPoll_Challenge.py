# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0

# Track Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track Winning Candidate and Winning Count Tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track County Count and Largest County Tracker
county_votes = {}
county_options = []
total_county_percentage = 0
county_results = ""
largest_county = 0
largest_county_percentage = 0
largest_county_turnout = ""

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        county_name = row[1]
        if county_name not in county_options:
           # Add the county name to the county list.
            county_options.append(county_name)

           # Begin tracking that county's vote count. 
            county_votes[county_name] = 0
            # Add a vote to that candidate's count.
        county_votes[county_name] += 1

        # Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    # Print the final vote count.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    
    for county in county_votes:
    # Retrieve vote count of a county.
        votes = county_votes[county]
    # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #print(county_results, end="")
        txt_file.write(county_results)
        #print(county_results, end="")
        #  Save the county results to our text file.
    
        if(votes > largest_county) and (vote_percentage > largest_county_percentage):
            largest_county= votes
            largest_county_percentage= vote_percentage
            largest_county_turnout = county
            largest_county_results =(
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_county_turnout}\n"
            f"-------------------------\n")
        
            #print(largest_county_turnout, end="")
        #  Save the county results to our text file.
    #txt_file.write(largest_county_turnout)
    #print(largest_county_turnout, end="\n")
    print(largest_county_results)
    txt_file.write(largest_county_results)
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
#with open(file_to_save, "w") as txt_file:
    #print("\n")
    #print(largest_county_turnout)
   
    for candidate in candidate_votes:
    # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
            #f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #print("-------------------------\n")
        txt_file.write(candidate_results)
        #print(max(vote_percentage))
    # Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
      
     # To do: print out each candidate's name, vote count, and percentage of
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)







   

