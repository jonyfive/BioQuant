#!/usr/bin/python3
# =============================================================
# Function descriptions:
# ----------------------
# 0)Main: The main function.
# 1)Extract: Extract users from general population, update list
# and write to file.
# 2)checkErrors: Check data for duplicates.
# 3)Balance: Calculate daily balance by delta.
# =============================================================


import os
import re
import time
from time import localtime, strftime


# Function 2
def checkErrors(raw):
    print('\n2)Checking for duplicants...')
    checked = []  # List of checked users
    duplicates = []  # Duplicate entries
    count = 0  # Counting var
    limit = len(raw)  # Length of list to be modified in iteration
    i = 0  # Index
    while i < limit:
        checked.append(raw[i])  # Append name of user to checked list
        j = i+1  # Index
        while j < limit:
            if checked[i][0] == raw[j][0]:  # Check for username repeats
                duplicates.append(raw[j])
                del raw[j]  # Delete duplicate
                count += 1  # Count duplicate entries
                limit -= 1  # Decrease list size after duplicate deletion
            j += 1
        i += 1
    return(count, checked)

# Function 1
def extract(tNum):
    # Extract users, build list and write to file
    print('\n1)Looking for users...')
    checked = []
    raw = []  # List of relevent users
    count = 0  # Counting var
    date = strftime("%d %b %y", localtime())  # Day month year
    current = 'current/allUsers'  # Filename
    archive = 'archive/myUsers/' + date  # Filename
    with open(current, 'r') as f1, open(archive, 'w') as f2:  # Open file
        current = f1.readlines()  # Dump info to iterable
        for line in current:

            # Verify data
            if len(line.split()) == 4 and line.split()[3] == tNum:
                f2.write(line.split()[0] + " " +
                         line.split()[1] + '\n')  # Write verified data to file
                nameAndPoints = [line.split()[0], int(
                    line.split()[1])]  # Build user list
                raw.append(nameAndPoints)
                count += 1  # Count occorrunces
    print(count, ' users found')  # Print number of users found
    return(checkErrors(raw))  # Send to error check func2 and return to Main

# Function 3
def balance(current):
    print('\n3)Calculating user balance...')
    archive = []
    balance = []
    undocumented = []
    size = len(os.listdir('archive/myUsers/'))-2
    name1 = 'archive/myUsers/' + \
        os.listdir('archive/myUsers/')[size]  # Filnename
    date = strftime("%d %b %y", localtime())  # Day month year
    name2 = 'balance/' + date  # Filename
    with open(name1, 'r') as f1, open(name2, 'w') as f2:
        data = f1.readlines()  # Read archived data to var
        for line in data:  # Calculate user balance
            nameAndPoints = [line.split()[0], int(
                line.split()[1])]  # Build user list from archive
            archive.append(nameAndPoints)
        for i in range(0, len(current), 1):
            balance.append(current[i])
            flag = 0
            for j in range(0, len(archive), 1):
                if balance[i][0] == archive[j][0]:  # Match by user name
                    balance[i][1] = (current[i][1] - archive[j]
                                     [1])  # Calculate delta
                    flag = 1
            if flag == 0:  # Flag new user
                undocumented.append(balance[i])

        for usr in balance:  # Write balance to file
            f2.write(str(usr) + '\n')
        f2.write(date)
    return(len(undocumented))


# MAIN==================================================
print('\nInitiating MAIN...')
tzero = time.time()  # Set inital time for runtime test
tNum = ''
count, current = extract(tNum)  # Call function 1 and 2
if count:  # Function 2 error msg
    print(count, ' duplicants found')
else:
    print('No errors')
num = balance(current)  # Call function 3
print('Found', num, 'new users')
print('\nAll function executed')
print('Final runtime is %s seconds' %
      (time.time() - tzero), '\n')  # Final code runtime
# ======================================================
