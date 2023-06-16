USE Voting_Manager;



-- Query For Admin Login
SELECT * FROM Admin where Admin_ID = 1 AND Password = 'apassword1';

-- Query To Add Voter
INSERT INTO Voter(Password,Name,Email,Address,Phone_Number,DateOfBirth) 
VALUES('password16','Abir Abhyankar','abirabh20170@gmail.com',
'Salunke Vihar, Delhi - 111001','9103025510','2004-01-26');

-- Query To Add Candidates
INSERT INTO Candidate(Name,DOB,Age,Party_Name,Admin_ID) 
VALUES('Arjun Abhyankar','2000-09-09','22','Liberty League','1');

-- Query To Add Elections
INSERT INTO Election(Election_Start_Date,Election_End_Date,Election_Title,Admin_ID) 
VALUES('2024-05-03','2024-05-07','Lok Sabha Elections',1);

-- Query To Delete a Specific Voter
DELETE FROM VOTER where VOTER_ID = 16;

-- Query To Get Total Votes Made in an Election
SELECT COUNT(*) FROM VOTE WHERE Election_ID = 1;

-- Query To Determine Winner of an Election
SELECT Name,Party_Name  FROM Candidate NATURAL JOIN (SELECT Candidate_ID,COUNT(Candidate_ID) 
AS VOTE FROM VOTE WHERE ELECTION_ID = 1 GROUP By Candidate_ID ORDER BY VOTE DESC) 
as T ORDER BY VOTE DESC LIMIT 1;

-- Query To Determine Rank List of Candidates for an Election
SELECT Candidate_ID,Name,Party_Name  FROM Candidate NATURAL JOIN (SELECT Candidate_ID,COUNT(Candidate_ID) 
AS VOTE FROM VOTE WHERE ELECTION_ID = 1 GROUP By Candidate_ID ORDER BY VOTE DESC) as T ORDER BY VOTE DESC;

-- Query To Count Total Number of Votes Received by a Candidate in an Election
SELECT COUNT(*) FROM VOTE WHERE Candidate_ID = 1 AND Election_ID = 1;

-- Query To Calculate Percentage of Votes Received By a Candidate in an Election
SELECT COUNT(*)*100/(SELECT COUNT(*) FROM VOTE WHERE Election_ID = 1) 
FROM VOTE WHERE Candidate_ID = 1 AND Election_ID = 1; 

-- Query To Update a User's Profile
UPDATE Voter SET Password = 'password1', Name = 'Amit Singh Khurana', Email = 'amit.singh@example.com', 
Address = '34/25, Shyam Nagar, 201001', Phone_Number = '9767901970', DateOfBirth = '1990-01-01' 
WHERE Voter_ID = 1;

-- Query To Login a Voter into the System
SELECT Name FROM Voter where Voter_ID = 11 AND Password = 'password11';

-- Query To Get Ongoing and Upcoming Elections for Voters
SELECT * FROM Election WHERE Election_End_Date >= '2023-04-11' ORDER BY Election_Start_Date;

-- Query To Get Candidates who are Contesting a Particular Election
SELECT Candidate_ID,Name,Party_Name FROM Candidate WHERE Candidate_ID 
IN (SELECT Candidate_ID FROM Stands_For WHERE Election_ID = 1);

-- Query To Register A Vote
INSERT INTO Vote(Voter_ID,Candidate_ID,Election_ID) VALUES(2,5,1);