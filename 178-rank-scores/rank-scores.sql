# Write your MySQL query statement below
SELECT score, ((SELECT COUNT(DISTINCT Score) from Scores S2 where S1.score < S2.score) + 1) as 'Rank'
FROM Scores S1
GROUP BY S1.SCORE, S1.id
ORDER BY S1.Score DESC