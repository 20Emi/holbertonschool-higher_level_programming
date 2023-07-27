-- creates the table unique_id on your MySQL server.
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)

CREATE TABLE unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);