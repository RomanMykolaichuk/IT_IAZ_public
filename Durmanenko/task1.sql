-- Вибірка всіх записів
SELECT * FROM sampe;
-- Вибірка записів з умовою WHERE
SELECT * FROM sampe WHERE Document = 'Document 7';
-- Оновлення значення в стовпчику "Description"
UPDATE sampe SET Description = 'New Description' WHERE Document = 'Document 7';
-- Вставка нового запису
INSERT INTO sampe (Document, Description, Column3, Column4) VALUES ('New Document', 'New Description', 3, 22);
-- Видалення запису за певною умовою
DELETE FROM sampe WHERE Document = 'Document 7';
-- Вибірка конкретних стовпчиків для всіх записів
SELECT Document, Description FROM sampe;
-- Вибірка унікальних значень в стовпчику "Column3"
SELECT DISTINCT Column3 FROM sampe;
-- Вибірка кількості записів за певною умовою
SELECT COUNT(*) FROM sampe WHERE Column3 > 5;
-- Сортування результатів за зростанням у стовпчику "Description"
SELECT * FROM sampe ORDER BY Description ASC;
-- Групування та виведення кількості записів за значеннями в стовпчику "Column3"
SELECT Column3, COUNT(*) as Count FROM sampe GROUP BY Column3;
-- Вибірка записів з об'єднанням таблиць за певною умовою
SELECT * FROM sampe
INNER JOIN other_table ON sampe.Document = other_table.Document;
-- Вибірка середнього значення у стовпчику "Column4"
SELECT AVG(Column4) as AvgColumn4 FROM sampe;
-- Обмеження кількості повернутих записів
SELECT * FROM sampe LIMIT 10;
-- Вибірка записів, які відповідають певному шаблону в стовпчику "Description"
SELECT * FROM sampe WHERE Description LIKE '%search_term%';
-- Вибірка максимального значення у стовпчику "Column3" за групами
SELECT Column3, MAX(Column3) as MaxColumn3 FROM sampe GROUP BY Column3;
-- Вибірка записів, які відповідають певній умові відносно двох стовпчиків
SELECT * FROM sampe WHERE Column3 > 5 AND Column4 < 20;
-- Вибірка кількості записів, які мають непорожнє значення в стовпчику "Description"
SELECT COUNT(*) FROM sampe WHERE Description IS NOT NULL;
-- Оновлення значення в одному стовпчику на основі значення в іншому стовпчику
UPDATE sampe SET Column4 = Column4 * 1.1 WHERE Column3 > 5;
-- Видалення дублікатів на основі значення стовпчика "Document"
DELETE s1 FROM sampe s1, sampe s2 WHERE s1.Document = s2.Document AND s1.id > s2.id;
-- Вибірка найменшого значення в стовпчику "Column4" за умови, що значення у стовпчику "Column3" менше 10
SELECT MIN(Column4) as MinColumn4 FROM sampe WHERE Column3 < 10;