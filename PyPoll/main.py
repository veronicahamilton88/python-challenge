# Import
import os
import csv

# Connect the data file
election_data = os.path.join('election_data.csv')

# Open and read csv file
with open(election_data,'r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    
    # Define our variables
    total_votes = 0
    candidate_list = []
    percent_won = 0.0
    votes = 0
    total_votes_won = 0.0
    winner = ""
    candidate_name = ""
    candidate_detail = {}
    candidate_percentage = {}
    winner_votes = 0
    
    # Skip the header row
    next(election_data)
    
    # Define all the rows of data
    for row in election_data:
        voter_id = row[0]
        county = row[1]
        candidate_name = row[2]
        total_votes +=1
        

        # FIND OUT HOW MANY VOTES EACH CANDIDATE RECEIVED AND ADD TO DICTIONARY
        # If the candidate name appears in the candidate deail
        if candidate_name in candidate_detail:
            # Count the candidate name as a vote
            votes = candidate_detail.get(candidate_name)
            # Increase the vote count by 1
            votes +=1
            # Add the number of votes to the dictionary
            candidate_detail[candidate_name] = votes
        else:
            # If the candidate name only appears once, it just counts as 1 vote
            candidate_detail[candidate_name] = 1    
     
    
    # FIND THE PERCENTAGE WON
    # Locating each candidate name in the candidate detail
    for candidate_name in candidate_detail:
        # Counting each isntance of candidate name as 1 vote
        votes = candidate_detail.get(candidate_name)
        # Percentage calculation
        percent_won = (votes/total_votes) * 100
        # Adding the percentage won to the dictionary
        candidate_percentage[candidate_name] = percent_won
        
        # FIND THE WINNER
        
        if votes > winner_votes:
            winner = candidate_name
            winner_votes = votes
        
    # MAKE THE SUMMARY
    print('Election Results')
    print('-------------------------')
    # The total number of votes cast
    print(f'{"Total Votes: "} {total_votes}')
    print('-------------------------')

    for candidate_name in candidate_percentage:
        print(f'{candidate_name} : {round(candidate_percentage.get(candidate_name),1)}% ({candidate_detail.get(candidate_name)})')
    print('-------------------------')
    print(f'Winner: {winner}')
