# Living Expenses Calculator for Verbena Heights fam

import csv
import datetime

#accounts
veronica_pay = []
veronica_receive = []

christine_pay = []
christine_receive = []

arvind_pay = []
arvind_receive = []

victor_pay = []
victor_receive = []

mydate = datetime.datetime.now()
print("Ok, the file's loaded for the month of " + mydate.strftime("%B"))

# Open the file
expense_file = open("Monthly Expenses + Items Purchased - " + mydate.strftime("%B") + ".csv", "r")
reader = csv.reader(expense_file)
next(expense_file)

for row in reader:
	
	##PART 1: ADDING DATA TO ACCOUNTS##

	#read the people who needs to pay
	pay_names = row[4].split(', ')

	#divide the amount to be shared among responsible people
	amount_to_pay_per_person = float(row[3].replace(',', '')) / len(pay_names)

	#remove person who will receive the paid amount & turn it back into string
	for name in pay_names:
		if name == row[5]:
			pay_names.remove(name)
	pay_names_string = ", ".join(pay_names)
	
	#add amount to be paid by others
	for payers in pay_names:
		if payers == "Veronica":
			veronica_pay.append([str(amount_to_pay_per_person), row[5], row[0]])
		elif payers == "Christine":
			christine_pay.append([str(amount_to_pay_per_person), row[5], row[0]])
		elif payers == "Arvind":
			arvind_pay.append([str(amount_to_pay_per_person), row[5], row[0]])
		elif payers == "Victor":
			victor_pay.append([str(amount_to_pay_per_person), row[5], row[0]])


	#add to a person's receive account for the person who paid for something
	if row[5] == "Veronica":
		veronica_receive.append([row[3].replace(',',''), pay_names_string, str(amount_to_pay_per_person), row[0], pay_names])
	elif row[5] == "Christine":
		christine_receive.append([row[3].replace(',',''), pay_names_string, str(amount_to_pay_per_person), row[0], pay_names])
	elif row[5] == "Arvind":
		arvind_receive.append([row[3].replace(',',''), pay_names_string, str(amount_to_pay_per_person), row[0], pay_names])
	elif row[5] == "Victor":
		victor_receive.append([row[3].replace(',',''), pay_names_string, str(amount_to_pay_per_person), row[0], pay_names])


expense_file.close()

##PART 2: PRODUCE BILL FOR EACH PERSON##
	
#Veronica's Bill
#How much Veronica needs to receive from others
christine_to_veronicabill = 0
arvind_to_veronicabill = 0
victor_to_veronicabill = 0

veronica_bill = open(mydate.strftime("%B")+ ' Bill for Veronica.txt', 'w')
veronica_bill.write("%s\n%s\n%s\n" % ('Veronica\'s Bill for ' + mydate.strftime("%B"), '---------------------------------', "Here's stuff you need to get from others:"))

veronica_bill = open(mydate.strftime("%B") + ' Bill for Veronica.txt', 'a')

for stuff_to_receive in veronica_receive:
	for name in stuff_to_receive[4]:
		if name == "Christine":
			christine_to_veronicabill += float(stuff_to_receive[2])
		elif name == "Arvind":
			arvind_to_veronicabill += float(stuff_to_receive[2])
		elif name == "Victor":
			victor_to_veronicabill += float(stuff_to_receive[2])
	veronica_bill.write("%s\n\n" % ('You need to get total $' + str(float(stuff_to_receive[0])-float(stuff_to_receive[2])) + ' from ' + stuff_to_receive[1] + ' -- ' + '$'+stuff_to_receive[2] + ' per person -- for the item ' + stuff_to_receive[3]))

#Breakdown of how much each person owes & total
everyone_to_veronica = christine_to_veronicabill + arvind_to_veronicabill + victor_to_veronicabill
veronica_bill.write("%s\n%s\n%s\n%s\n%s\n\n" % ('Summary', 'Christine owes you: $' + str(christine_to_veronicabill), 'Arvind owes you: $' + str(arvind_to_veronicabill), 'Victor owes you: $' + str(victor_to_veronicabill), 'Total: $' + str(everyone_to_veronica)))

#How much Veronica needs to pay to others & to whom & total
veronica_bill.write("%s\n" % ("Here's what you owe to others:"))

