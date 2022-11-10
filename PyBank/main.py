
import os
import csv 

budget_path=os.path.join("Resource", "budget_data.csv")

with open(budget_path, "r") as budgetdata:
    csvreader=csv.reader(budgetdata, delimiter=",")
      
    csv_header =next(csvreader)   
    first_month = next(csvreader)

    first_mo_pro_loss = float(first_month[1])
    prev_mo_pro_loss = first_mo_pro_loss

    counter = 1
    net = float(first_month[1])
    changesum = 0
    
    
    for row in csvreader:

        net = net + float(row[1])

        change = float(row[1]) - prev_mo_pro_loss
        prev_mo_pro_loss = float(row[1])
        changesum= changesum + change
        
        if counter == 1:
            max_change = change
            max_change_month= row[0]

        if counter == 1:
            min_change = change
            min_change_month= row[0]

        counter= counter +1
   
        if max_change < change:
            max_change = change
            max_change_month = row[0]

        if min_change > change:
            min_change = change
            min_change_month = row[0]
    
    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months : {counter}")
    print(f"Total : ${net}")
    print(f"Average Change: {round(changesum / (counter-1), 2)}")
    print(f"Greatest Increase in Profit : {max_change_month} and ${round(max_change)}")
    print(f"Greatest Decrease in Profit : {min_change_month} and ${round(min_change)}")
     
output_path =os.path.join("analysis" ,"Analysis.txt")  

with open(output_path, "w") as resultwriter:
    csvwriter=csv.writer(resultwriter,delimiter="," )

    csvwriter.writerow(["Financial Analysis"]  )
    csvwriter.writerow(["--------------------------------" ])
    csvwriter.writerow([f"Total Months : {counter}"] )
    csvwriter.writerow([f"Total : ${net}" ] )
    csvwriter.writerow([f"Average Change: {round(changesum / (counter-1), 2)}"] )
    csvwriter.writerow([f"Greatest Increase in Profit : {max_change_month} and ${round(max_change)}"]  )
    csvwriter.writerow([f"Greatest Decrease in Profit : {min_change_month} and ${round(min_change)}"]  )

