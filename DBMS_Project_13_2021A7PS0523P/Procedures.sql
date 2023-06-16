USE Voting_Manager;

-- Procedure to Get Voter-ID
DELIMITER //
CREATE PROCEDURE add_Voter(
IN pswd VARCHAR(50),
IN naem VARCHAR(50),
IN emai VARCHAR(50),
IN addre VARCHAR(100),
IN phone CHAR(10),
IN dob DATE)
BEGIN 
INSERT INTO VOTER(Password,Name,Email,Address,Phone_Number,DateOfBirth)
VALUES (Passwrd,n1,emai,addre,phone,dob);
END //
DELIMITER ;

-- Procedure to Register A Vote
DELIMITER // 
CREATE PROCEDURE add_Vote(
IN voter INT,
IN cand INT,
IN elec INT)
BEGIN 
INSERT INTO VOTE(Voter_ID,Candidate_ID,Election_ID)
VALUES (voter,cand,elec);
END //
DELIMITER ;

-- Procedure to get Percentage of Votes Received by a Candidate
DELIMITER // 
CREATE PROCEDURE get_Vote_Percentage(
IN cand INT,
IN elec INT)
BEGIN 
SELECT COUNT(*)*100/(SELECT COUNT(*) FROM VOTE WHERE Election_ID = elec) 
FROM VOTE WHERE Candidate_ID = cand AND Election_ID = elec;
END //
DELIMITER ;

-- Procedure to Get Voter-ID
DELIMITER // 
CREATE PROCEDURE get_Voter_ID(
IN pswd VARCHAR(50),
IN naem VARCHAR(50),
IN emai VARCHAR(50),
IN addre VARCHAR(100),
IN phone CHAR(10),
IN dob DATE)
BEGIN 
SELECT Voter_ID FROM VOTER WHERE Password = pswd AND Name = naem AND Email = emai AND Address = addre AND Phone_Number = phone AND DateOfBirth = dob;
END //
DELIMITER ;