veronica_to_christine = 0
veronica_to_arvind = 0
veronica_to_victor = 0

for stuff_to_pay in veronica_pay:
	if stuff_to_pay[1] == "Christine":
		veronica_to_christine += float(stuff_to_pay[0])
	elif stuff_to_pay[1] == "Arvind":
		veronica_to_arvind += float(stuff_to_pay[0])
	elif stuff_to_pay[1] == "Victor":
		veronica_to_victor += float(stuff_to_pay[0])
	veronica_bill.write("%s\n\n" % ("You need to pay $" + stuff_to_pay[0] + " to " + stuff_to_pay[1] + " for the item - " + stuff_to_pay[2]))


#Breakdown of how much veronica owes to each person
veronica_to_everyone = veronica_to_christine + veronica_to_arvind + veronica_to_victor
veronica_bill.write("%s\n%s\n%s\n%s\n%s\n\n" % ('Summary', 'You owe Christine: $' + str(veronica_to_christine), 'You owe Arvind: $' + str(veronica_to_arvind), 'You owe Victor: $' + str(veronica_to_victor), 'Total: $' + str(veronica_to_everyone)))

veronica_bill.write("%s\n\n%s\n\n" % ("-------------------------------------------", "For simplicity, you could just..."))

if veronica_to_christine > christine_to_veronicabill:
	diff = veronica_to_christine - christine_to_veronicabill
	veronica_bill.write("%s\n" % ("Pay $" + str(diff) + " to Christine"))
elif veronica_to_christine == christine_to_veronicabill:
	veronica_bill.write("%s\n" % ("No need to pay or receive from Christine"))
else:
	diff = christine_to_veronicabill - veronica_to_christine
	veronica_bill.write("%s\n\n" % ("Receive $" + str(diff) + " from Christine"))

if veronica_to_arvind > arvind_to_veronicabill:
	diff = veronica_to_arvind - arvind_to_veronicabill
	veronica_bill.write("%s\n" % ("Pay $" + str(diff) + " to Arvind"))
elif veronica_to_arvind == arvind_to_veronicabill:
	veronica_bill.write("%s\n" % ("No need to pay or receive from Arvind"))
else:
	diff = arvind_to_veronicabill - veronica_to_arvind
	veronica_bill.write("%s\n" % ("Receive $" + str(diff) + " from Arvind"))

if veronica_to_victor > victor_to_veronicabill:
	diff = veronica_to_victor - victor_to_veronicabill
	veronica_bill.write("%s\n" % ("Pay $" + str(diff) + " to Victor"))
elif veronica_to_victor == victor_to_veronicabill:
	veronica_bill.write("%s\n" % ("No need to pay or receive from Victor"))
else:
	diff = victor_to_veronicabill - veronica_to_victor
	veronica_bill.write("%s\n\n" % ("Receive $" + str(diff) + " from Victor"))

veronica_bill.close()

#Christine's Bill
#How much Christine needs to receive from others
veronica_to_christinebill = 0
arvind_to_christinebill = 0
victor_to_christinebill = 0

christine_bill = open(mydate.strftime("%B") + ' Bill for Christine.txt', 'w')
christine_bill.write("%s\n%s\n%s\n" % ('Christine\'s Bill for ' + mydate.strftime("%B"), '---------------------------------', "Here's stuff you need to get from others:"))

christine_bill = open(mydate.strftime("%B") + ' Bill for Christine.txt', 'a')

for stuff_to_receive in christine_receive:
	for name in stuff_to_receive[4]:
		if name == "Veronica":
			veronica_to_christinebill += float(stuff_to_receive[2])
		elif name == "Arvind":
			arvind_to_christinebill += float(stuff_to_receive[2])
		elif name == "Victor":
			victor_to_christinebill += float(stuff_to_receive[2])
	christine_bill.write("%s\n\n" % ('You need to get total $' + str(float(stuff_to_receive[0])-float(stuff_to_receive[2])) + ' from ' + stuff_to_receive[1] + ' -- ' + '$'+stuff_to_receive[2] + ' per person -- for the item ' + stuff_to_receive[3]))

