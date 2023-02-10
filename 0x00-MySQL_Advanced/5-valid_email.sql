-- Script that creates a trigger that resets te attribute

DELIMETER $$;
CREATE TRIGGER validate BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		IF NEW.email != OLD.email THEN
			SET NEW.valid_email = 0;
		END IF;
END;$$
delimeter;
