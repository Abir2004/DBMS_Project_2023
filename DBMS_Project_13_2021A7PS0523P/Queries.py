import mysql.connector as mc
from datetime import date, datetime


# Change this according to the User of the Code,
# Ensure that you run the runFirst.sql file
# beforehand

userID = "root"
pwd = "Tintin@1"

# Voting Management System
# Abir Abhyankar 2021A7PS0523P

# This file contains Python scripts
# for all the queries run in the project

# Same structure in all queries First few lines
# involve connecting to the database and
# establishing a cursor and executing queries to
# get output

# Individual Queries have also been documented


def add_Voter(password, name, email, address, phone, dob):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = "INSERT INTO Voter(Password,Name,Email,Address,DateOfBirth) VALUES("
    l = dob.split("-")
    d = date.today()
    s1 = d.strftime("%Y/%m/%d")
    s2 = l[0] + "/" + l[1] + "/" + l[2]
    d1 = datetime.strptime(s1, "%Y/%m/%d")
    d2 = datetime.strptime(s2, "%Y/%m/%d")
    delta = d1 - d2  # Checking the difference between Current Date and DOB of the Voter
    s = f"SELECT Voter_ID FROM Voter WHERE Password = '{password}' AND Name = '{name}' AND Email = '{email}' AND Address = '{address}' AND Phone_Number = '{phone}' AND DateOfBirth = '{dob}';"
    cursor.execute(
        s
    )  # Checking if a Voter_ID corresponding to such details already exists?
    x = cursor.fetchall()
    if len(x) > 0:  # If len(x)>0, Voter has already registered previously, so return -2
        cursor.close()
        db.close()
        return -2  # Already Registered
    if delta.days // 365 < 18:  # Voter shouldn't be a minior so this restriction
        cursor.close()
        db.close()
        return -1  # Not Above 18
    else:
        s = f"INSERT INTO Voter(Password,Name,Email,Address,Phone_Number,DateOfBirth) VALUES('{password}','{name}','{email}','{address}','{phone}','{dob}');"
        cursor.execute(s)  # Inserting into Voter Database
        print(s)
        s = f"SELECT Voter_ID FROM Voter WHERE Password = '{password}' AND Name = '{name}' AND Email = '{email}' AND Address = '{address}' AND Phone_Number = '{phone}' AND DateOfBirth = '{dob}';"
        cursor.execute(s)
        x = cursor.fetchall()  # x now contains the Voter_ID of the Voter newly added
        cursor.close()
        db.commit()  # Committing the changes made
        db.close()  # Close Database and Cursor
        return x[0][0]  # Returning the Voter_Id to be displayed on the GUI


def add_Candidate(name, dob, party, admin_id, elec_id):
    # Get Elec_ID as well, as Admins enter Candidates for new Elections
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    l = dob.split("-")
    d = date.today()
    s1 = d.strftime("%Y/%m/%d")
    s2 = l[0] + "/" + l[1] + "/" + l[2]
    d1 = datetime.strptime(s1, "%Y/%m/%d")
    d2 = datetime.strptime(s2, "%Y/%m/%d")
    delta = d1 - d2  # Checking the difference between candidate's DOB and today's date
    if delta.days // 365 < 18:  # Candidate cannot be a minor, thus prevent insertion
        cursor.close()
        db.close()
        return -1
    else:
        s = f"SELECT  Candidate_ID FROM Candidate WHERE NAME = '{name}' AND DOB = '{dob}' AND Party_Name = '{party}';"
        cursor.execute(s)
        # Checking the existence of the Candidate in the Candidate table
        # If Candidate details were already present, no need to add the details again
        # We just need to update the stands_for table
        a = cursor.fetchall()
        if len(a) == 0:  # No Previous Record of the candidate
            s = f"INSERT INTO Candidate(Name,DOB,Age,Party_Name,Admin_ID) VALUES('{name}','{dob}','{delta.days//365}','{party}','{admin_id}');"
            cursor.execute(s)  # Inserting Candidate into Candidate Table
            print(s)
        s = f"INSERT IGNORE INTO Stands_For VALUES((SELECT Candidate_ID FROM Candidate WHERE Name = '{name}' AND DOB = '{dob}' AND Party_Name = '{party}'),{elec_id});"
        # INSERT IGNORE used to prevent situations when 2
        # admins enter the same candidate into the same
        # election
        cursor.execute(s)
        cursor.close()
        db.commit()  # Commit the changes made
        db.close()  # Close Database and Cursor
        return 1