#Breakdown of how much each person owes & total
everyone_to_christine = veronica_to_christinebill + arvind_to_christinebill + victor_to_christinebill
christine_bill.write("%s\n%s\n%s\n%s\n%s\n\n" % ('Summary', 'Veronica owes you: $' + str(veronica_to_christinebill), 'Arvind owes you: $' + str(arvind_to_christinebill), 'Victor owes you: $' + str(victor_to_christinebill), 'Total: $' + str(everyone_to_christine)))

#How much Christine needs to pay to others & to whom & total
christine_bill.write("%s\n" % ("Here's what you owe to others:"))

christine_to_veronica = 0
christine_to_arvind = 0
christine_to_victor = 0

for stuff_to_pay in christine_pay:
	if stuff_to_pay[1] == "Veronica":
		christine_to_veronica += float(stuff_to_pay[0])
	elif stuff_to_pay[1] == "Arvind":
		christine_to_arvind += float(stuff_to_pay[0])
	elif stuff_to_pay[1] == "Victor":
		christine_to_victor += float(stuff_to_pay[0])
	christine_bill.write("%s\n\n" % ("You need to pay $" + stuff_to_pay[0] + " to " + stuff_to_pay[1] + " for the item - " + stuff_to_pay[2]))

#Breakdown of how much Christine owes to each person
christine_to_everyone = christine_to_veronica + christine_to_arvind + christine_to_victor
christine_bill.write("%s\n%s\n%s\n%s\n%s\n\n" % ('Summary', 'You owe Veronica: $' + str(christine_to_veronica), 'You owe Arvind: $' + str(christine_to_arvind), 'You owe Victor: $' + str(christine_to_victor), 'Total: $' + str(christine_to_everyone)))

christine_bill.write("%s\n\n%s\n\n" % ("-------------------------------------------", "For simplicity, you could just..."))

if christine_to_veronica > veronica_to_christinebill:
	diff = veronica_to_christine - christine_to_veronicabill
	christine_bill.write("%s\n" % ("Pay $" + str(diff) + " to Veronica"))
elif christine_to_veronica == veronica_to_christinebill:
	christine_bill.write("%s\n" % ("No need to pay or receive from Veronica"))
else:
	diff = veronica_to_christinebill - christine_to_veronica
	christine_bill.write("%s\n\n" % ("Receive $" + str(diff) + " from Veronica"))

if christine_to_arvind > arvind_to_christinebill:
	diff = christine_to_arvind - arvind_to_christinebill
	christine_bill.write("%s\n" % ("Pay $" + str(diff) + " to Arvind"))
elif christine_to_arvind == arvind_to_christinebill:
	christine_bill.write("%s\n" % ("No need to pay or receive from Arvind"))
else:
	diff = arvind_to_christinebill - christine_to_arvind
	christine_bill.write("%s\n" % ("Receive $" + str(diff) + " from Arvind"))

if christine_to_victor > victor_to_christinebill:
	diff = christine_to_victor - victor_to_christinebill
	christine_bill.write("%s\n" % ("Pay $" + str(diff) + " to Victor"))
elif christine_to_victor == victor_to_christinebill:
	christine_bill.write("%s\n" % ("No need to pay or receive from Victor"))
else:
	diff = victor_to_christinebill - christine_to_victor
	christine_bill.write("%s\n\n" % ("Receive $" + str(diff) + " from Victor"))

christine_bill.close()

#Arvind's Bill
#How much Arvind needs to receive from others
veronica_to_arvindbill = 0
christine_to_arvindbill = 0
victor_to_arvindbill = 0

arvind_bill = open(mydate.strftime("%B")+ ' Bill for Arvind.txt', 'w')
arvind_bill.write("%s\n%s\n%s\n" % ('Arvind\'s Bill for ' + mydate.strftime("%B"), '---------------------------------', "Here's stuff you need to get from others:"))

arvind_bill = open(mydate.strftime("%B") + ' Bill for Arvind.txt', 'a')

for stuff_to_receive in arvind_receive:
	for name in stuff_to_receive[4]:
		if name == "Veronica":
			veronica_to_arvindbill += float(stuff_to_receive[2])
		elif name == "Christine":
			christine_to_arvindbill += float(stuff_to_receive[2])
		elif name == "Victor":
			victor_to_arvindbill += float(stuff_to_receive[2])
	arvind_bill.write("%s\n\n" % ('You need to get total $' + str(float(stuff_to_receive[0])-float(stuff_to_receive[2])) + ' from ' + stuff_to_receive[1] + ' -- ' + '$'+stuff_to_receive[2] + ' per person -- for the item ' + stuff_to_receive[3]))

