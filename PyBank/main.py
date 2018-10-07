# First part should be importing the OS module to create mechanism to create file path across operating system
import os

# call module to read CSv files
import csv

# provide location to load the source data for analysis and to store the analysis report
File_to_Load = os.path.join('Resources', 'budget_data.csv')
Out_put_file = os.path.join('Report', 'budget_repot.txt')

# Setting parameters for the Analysis
Total_Months = 0
previous_Revenue = 0
Month_change = []
Revenue_Change_List = []
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 9999999999999999999]
Total_Revenue = 0


# extract the data from CSV file and assign it into a list of Dictionaries
with open(File_to_Load) as budget_data:
    reader = csv.DictReader(budget_data)

    for row in reader:

        # Trace Total months and Revenue
        Total_Months = Total_Months + 1
        Total_Revenue = Total_Revenue + int(row["Profit/Losses"])

        # Trace the changes for revenue and duration
        Revenue_Change = int(row["Profit/Losses"]) - previous_Revenue
        previous_Revenue = int(row["Profit/Losses"])
        Revenue_Change_List = Revenue_Change_List + [Revenue_Change]
        Month_change = Month_change + [row["Date"]]

        # Determine Greatest increase and decrease in profit/losses  over the entire period
        if (Revenue_Change > Greatest_Increase[1]):
            Greatest_Increase[0] = row["Date"]
            Greatest_Increase[1] = Revenue_Change

        if (Revenue_Change < Greatest_Decrease[1]):
            Greatest_Decrease[0] = row["Date"]
            Greatest_Decrease[1] = Revenue_Change

        # Trace Average Revenue Change
        Average_Revenue = sum(Revenue_Change_List) / len(Revenue_Change_List)

        # Generate Report 
        output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total Revenue: ${Total_Revenue}\n"
    f"Average Change: ${Average_Revenue}\n"
    f"Greatest Increase in Revenue: {Greatest_Increase[0]} (${Greatest_Increase[1]})\n"
    f"Greatest Decrease in Revenue: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(Out_put_file, "w") as txt_file:
    txt_file.write(output)





