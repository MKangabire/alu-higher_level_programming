-- a script that creates a database
-- hbtn_0d_usa and the table states

CREATE IF NOT EXISTS DATABASE hbtn_0d_usa
CREATE TABLE states(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
