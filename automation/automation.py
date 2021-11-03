import re

with open("assets/potential-contacts.txt","r")as file:
    potential_contacts=file.read()

emails=re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+',potential_contacts)

with open("automation/emails.txt","w") as f:
    for email in emails:
        f.write(str(email)+"\n")

phones=re.findall(r'[(]+[\d]{3}[)\d][\d]{3}-\d{4}|[\d]{3}-[\d]{3}-[\d]{4}|[\d]{3}-[\d]{3}',potential_contacts)

with open("automation/phone_numbers.txt","w") as f:
    for phone in phones:
        if len(phone) == 7:
            f.write("206-"+str(phone)+"\n")
        else:
            phone=phone.replace("(","")
            phone=phone.replace(")","-")
            f.write(str(phone)+"\n")
print(len(phones))