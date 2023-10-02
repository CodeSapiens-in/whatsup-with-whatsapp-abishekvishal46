with open("_chat.txt", "r", encoding="utf-8") as file:
    chat_messages = file.readlines()

for i in chat_messages:
 if "created this group" in i:

    print("The Creator of the Group",i.split("created")[-2].split(":")[-1])

participant_names = []
participant_names_via_link = []
count=0
count_1=0
for message in chat_messages:
    if "joined" in message:
        count+=1
        names=message.split("joined")[-2].split("~")[-1]
        participant_names.append(names)

    if "joined using this group's invite link" in message:
        names_1 = message.split("joined")[-2].split("~")[-1]
        participant_names_via_link.append(names_1)
print("People joined via link: ",len(set(participant_names_via_link)))
print("No. of Participants: ",len(set(participant_names)))
dates=[]
count_msg=0
for i in chat_messages:
    if i.startswith("["):
        count_msg+=1
        dates.append(i[1:9])
correct_dates=set(dates)
print("No.of Messages: ",count_msg)
links_count=0
for message in chat_messages:
    if "https" in message:
        links_count+=1


print("No.of links that are shared",links_count)

co=0
for i in correct_dates:
     for j in chat_messages:
         if  i in j:
             co+=1

     print(f"there are {co} messages in {i}")
     co=0
print("The following are the participants: ")
for i in set(participant_names):
    print(i)
