-- cript that lists all records of the table.
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)

SELECT  score, name -- selecciona las columnas 'scire' y 'name'
FROM second_table
ORDER BY score DESC; -- ordena los resultados en orden desendiente