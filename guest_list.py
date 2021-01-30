guest_list = []
no_list = []

while len(guest_list) < 10:
    new_guest = input("Please invite a new guest: ")
    print("Congratulations, {} you are invited to my party.".format(new_guest))
    rsvp = input("Please RSVP yes or no: ")
    
    if rsvp == "yes" or rsvp =="Yes" or rsvp == "YES":
    	guest_list.append(new_guest)
    	continue
        
    if rsvp == "No" or rsvp == "NO" or rsvp == 'no':
        no_list.append(new_guest)
        continue 
    else:
    	rsvp = input("Please Enter Yes or No: ")

	if rsvp == "yes" or rsvp =="Yes" or rsvp == "YES":
    	guest_list.append(new_guest)
    	continue
        
    if rsvp == "No" or rsvp == "NO" or rsvp == 'no':
        no_list.append(new_guest)
        continue 



        
print(guest_list)
print(no_list)

new_guest_list = str(guest_list)
new_no_list = str(no_list)

file_name = open("guest_list.txt" , 'w')
file_name.write("This is your guest list: \n")
file_name.write(new_guest_list + '\n')
file_name.write("\n This is your no list: \n")
file_name.write(new_no_list)
file_name.close()