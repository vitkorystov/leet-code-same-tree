# https://leetcode.com/problems/rising-temperature/description/

# MySql

SELECT
    Id
FROM (
    SELECT
        id as 'Id',
        temperature,
        recordDate,
        LAG(temperature, 1) OVER () as previous_temperature,
        LAG(recordDate, 1) OVER () as previous_recordDate
    FROM Weather
    ORDER BY recordDate ASC
) as a
WHERE NOT previous_temperature is null AND temperature>previous_temperature
AND DATEDIFF(recordDate, previous_recordDate) = 1