#Breakdown of how much each person owes & total
everyone_to_arvind = veronica_to_arvindbill + christine_to_arvindbill + victor_to_arvindbill
arvind_bill.write("%s\n%s\n%s\n%s\n%s\n\n" % ('Summary', 'Veronica owes you: $' + str(veronica_to_arvindbill), 'Christine owes you: $' + str(christine_to_arvindbill), 'Victor owes you: $' + str(victor_to_arvindbill), 'Total: $' + str(everyone_to_arvind)))

#How much Arvind needs to pay to others & to whom & total
arvind_bill.write("%s\n" % ("Here's what you owe to others:"))

arvind_to_veronica = 0
arvind_to_christine = 0
arvind_to_victor = 0

for stuff_to_pay in arvind_pay:
	if stuff_to_pay[1] == "Veronica":
		arvind_to_veronica += float(stuff_to_pay[0])
	elif stuff_to_pay[1] == "Christine":
		arvind_to_christine += float(stuff_to_pay[0])
	elif stuff_to_pay[1] == "Victor":
		arvind_to_victor += float(stuff_to_pay[0])
	arvind_bill.write("%s\n\n" % ("You need to pay $" + stuff_to_pay[0] + " to " + stuff_to_pay[1] + " for the item - " + stuff_to_pay[2]))

#Breakdown of how much Arvind owes to each person
arvind_to_everyone = arvind_to_veronica + arvind_to_christine + arvind_to_victor
arvind_bill.write("%s\n%s\n%s\n%s\n%s\n\n" % ('Summary', 'You owe Veronica: $' + str(arvind_to_veronica), 'You owe Christine: $' + str(arvind_to_christine), 'You owe Victor: $' + str(arvind_to_victor), 'Total: $' + str(arvind_to_everyone)))

arvind_bill.write("%s\n\n%s\n\n" % ("-------------------------------------------", "For simplicity, you could just..."))

if arvind_to_veronica > veronica_to_arvindbill:
	diff = arvind_to_veronica  - veronica_to_arvindbill
	arvind_bill.write("%s\n" % ("Pay $" + str(diff) + " to Veronica"))
elif arvind_to_veronica == veronica_to_arvindbill:
	arvind_bill.write("%s\n" % ("No need to pay or receive from Veronica"))
else:
	diff =  veronica_to_arvindbill - arvind_to_veronica
	arvind_bill.write("%s\n\n" % ("Receive $" + str(diff) + " from Veronica"))

if arvind_to_christine > christine_to_arvindbill:
	diff = arvind_to_christine - christine_to_arvindbill
	arvind_bill.write("%s\n" % ("Pay $" + str(diff) + " to Christine"))
elif arvind_to_christine == christine_to_arvindbill:
	arvind_bill.write("%s\n" % ("No need to pay or receive from Christine"))
else:
	diff = christine_to_arvindbill - arvind_to_christine
	arvind_bill.write("%s\n" % ("Receive $" + str(diff) + " from Christine"))

if arvind_to_victor > victor_to_arvindbill:
	diff = arvind_to_victor - victor_to_arvindbill
	arvind_bill.write("%s\n" % ("Pay $" + str(diff) + " to Victor"))
elif arvind_to_victor == victor_to_arvindbill:
	arvind_bill.write("%s\n" % ("No need to pay or receive from Victor"))
else:
	diff = victor_to_arvindbill - arvind_to_victor
	arvind_bill.write("%s\n\n" % ("Receive $" + str(diff) + " from Victor"))


arvind_bill.close()


#Victor's Bill
#How much Victor needs to receive from others
veronica_to_victorbill = 0
christine_to_victorbill = 0
arvind_to_victorbill = 0

victor_bill = open(mydate.strftime("%B") + ' Bill for Victor.txt', 'w')
victor_bill.write("%s\n%s\n%s\n" % ('Victor\'s Bill for ' + mydate.strftime("%B"), '---------------------------------', "Here's stuff you need to get from others:"))

