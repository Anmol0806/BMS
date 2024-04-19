import pandas as pd
import datetime

df = pd.read_csv('data.csv');

def add_row(dataframe, cname, oname, date, q):
    new_id = len(dataframe) + 1 
    new_row = pd.DataFrame({'id': [new_id], 'cname': [cname], 'oname': [oname], 'date': [date], 'q': [q]})
    dataframe = pd.concat([dataframe, new_row], ignore_index=True)
    return dataframe

def update_data_by_id(dataframe, id_to_update, new_cname, new_oname, new_date, new_q):
    dataframe.loc[dataframe['id'] == id_to_update, 'cname'] = new_cname
    dataframe.loc[dataframe['id'] == id_to_update, 'oname'] = new_oname
    dataframe.loc[dataframe['id'] == id_to_update, 'date'] = new_date
    dataframe.loc[dataframe['id'] == id_to_update, 'q'] = new_q
    return dataframe
    
def update_value_by_id(dataframe, id_to_update, column_name, new_value):
    dataframe.loc[dataframe['id'] == id_to_update, column_name] = new_value
    return dataframe 

def date_format(date_string):
    parsed_date = datetime.datetime.strptime(date_string, "%d-%m-%Y").date()
    formatted_date = parsed_date.strftime("%d-%m-%Y")
    return formatted_date
 
date_string = "07-12-2025"

print(date_format(date_string))

df.to_csv('data.csv', index=False)
print(df.to_string(index=False))

# 1. add data 
# 2. retrive data with id 
# 3. update data 
#       1. id , new data. 
#       2. id , column name , column value. 
# 4. show all data 