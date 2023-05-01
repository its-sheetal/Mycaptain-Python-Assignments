#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
def write_info_csv(info_list):
    with open('worker_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
             writer.writerow(['Name','Age','contact number','Email id'])
        writer.writerow(info_list)


if __name__== '__main__':
    condition= True
    worker_num=1
while(condition):
    worker_info=input('enter worker information for worker #{} in the following format (Name Age Contact_no Email_id): '.format(worker_num))
    print('Entered information:'+ worker_info)
    
    worker_info_list = worker_info.split(' ')
    
    print('\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nEmail_id: {}'.format(worker_info_list[0],worker_info_list[1],worker_info_list[2],worker_info_list[3]))
    choice_check = input('is the entered info correct?(yes/no):')
    
    if choice_check=='yes':
         write_info_csv(worker_info_list)
    
         condition_check=input('enter (yes/no) if you want to enter info for another worker: ')
         if condition_check=='yes':
                condition=True
                worker_num=worker_num+1
         elif condition_check=='no':
            condition=False
    elif condition_check=='no':
        print('\nPlease re-enter the value')
        
        


# In[ ]:




