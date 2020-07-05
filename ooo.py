import json, pprint, os
from os import path

#function for dump tha data:
def FunctionForOpenAndDumpFile(ParameterForDumping):
	with open("LoginOrSingnup.json","a") as varForLoginOrSignup_1:
		json.dump(ParameterForDumping,varForLoginOrSignup_1)

#function for read the data:-
def FunctionForOpenAndReadFile():
	with open("LoginOrSingnup.json","r") as varForLoginOrSignup_2:
		List_Account = json.load(varForLoginOrSignup_2)
		return (List_Account)

#function for rewrite the data:-
def FunctionForOpenAndRewrite(ParameterForRewriting):
		with open("LoginOrSingnup.json","w") as varForLoginOrSignup_1:
			json.dump(ParameterForRewriting,varForLoginOrSignup_1,indent=4)

def FunctionForUpdating(StorageList):
	Dict_Note = {}
	StorageList_Value3 = StorageList
	print("4.:-Updating\n5.:-No Need Of Updating")
	InputForUpdating = int(input("4 or 5:-"))
	if InputForUpdating == 4:
		Dict_Note[len(StorageList_Value3)+1] = input("Enter Wharever You Want:-")
		StorageList_Value3.append(Dict_Note)
		return StorageList_Value3
	elif InputForUpdating == 5:
		return StorageList_Value3

#function for accessing the data:-
def FunctionForAccessingAccount(ListForAccount,UserName,PassWord):
	for SpecificAccount in ListForAccount:
		for key1,value1 in SpecificAccount.items():
			if key1 in UserName:
				for key2,value2 in value1.items():
					if key2 == UserName:
						for key3,value3 in value2.items():
							if key3 == PassWord:
								return(FunctionForUpdating(value3))
							else:
								print("You May Enter WrongPassWord!")
					break
			break
#virtual note pad:-
print("<*******************************************Welcome To Virtual Note pad:-****************************************************")
print("1.login\n2.signup")
FileForData = path.exists("LoginOrSingnup.json")
if FileForData == True:
	LoginOrSingnup = int(input("enter 1.login or 2.singup:-"))
	if LoginOrSingnup == 1:
		UserName = input("Enter UserName:-").strip()
		PassWord = input("Enter PassWord:-").strip()
		ListOfAllAccounts = FunctionForOpenAndReadFile()
		UpdatedStorage = FunctionForAccessingAccount(ListOfAllAccounts,UserName,PassWord)
		for MyAccount in ListOfAllAccounts:
			for keys,values in MyAccount.items():
				if keys in UserName:
					values[UserName][PassWord] = UpdatedStorage
		VarForFunction = FunctionForOpenAndRewrite(ListOfAllAccounts)
	else:
		FirstName = input("enter FirstName:-")
		LirstName = input("enter LirstName:-")
		password = input("enter your password:-")
		Account = {FirstName:{FirstName+LirstName:{password:list()}}}
		ListForAppending = FunctionForOpenAndReadFile()
		ListForAppending.append(Account)
		FunctionForOpenAndRewrite(ListForAppending)
else:
	Parameter = list()
	FunctionForOpenAndDumpFile(Parameter)



