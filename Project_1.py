import csv

def write_to_csv(list_input):
    with open('student_details.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(list_input)


data_fields_required = ["Name","Age","Contact Number","Email Address"]
write_to_csv(data_fields_required)
condition = True
while condition == True:
    
    student_info = input("\nEnter the student information in the given format - (Name Age Contact_Number Email_Address):")
    student_info_list = student_info.split(" ")
    print("\nThe entered student information is : Name:{} ,Age:{} ,Contact Number:{} ,Email Address:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    information_check = input("\nEnter (yes//no) if entered information is correct :")

    if information_check.lower() == "yes":
        write_to_csv(student_info_list)
        condition_check = input("\nEnter (yes//no) if you want to enter another student information :")

        if condition_check.lower() == "yes":
            condition = True
            
        else:
            condition = False
            
    else:
        student_info=input("Please re-enter the details :")
        student_info_list = student_info.split(" ")
        print("\nThe entered student information is : Name:{} ,Age:{} ,Contact Number:{} ,Email Address:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        write_to_csv(student_info_list)
        condition_check = input("\nEnter (yes//no) if you want to enter another student information :")

        if condition_check.lower() == "yes":
            condition = True
            
        else:
            condition = False
    
        
    

