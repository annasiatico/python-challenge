import os
import csv
import datetime
import csv 

filepath = os.path.join("employee_data.csv")

with open(filepath, "r") as in_file:
    in_csv = csv.reader(in_file)

    header = next(in_csv)
    # print (header)
    new_header = ["Emp ID", "First Name", "Last Name", "DOB ", "SSN", "State"]
    # print (new_header)

    l = list(in_csv)
    

    def sortlist(element2):
        return element2[1]
    l.sort(key=sortlist)
    

    # print (l)

    emp_id = [i[0] for i in l]
    # print (emp_id)

    names = [i[1].split(" ") for i in l]
    first_name = [i[0] for i in names]
    last_name = [i[1] for i in names]


    # first_name = names[:][0]
    # last_name = names[:][1]
    # print (names)

    change_date = [datetime.datetime.strptime(i[2], '%Y-%m-%d').strftime('%m/%d/%Y') for i in l]
    # print (change_date)

    change_SSN = [i[3][:0] + "***-**-" + i[3][7:] for i in l]
    # print (change_SSN)

    
    
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
    # print (change_state)

    new_l = zip(*(emp_id, first_name, last_name, change_date, change_SSN, change_state))
    new_list = list(new_l)
    # new_list[0] = new_header
    
    # print (new_list)


with open('output.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(new_list)

# readFile.close()
# writeFile.close()

# from itertools import zip_longest

# export_data = zip_longest(*new_list, fillvalue = '')
# with open('output.csv', 'w', newline='') as myfile:
#       wr = csv.writer(myfile)
#       wr.writerow(export_data)
#       for val in new_list:
#             wr.writerow(val)
#     #   wr.writerows(export_data)
# myfile.close()
    

# with open("ouput.csv","w",newline="") as file_writer:

# #    fields = new_header

#     writer = csv.DictWriter(file_writer,fieldnames=new_header)

#     writer.writeheader()

#     for row in new_list:
#         writer.writerow({"Emp ID": emp_id, "First Name": first_name, "Last Name": last_name, "DOB ": change_date, "SSN": change_SSN, "State": change_state})

#    writer = csv.writer(file_writer)

#    print (new_header)
    # for row in new_l:
    #     writer.writerow(row)

# with open("ouput.csv", "w") as f:
#     writer = csv.writer(f)
#     for row in new_l:
#         writer.writerow(row)


#    writer.writerow({"Emp ID": emp_id, "First Name": names[0], "Last Name": names[1], "DOB ": change_date, "SSN": change_SSN, "State": change_state})
    