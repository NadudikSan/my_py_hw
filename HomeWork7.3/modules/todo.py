import time
messageUser = input("Enter message:")
with open('note.txt','w') as file:
    while messageUser != "end":
        named_tuple = time.localtime() # receive struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        file.write(time_string +" "+ messageUser+"\n" )
        messageUser = input("Enter message:")