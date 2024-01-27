-- Active: 1705064804951@@127.0.0.1@5432@postgres@public
-- Вибірка всіх записів
5209

SELECT * FROM erampe;
-- Вибірка записів з умовою WHERE
SELECT * FROM erampe WHERE Document = 'DALLocument 7';
-- Оновлення значення в стовпчику "Description"
UPDATE erampe SET Description = 'New Description' WHERE Document = 'DALLocument 7';
-- Вставка нового запису
INSERT INTO erampe (Document, Description, Column3, Column4) VALUES ('New Document', 'New Description', 3, 22);
-- Видалення запису за певною умовою
DELETE FROM erampe WHERE Document = 'DALLocument 7';
-- Вибірка конкретних стовпчиків для всіх записів
SELECT Document, Description FROM erampe;
-- Вибірка унікальних значень в стовпчику "Column3"
SELECT DISTINCT Column3 FROM erampe;
-- Вибірка кількості записів за певною умовою
SELECT COUNT(*) FROM erampe WHERE Column3 > 5;
-- Сортування результатів за зростанням у стовпчику "Description"
SELECT * FROM erampe ORDER BY Description ASC;
-- Групування та виведення кількості записів за значеннями в стовпчику "Column3"
SELECT Column3, COUNT(*) as Count FROM erampe GROUP BY Column3;
-- Вибірка записів з об'єднанням таблиць за певною умовою
SELECT * FROM erampe
INNER JOIN other_table ON erampe.Document = other_table.Document;
-- Вибірка середнього значення у стовпчику "Column4"
SELECT AVG(Column4) as AvgColumn4 FROM erampe;
-- Обмеження кількості повернутих записів
SELECT * FROM erampe LIMIT 10;
-- Вибірка записів, які відповідають певному шаблону в стовпчику "Description"
SELECT * FROM erampe WHERE Description LIKE '%search_term%';
-- Вибірка максимального значення у стовпчику "Column3" за групами
SELECT Column3, MAX(Column3) as MaxColumn3 FROM erampe GROUP BY Column3;
-- Вибірка записів, які відповідають певній умові відносно двох стовпчиків
SELECT * FROM erampe WHERE Column3 > 5 AND Column4 < 20;
-- Вибірка кількості записів, які мають непорожнє значення в стовпчику "Description"
SELECT COUNT(*) FROM erampe WHERE Description IS NOT NULL;
-- Оновлення значення в одному стовпчику на основі значення в іншому стовпчику
UPDATE erampe SET Column4 = Column4 * 1.1 WHERE Column3 > 5;
-- Видалення дублікатів на основі значення стовпчика "Document"
DELETE s1 FROM erampe s1, erampe s2 WHERE s1.Document = s2.Document AND s1.id > s2.id;
-- Вибірка найменшого значення в стовпчику "Column4" за умови, що значення у стовпчику "Column3" менше 10
SELECT MIN(Column4) as MinColumn4 FROM erampe WHERE Column3 < 10;