victor_bill = open(mydate.strftime("%B") + ' Bill for Victor.txt', 'a')

for stuff_to_receive in victor_receive:
	for name in stuff_to_receive[4]:
		if name == "Veronica":
			veronica_to_victorbill += float(stuff_to_receive[2])
		elif name == "Christine":
			christine_to_victorbill += float(stuff_to_receive[2])
		elif name == "Arvind":
			arvind_to_victorbill += float(stuff_to_receive[2])
	victor_bill.write("%s\n\n" % ('You need to get total $' + str(float(stuff_to_receive[0])-float(stuff_to_receive[2])) + ' from ' + stuff_to_receive[1] + ' -- ' + '$'+stuff_to_receive[2] + ' per person -- for the item ' + stuff_to_receive[3]))

#Breakdown of how much each person owes & total
everyone_to_victor = veronica_to_victorbill + christine_to_victorbill + arvind_to_victorbill
victor_bill.write("%s\n%s\n%s\n%s\n%s\n\n" % ('Summary', 'Veronica owes you: $' + str(veronica_to_victorbill), 'Christine owes you: $' + str(christine_to_victorbill), 'Arvind owes you: $' + str(arvind_to_victorbill), 'Total: $' + str(everyone_to_victor)))

#How much Victor needs to pay to others & to whom & total
victor_bill.write("%s\n" % ("Here's what you owe to others:"))

victor_to_veronica = 0
victor_to_christine = 0
victor_to_arvind = 0

for stuff_to_pay in victor_pay:
	if stuff_to_pay[1] == "Veronica":
		victor_to_veronica += float(stuff_to_pay[0])
	elif stuff_to_pay[1] == "Christine":
		victor_to_christine += float(stuff_to_pay[0])
	elif stuff_to_pay[1] == "Arvind":
		victor_to_arvind += float(stuff_to_pay[0])
	victor_bill.write("%s\n\n" % ("You need to pay $" + stuff_to_pay[0] + " to " + stuff_to_pay[1] + " for the item - " + stuff_to_pay[2]))

#Breakdown of how much Arvind owes to each person
victor_to_everyone = victor_to_veronica + victor_to_christine + victor_to_arvind
victor_bill.write("%s\n%s\n%s\n%s\n%s\n\n" % ('Summary', 'You owe Veronica: $' + str(victor_to_veronica), 'You owe Christine: $' + str(victor_to_christine), 'You owe Arvind: $' + str(victor_to_arvind), 'Total: $' + str(victor_to_everyone)))

victor_bill.write("%s\n\n%s\n\n" % ("-------------------------------------------", "For simplicity, you could just..."))

if victor_to_veronica > veronica_to_victorbill:
	diff = victor_to_veronica  - veronica_to_victorbill
	victor_bill.write("%s\n" % ("Pay $" + str(diff) + " to Veronica"))
elif victor_to_veronica == veronica_to_victorbill:
	victor_bill.write("%s\n" % ("No need to pay or receive from Veronica"))
else:
	diff =  veronica_to_victorbill - victor_to_veronica
	victor_bill.write("%s\n\n" % ("Receive $" + str(diff) + " from Veronica"))

if victor_to_christine > christine_to_victorbill:
	diff = victor_to_christine - christine_to_victorbill
	victor_bill.write("%s\n" % ("Pay $" + str(diff) + " to Christine"))
elif victor_to_christine == christine_to_victorbill:
	victor_bill.write("%s\n" % ("No need to pay or receive from Christine"))
else:
	diff = christine_to_victorbill - victor_to_christine
	victor_bill.write("%s\n" % ("Receive $" + str(diff) + " from Christine"))

if victor_to_arvind > arvind_to_victorbill:
	diff = victor_to_arvind - arvind_to_victorbill
	victor_bill.write("%s\n" % ("Pay $" + str(diff) + " to Arvind"))
elif victor_to_arvind == arvind_to_victorbill:
	victor_bill.write("%s\n" % ("No need to pay or receive from Arvind"))
else:
	diff = victor_to_arvindbill - arvind_to_victor
	victor_bill.write("%s\n\n" % ("Receive $" + str(diff) + " from Arvind"))

victor_bill.close()