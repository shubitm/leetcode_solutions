WITH First_Login AS (
    SELECT 
        player_id, 
        MIN(event_date) AS first_login_date
    FROM 
        Activity
    GROUP BY 
        player_id
),
Next_Day_Login AS (
    SELECT 
        fl.player_id
    FROM 
        First_Login fl
    JOIN 
        Activity a ON fl.player_id = a.player_id 
                   AND a.event_date = DATE_ADD(fl.first_login_date, INTERVAL 1 DAY)
)
SELECT 
    ROUND(COUNT(DISTINCT ndl.player_id) / COUNT(DISTINCT fl.player_id), 2) AS fraction
FROM 
    First_Login fl
LEFT JOIN 
    Next_Day_Login ndl ON fl.player_id = ndl.player_id