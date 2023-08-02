-- a script that creates a database
-- hbtn_0d_usa and the table states

CREATE IF NOT EXISTS DATABASE hbtn_0d_usa
USE hbtn_0d_usa
CREATE IF NOT EXISTS TABLE states(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
