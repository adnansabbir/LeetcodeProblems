# Write your MySQL query statement below
SELECT score, DENSE_RANK() over (order by score desc) as 'Rank'
FROM Scores
ORDER BY Score DESC