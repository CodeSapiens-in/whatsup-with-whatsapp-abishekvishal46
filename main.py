with open("_chat.txt", "r", encoding="utf-8") as file:
    chat_messages = file.readlines()


participant_names = []
participant_names_via_link = []
count=0
count_1=0
print(len(chat_messages))

for message in chat_messages:
    if "joined" in message:
        count+=1
        names=message.split("joined")[-2].split("~")[-1]
        participant_names.append(names)
        # Debug prints
    if "joined using this group's invite link" in message:
        names_1 = message.split("joined")[-2].split("~")[-1]
        participant_names_via_link.append(names_1)

total_participants = len(participant_names)
print("People joined via link: ",len(set(participant_names_via_link)))
print("No. of Participants: ",len(set(participant_names)))
dates=["28/04/23","05/05/23","06/05/23","08/05/23","09/05/23","10/05/23",""]
for i in chat_messages:
 if "created this group" in i:

    print("The Creator of the Group",i.split("created")[-2].split(":")[-1])
co=0
for i in dates:
     for j in chat_messages:
         if  i in j:
             co+=1

     print(f"{i},there are {co} messages in this dates")
     co=0


    
