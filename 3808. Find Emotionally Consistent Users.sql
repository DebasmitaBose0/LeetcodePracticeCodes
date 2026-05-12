WITH total_counts AS (
    SELECT 
        user_id,
        COUNT(*) AS total_reactions
    FROM reactions
    GROUP BY user_id
),
reaction_counts AS (
    SELECT 
        user_id,
        reaction,
        COUNT(*) AS cnt
    FROM reactions
    GROUP BY user_id, reaction
),
dominant AS (
    SELECT 
        r.user_id,
        r.reaction AS dominant_reaction,
        r.cnt,
        t.total_reactions,
        ROW_NUMBER() OVER (PARTITION BY r.user_id ORDER BY r.cnt DESC, r.reaction) AS rn
    FROM reaction_counts r
    JOIN total_counts t
    ON r.user_id = t.user_id
)
SELECT 
    user_id,
    dominant_reaction,
    ROUND(cnt * 1.0 / total_reactions, 2) AS reaction_ratio
FROM dominant
WHERE rn = 1
  AND total_reactions >= 5
  AND (cnt * 1.0 / total_reactions) >= 0.6
ORDER BY reaction_ratio DESC, user_id ASC;