def add_Vote(voter_id, cand_id, elec_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT Vote_ID FROM Vote WHERE Voter_ID = '{voter_id}' AND Election_ID = '{elec_id}';"
    cursor.execute(
        s
    )  # Checking if person with given voter_id has voted in the elction with elec_id
    x = cursor.fetchall()
    if len(x) > 0:  # If len(x) > 0, vote has been made by that voter in that election
        # So he can't cast anymore votes
        cursor.close()
        db.close()
        return -1  # Vote Already Casted
    s = f"INSERT INTO Vote(Voter_ID,Candidate_ID,Election_ID) VALUES({voter_id},{cand_id},{elec_id});"
    # Inserting new Vote into the Vote database and
    # Candidate's Vote Count Increases
    print(s)
    cursor.execute(s)
    cursor.close()
    db.commit()  # Committing the changes
    db.close()  # Closing database and server
    return 1


def add_Election(start_date, end_date, title, admin_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    l = start_date.split("-")
    l0 = end_date.split("-")
    s1 = l0[0] + "/" + l0[1] + "/" + l0[2]
    s2 = l[0] + "/" + l[1] + "/" + l[2]
    d1 = datetime.strptime(s1, "%Y/%m/%d")
    d2 = datetime.strptime(s2, "%Y/%m/%d")
    delta = (
        d1 - d2
    )  # Checking difference between Election End Date and Election Start Date
    if (
        delta.days < 0
    ):  # This means that Start Date is after End Date, so invalid eleciton timeline
        db.close()
        cursor.close()
        return -1  # Election Start Date is after Election End Date
    else:
        s = f"INSERT INTO Election(Election_Start_Date,Election_End_Date,Election_Title,Admin_ID) VALUES('{start_date}','{end_date}','{title}',{admin_id});"
        # Inserting New Election into the Database
        cursor.execute(s)
        print(s)
        cursor.close()
        db.commit()  # Committing the changes made
        db.close()  # Closing Database and cursor
        return 1


def get_Vote(cand_id, elec_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT COUNT(*) FROM VOTE WHERE Candidate_ID = {cand_id} AND Election_ID = {elec_id}; "
    # After execution we get Number of Votes received
    # by that candidate in a particular election
    cursor.execute(s)
    print(s)
    l = cursor.fetchall()
    cursor.close()
    db.close()  # Closing Database and cursor
    return l[0][0]


def get_Vote_Percentage(cand_id, elec_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT COUNT(*)*100/(SELECT COUNT(*) FROM VOTE WHERE Election_ID = {elec_id}) FROM VOTE WHERE Candidate_ID = {cand_id} AND Election_ID = {elec_id}; "
    # Nested Query ton find Vote Percentage of a Candidate
    cursor.execute(s)
    print(s)
    l = cursor.fetchall()
    cursor.close()
    db.close()  # Closing Database and Cursor
    return round(l[0][0], 2)  # Rounding to 2 Decimal Places


def get_Winner(elec_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT Election_Start_Date,Election_End_Date FROM Election WHERE Election_ID = {elec_id};"
    # Election Must be Over before Winner is determined
    cursor.execute(s)
    l = cursor.fetchall()
    d = date.today()
    delta = l[0][0] - d  # Difference between Election Start_Date and today
    if (
        delta.days > 0
    ):  # If greater than 0 this means that election will start sometime after today
        cursor.close()
        db.close()
        return -1  # Election not started
    delta = l[0][1] - d  # Difference between Election End Date and today
    if delta.days >= 0:  # Difference must be less than 0 for Election to be over
        cursor.close()
        db.close()
        return -2  # Election in progress
    s = f"SELECT Name,Party_Name  FROM Candidate NATURAL JOIN (SELECT Candidate_ID,COUNT(Candidate_ID) AS VOTE FROM VOTE WHERE ELECTION_ID = {elec_id} GROUP By Candidate_ID ORDER BY VOTE DESC) as T ORDER BY VOTE DESC LIMIT 1;"
    # LIMIT of 1 on output as we want to get Winner
    cursor.execute(s)
    print(s)
    l = cursor.fetchall()
    cursor.close()
    db.close()  # Closing Database and cursor
    return l[0]  # Election Winner


def get_Ranks(elec_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT Election_Start_Date,Election_End_Date FROM Election WHERE Election_ID = {elec_id};"
    # Election Must be Over before Ranklist is determined
    cursor.execute(s)
    l = cursor.fetchall()
    d = date.today()
    delta = l[0][0] - d  # Difference between Election Start_Date and today
    if (
        delta.days > 0
    ):  # If greater than 0 this means that election will start sometime after today
        cursor.close()
        db.close()
        return -1  # Election not started
    delta = l[0][1] - d  # Difference between Election End Date and today
    if delta.days >= 0:  # Difference must be less than 0 for Election to be over
        cursor.close()
        db.close()
        return -2  # Election in progress
    s = f"SELECT Candidate_ID,Name,Party_Name  FROM Candidate NATURAL JOIN (SELECT Candidate_ID,COUNT(Candidate_ID) AS VOTE FROM VOTE WHERE ELECTION_ID = {elec_id} GROUP By Candidate_ID ORDER BY VOTE DESC) as T ORDER BY VOTE DESC;"
    # No LIMIT as we want all candidates
    cursor.execute(s)
    print(s)
    l = cursor.fetchall()
    cursor.close()
    db.close()  # Closing Database and cursor
    return l  # Ranklist


def get_Total_Votes(elec_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT Election_Start_Date,Election_End_Date FROM Election WHERE Election_ID = {elec_id};"
    # Election Must be Over before Total Votes are determined
    cursor.execute(s)
    l = cursor.fetchall()
    d = date.today()
    delta = l[0][0] - d  # Difference between Election Start_Date and today
    if (
        delta.days > 0
    ):  # If greater than 0 this means that election will start sometime after today
        cursor.close()
        db.close()
        return -1  # Election not started
    delta = l[0][1] - d  # Difference between Election End Date and today
    if delta.days >= 0:  # Difference must be less than 0 for Election to be over
        cursor.close()
        db.close()
        return -2  # Election in progress
    s = f"SELECT COUNT(*) FROM VOTE WHERE Election_ID = {elec_id};"
    # Get Total Votes
    cursor.execute(s)
    print(s)
    l = cursor.fetchall()
    cursor.close()
    db.close()  # Closing Database and Cursor
    return l[0][0]  # Total Votes


def update_Voter(voter_id, password, name, email, address, phone, dob):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    l = dob.split("-")
    d = date.today()
    s1 = d.strftime("%Y/%m/%d")
    s2 = l[0] + "/" + l[1] + "/" + l[2]
    d1 = datetime.strptime(s1, "%Y/%m/%d")
    d2 = datetime.strptime(s2, "%Y/%m/%d")
    delta = d1 - d2  # This is the difference between today and DOB given
    if delta.days // 365 < 18:  # If this is less than 18, Voter is ineligible to Vote
        cursor.close()
        db.close()
        return -1  # Still a Minor, Ineligible to Vote
    else:
        s = f"UPDATE Voter SET Password = '{password}', Name = '{name}', Email = '{email}', Address = '{address}', Phone_Number = '{phone}', DateOfBirth = '{dob}' WHERE Voter_ID = {voter_id};"
        # Update All aspects of the Voter
        cursor.execute(s)
        print(s)
        cursor.close()
        db.commit()  # Committing the changes made
        db.close()  # Closing Database and cursor
        return 1  # Update Successful


def delete_Voter(voter_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"DELETE FROM VOTER where VOTER_ID = {voter_id};"
    # Voter with a specific Voter_ID will be deleted
    cursor.execute(s)
    print(s)
    x = cursor.fetchone()
    cursor.close()
    db.commit()  # Committing the changes made
    db.close()  # Closing Database and cursor
    return 1  # Deleteion Successful


def admin_Login(admin_id, pswd):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT * FROM Admin where Admin_ID = {admin_id} AND Password = '{pswd}';"
    # Retrieve records with given Admin_ID and Password
    cursor.execute(s)
    print(s)
    x = cursor.fetchall()
    if (
        len(x) == 0
    ):  # If len(x) == 0 then no such record exists, thus invalid credentials
        cursor.close()
        db.close()
        return -1  # Wrong Credentials
    cursor.close()
    db.close()  # Closing Database and cursor
    return 1  # Successful Login


def voter_Login(voter_id, pswd):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT Name FROM Voter where Voter_ID = {voter_id} AND Password = '{pswd}';"
    # Retrieve records with given Voter_ID and Password
    cursor.execute(s)
    print(s)
    x = cursor.fetchall()
    cursor.close()
    db.close()  # Closing Database and cursor
    if (
        len(x) == 0
    ):  # If len(x) == 0 then no such record exists, thus invalid credentials
        return -1  # Wrong Credentials
    return 1  # Successful Login


def get_Elections():
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    d = date.today()
    s1 = d.strftime("%Y-%m-%d")  # Current Date
    s = f"SELECT * FROM Election WHERE Election_End_Date >= '{s1}' ORDER BY Election_Start_Date;"
    # Voters can only see those Elections which are upcoming and ongoing
    cursor.execute(s)
    print(s)
    x = cursor.fetchall()  # List of Elections
    cursor.close()
    db.close()  # Closing Database and cursor
    return x


def get_Candidates(elec_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT Candidate_ID,Name,Party_Name FROM Candidate WHERE Candidate_ID IN (SELECT Candidate_ID FROM Stands_For WHERE Election_ID = {elec_id});"
    # Get Candidates Participating in a particular Election
    cursor.execute(s)
    print(s)
    x = cursor.fetchall()  # List of Candidates
    cursor.close()
    db.close()  # Closing Database and cursor
    return x


def get_All_Elections():
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT * FROM Election ORDER BY Election_Start_Date;"
    # Gives us an Ordered Set of Elections, for
    # Admins to look at and geenrate reports
    cursor.execute(s)
    print(s)
    x = cursor.fetchall()  # List of All Elections
    cursor.close()
    db.close()  # Closing Database and cursor
    return x


def get_Election_Title(elec_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT Election_Title FROM Election WHERE Election_ID = {elec_id}"
    # Gets Election_Title from Election_ID
    cursor.execute(s)
    print(s)
    x = cursor.fetchall()  # Holds Election_Title
    cursor.close()
    db.close()  # Closing Database and cursor
    return x[0][0]


def get_Voter_Details(voter_id):
    db = mc.connect(  # Connecting with the MySQL Server
        host="localhost", user=userID, password=pwd, database="Voting_Manager"
    )
    cursor = db.cursor()  # Cursor Initialisation
    s = f"SELECT * FROM Voter WHERE Voter_ID = {voter_id}"
    # Get the Voter Details from a Particular Voter_ID
    cursor.execute(s)
    print(s)
    x = cursor.fetchall()  # Details of the Voter
    cursor.close()
    db.close()  # Closing Database and cursor
    return x[0]
