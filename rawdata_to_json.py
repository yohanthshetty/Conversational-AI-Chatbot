import json

# input_file = open('patient_doctor_dialogue.txt', 'r')
# output_file = open('conversation_in_json_format.json', 'w')

with open('patient_doctor_dialogue.txt', encoding= 'utf-8') as file1:
    input_text = file1.readlines()


desc_flag = False
dialog_flag = False
patient_flag = False
doctor_flag = False

patient_list = []
doctor_list = []

main_list = []

# main_dict = {}
my_dict = {}
dialog_dict = {}
count = 0
patient_convo = ""
doctor_convo = ""
for line in input_text:
    line = line.replace('\n',"")
    if line == '':
        continue
    if line[0:3] == "id=":
        # print(main_list)
        if len(doctor_convo) != 0:
            doctor_list.append(doctor_convo.rstrip())
        patient_convo = ""
        doctor_convo = ""
        if count > 0 :
            # print("Entry")
            dialog_dict['patient'] = patient_list
            dialog_dict['doctor'] = doctor_list
            my_dict['dialogue'] = dialog_dict
            #print(my_dict)
            main_list.append(my_dict)
            patient_flag = False
            doctor_flag = False

        my_dict = {}
        dialog_dict = {}
        patient_list = []
        doctor_list = []
        # print(line[3:])
        my_dict['id'] = line[3:]
        count += 1
        continue
    
    if line[0:4] == "http":
        my_dict['url'] = line
        continue
    
    if line[0:11] == "Description":
        desc_flag = True
        continue
    
    if desc_flag == True:
        my_dict['description'] = line
        desc_flag = False
        continue
    # if line[0:8] == "Dialogue":
    #     dialog_flag = True
    #     continue
    
    if line[0:8] == "Patient:":
        if len(doctor_convo) != 0:
            doctor_list.append(doctor_convo.rstrip())
        doctor_flag = False
        patient_flag = True
        patient_convo = ""
        continue
    if line[0:7] == "Doctor:":
        if len(patient_convo) != 0:
            patient_list.append(patient_convo.rstrip())
        patient_flag = False
        doctor_flag = True
        doctor_convo = ""
        continue

    if patient_flag == True:
        # patient_list.append(line)
        patient_convo += line + " "
        # print("Patient: "+ line)
        continue
    
    if doctor_flag == True:
        doctor_convo += line + " "
        # print("Doctor: "+ line)
        continue

if len(doctor_convo) != 0:
    doctor_list.append(doctor_convo.rstrip())
dialog_dict['patient'] = patient_list
dialog_dict['doctor'] = doctor_list
my_dict['dialogue'] = dialog_dict
main_list.append(my_dict)



with open('conversation_in_json_format.json', 'w') as fout:
    json.dump(main_list , fout)