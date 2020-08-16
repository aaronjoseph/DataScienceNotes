Suppose there are two columns
Age Name
25   Nitin
30   Amit
27   Rishab
29   Ankush

Convert into
Name   Nitin.  Amit. Rishab. Ankush
Age.      25.       30.      27.        29

Without using pivot

With CTE As
(SELECT Age, Name, ROW_NUMBER() OVER() As Row_Number
FROM table)
SELECT
MAX(CASE Name WHEN ‘Nitin’ Then Age End) Nitin,
MAX(CASE Name WHEN ‘Amit’ Then Age End) Amit,
MAX(CASE Name WHEN ‘Rishab’ Then Age End) Rishab,
MAX(CASE Name WHEN ‘Ankush’ Then Age End) Ankush
FROM CTE
GROUP BY Row_Number