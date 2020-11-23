import json
import csv

input_file=open('topics_json_file.json', 'r')
records = {}
records=json.load(input_file)

qfname = "qrel.txt"
with open(qfname, encoding = "utf8") as f:
        qrels = f.readlines()

main_list = []
row_list = []
my_dict = {}
temp_list = []

for record in records:
    for line in qrels:
        my_dict = {}
        temp_list = []
        words = line.split()
        # print(words[3])
        if words[0] == record['topic_number']:
            if words[3] != "0":
                record['doc_id'] = words[2]
                record['topic_number'] = record['topic_number'] 
                record['rel_score'] = words[3]
                my_dict = record
                main_list.append(my_dict)
                
                temp_list.append(words[0])
                temp_list.append(words[2])
                temp_list.append(words[3])
                temp_list.append(record['query'])
                temp_list.append(record['question'])
                temp_list.append(record['narrative'])
                row_list.append(temp_list)


with open('final_covid_data.json', 'w') as fout:
   json.dump(main_list, fout)

with open('final_covid_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["topic number", "doc id", "relevance score", "query", "question","narrative"])
    writer.writerows(row_list)

print("Data Ready in CSV and JSON form")