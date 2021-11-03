import re

with open("assets/potential-contacts.txt","r")as file:
    potential_contacts=file.read()

emails=re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+',potential_contacts)
emails=set(emails)
with open("automation/emails.txt","w") as f:
    for email in emails:
        f.write(str(email)+"\n")
        
# [+\d-]+[\d]{3}-[\d]{3}-[\d]{4}
phones=re.findall(r'[(]+[\d]{3}[)\d][\d]{3}-\d{4}|[\d]{3}-[\d]{3}-[\d]{4}|[\d]{3}-[\d]{4}',potential_contacts)
phones= set(phones)
with open("automation/phone_numbers.txt","w") as f:
    for phone in phones:
        if len(phone) == 7:
            f.write("206-"+str(phone)+"\n")
        else:
            phone=phone.replace("(","")
            phone=phone.replace(")","-")
            f.write(str(phone)+"\n")
print(len(phones))