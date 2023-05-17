SELECT w2.id FROM weather w1, weather w2
WHERE w2.recordDate = DATE_ADD(w1.recordDate, INTERVAL 1 DAY) AND w1.temperature < w2.temperature;