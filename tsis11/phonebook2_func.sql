CREATE OR REPLACE PROCEDURE delete_user(who_is_del text)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook2 WHERE name = who_is_del OR phone = who_is_del;
END;
$$;


DROP FUNCTION add_many_users;
CREATE OR REPLACE FUNCTION add_many_users(add_names text[], add_numbers text[])
RETURNS text[]
LANGUAGE plpgsql
AS $$
DECLARE
    incor_number text[];
    i integer;
BEGIN
    FOR i IN 1..array_length(add_names, 1) LOOP
        IF (LENGTH(add_numbers[i]) = 5) AND add_numbers[i] ~ '^[0-9]+$' THEN
             INSERT INTO phonebook2 VALUES (add_names[i], add_numbers[i]);
        ELSE
             incor_number = array_append(incor_number, add_numbers[i]);
        END IF;
    END LOOP;
	return(incor_number);

END;
$$;

CREATE OR REPLACE FUNCTION return_all_same_user(same_res text)
RETURNS TABLE(name_user character varying, phone_user character varying) AS $$
BEGIN
    RETURN QUERY SELECT *
                 FROM phonebook2
                 WHERE name ~ same_res OR
                 phone ~ same_res;

END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE add_or_update_user(new_user text, new_number text)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT * FROM phonebook2 WHERE name = new_user) THEN
        UPDATE phonebook2 SET phone =  new_number WHERE name = new_user;
    ELSE
        INSERT INTO phonebook2 VALUES (new_user, new_number);
    END IF;

END;
$$;

CREATE OR REPLACE FUNCTION get_users_between_rows(start_row integer, number_row integer)
RETURNS TABLE(user_names character varying, phone_numbers character varying) AS $$
BEGIN
    RETURN QUERY SELECT *
                 FROM phonebook2
                 ORDER BY name
                 LIMIT number_row
                 OFFSET start_row - 1;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM phonebook2;