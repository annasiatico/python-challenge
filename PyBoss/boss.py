import os
import csv
import datetime

filepath = os.path.join("employee_data.csv")

with open(filepath, "r") as in_file:
    in_csv = csv.reader(in_file)

    header = next(in_csv)
    
    new_header = ["Emp ID", "First Name", "Last Name", "DOB ", "SSN", "State"]
   
    l = list(in_csv)
    
    def sortlist(element2):
        return element2[1]
    l.sort(key=sortlist)
    

    emp_id = [i[0] for i in l]


    names = [i[1].split(" ") for i in l]
    first_name = [i[0] for i in names]
    last_name = [i[1] for i in names]


    change_date = [datetime.datetime.strptime(i[2], '%Y-%m-%d').strftime('%m/%d/%Y') for i in l]
  

    change_SSN = [i[3][:0] + "***-**-" + i[3][7:] for i in l]

    
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

    change_state = [us_state_abbrev.get(i[4],'') for i in l]


    new_l = zip(emp_id, first_name, last_name, change_date, change_SSN, change_state)
    new_list = list(new_l)


with open('output.csv', 'w') as writetoFile:
    writer = csv.writer(writetoFile)
    writer.writerow(new_header)
    writer.writerows(new_list)

