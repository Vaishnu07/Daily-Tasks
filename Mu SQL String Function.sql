use training;

select * from employees;

SELECT ASCII(First_Name) AS NumCodeOfFirstChar
FROM employees; 

  --   Uppercase letters: A (65), B (66), C (67), ..., Z (90)
--     Lowercase letters: a (97), b (98), c (99), ..., z (122)
--     Digits: 0 (48), 1 (49), 2 (50), ..., 9 (57)
--     Punctuation marks: ! (33), " (34), # (35), ..., / (47)
--     Special characters: @ (64), [ (91), \ (92), ], ^ (94), _ (95), ` (96), { (123), | (124), } (125), ~ (126)

-- Note that the ASCII standard only covers 128 characters, which means that it is not sufficient to represent characters from all languages and scripts. As a result, other character encoding standards, such as Unicode, have been developed to support a wider range of characters.


SELECT CHAR_LENGTH("First_Name") AS LengthOfString; 

SELECT CHAR_LENGTH(First_Name) AS LengthOfName
FROM employees;

SELECT CHARACTER_LENGTH("First_Name") AS LengthOfString; 

SELECT CHARACTER_LENGTH(First_Name) AS LengthOfName
FROM employees;

SELECT CONCAT("SQL ", "Tutorial ", "is ", "fun!") AS ConcatenatedString; 

SELECT CONCAT(First_Name,' ',LAST_NAME) from employees;

SELECT CONCAT_WS("-", "SQL", "Tutorial", "is", "fun!") AS ConcatenatedString;

SELECT CONCAT_WS("_",First_Name,LAST_NAME) from employees;

SELECT FIELD("q", "s", "q", "l"); 

SELECT FIND_IN_SET("a", "s,q,l");


SELECT FORMAT(250500.5634, 2); 

SELECT FORMAT(250500.5634, 0);

SELECT INSERT("W3Schools.com", 11, 3, "no");

select substring('hello world',1,8);

select substring(First_Name, 1,5) from employees;

SELECT LCASE("SQL Tutorial is FUN!"); 

SELECT LCASE(First_Name) from employees;

SELECT UCASE("Sql Tutorial is FUN!"); 

SELECT UCASE(First_Name) from employees;

SELECT SUBSTR("SQL Tutorial", 5, 3) AS ExtractString;

SELECT SUBSTR("First_Name", 5, 3) AS ExtractString;

SELECT UPPER("SQL Tutorial is FUN!") AS UppercaseText;

SELECT UPPER(First_Name) AS UppercaseFirst_Name
FROM employees; 


SELECT TRIM('    SQL Tutorial    ') AS TrimmedString; 


SELECT STRCMP("SQL Tutorial", "HTML Tutorial");

SELECT REPEAT("SQL Tutorial", 2);

SELECT REPEAT(First_Name, 2)
FROM employees;


SELECT REVERSE(First_Name) from employees;

SELECT INSTR("W3Schools.com", "COM") AS MatchPosition; 

SELECT INSTR(First_Name, "a"), First_Name
FROM employees;