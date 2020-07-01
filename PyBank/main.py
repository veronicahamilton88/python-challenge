# Connect the data file
budget_data = os.path.join('budget_data.csv')

# Open and read csv file
with open(budget_data,'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(budget_data)
    
    # Define our variables
    total_months = 0
    max_return = 0.0
    min_return = 0.0
    month_max_return = ""
    month_min_return = ""
    
    # Loop through the rows in budget_data to find what we need
    for row in budget_data:
        total_months +=1
        date = row[0]
        # Cast the string value to float
        profit_loss = float(row[1])
        # Find the total profit/loss of all
        total_profit_loss = total_profit_loss + profit_loss
        # Find monthly return
        if total_months != 1:
            monthly_return = profit_loss - previous_row_profit_loss
            return_list.append(monthly_return)
            # Check the next value against the previous max return
            # If it is greater than the previous max return, make it the new max return
            # If it is not greater than the previous max return, keep the same max return value
            if monthly_return > max_return:
                month_max_return = date
                max_return = monthly_return
            # Same function as max return, but for min
            if monthly_return < min_return:
                month_min_return = date
                min_return = monthly_return
        else:
            monthly_return = 0
            
        # Total returns calculation
        # total_return = total_return + monthly_return
        # Reset previous row
        previous_row_profit_loss = profit_loss

    file = open('Financial Summary.txt','w')
    file.write(f'Financial Summary- \n')
    file.write(f' Total Months:  {total_months} \n')
    file.write(f' Total: ${round(total_profit_loss)} \n')
    file.write(f' Average Change: ${round((sum(return_list))/len(return_list),2)} \n')
    file.write(f' Greatest Increase in Profits: {month_max_return}  "($"{round(max(return_list))}")" \n')
    file.write(f' Greatest Decrease in Profits: {month_min_return} "($"{round(min(return_list))}")" \n')
    file.close()
