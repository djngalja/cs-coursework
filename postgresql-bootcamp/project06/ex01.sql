WITH RECURSIVE res AS (
  SELECT '{' || point1 AS tour, point1, point2, cost, 0 AS cnt
  FROM roads
  WHERE point1 = 'a'
  UNION ALL
  SELECT res.tour || ',' || roads.point1 AS tour,
    roads.point1, roads.point2,
    res.cost + roads.cost, cnt + 1
  FROM res INNER JOIN roads ON res.point2 = roads.point1
  WHERE tour NOT LIKE '%' || roads.point1 || '%'
),
final_res AS (
  SELECT cost AS total_cost, tour || ',' || point2 || '}' as tour
  FROM res
  WHERE point2 = 'a' AND cnt IN (SELECT MAX(cnt) FROM res)
)
SELECT * 
FROM final_res
WHERE total_cost IN (SELECT MIN(total_cost) FROM final_res)
  OR total_cost IN (SELECT MAX(total_cost) FROM final_res)
ORDER BY 1, 2;