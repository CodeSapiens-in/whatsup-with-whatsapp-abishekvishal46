with open(r"_chat.txt",  encoding="utf8") as fp:
    text = fp.readlines()
    lines = len(text)
    pollcount =0
    for eachline in text:
        if 'POLL' in eachline:
            pollcount=pollcount+1
    print('Total Number of lines:', lines)
    print('Total polls: '+str(pollcount))
    participant_names = set()

for message in chat_messages:
    if "joined using" in message:

        parts = message.split('~')
        if len(parts) > 1:
            participant_name = parts[1]
            participant_names.add(participant_name)

        # Debug prints

print(participant_names)
total_participants = len(participant_names)
print("Total number of participants:", total_participants)
co=0
for i in dates:
     for j in chat_messages:
         if  i in j:
             co+=1

     print(f"{i},there are {co} messages in this dates")
     co=0

    
