-- a script that creates the table
-- id_not_null on mysql

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
	);
