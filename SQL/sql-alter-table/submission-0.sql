CREATE TABLE books (
  id INTEGER,
  title TEXT,
  author TEXT
);
-- Do not modify above this line --
ALTER TABLE books add column published_year Integer;
ALTER TABLE books rename column id TO isbn;
ALTER TABLE books Drop column author;




-- Do not modify below this line --
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'books'
ORDER BY column_name;
