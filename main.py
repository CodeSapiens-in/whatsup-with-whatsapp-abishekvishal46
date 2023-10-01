with open(r"_chat.txt",  encoding="utf8") as fp:
    text = fp.readlines()
    lines = len(text)
    pollcount =0
    for eachline in text:
        if 'POLL' in eachline:
            pollcount=pollcount+1
    print('Total Number of lines:', lines)
    print('Total polls: '+str(pollcount))
    
