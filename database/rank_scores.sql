-- https://leetcode.com/problems/rank-scores/description/

-- MySql

SELECT
    s.score,
    t2.rank
FROM (
    SELECT
        score,
        ROW_NUMBER() OVER() as 'rank'
    FROM (
        SELECT
            score
        FROM Scores
        GROUP BY score
        ORDER BY score DESC
    ) as t1
) as t2
INNER JOIN Scores s ON s.score=t2.score
ORDER BY s.score DESC
