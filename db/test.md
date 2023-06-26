```
SELECT DATE_FORMAT(t1.dt, '%Y-%m-%d') AS date,
       CONCAT(HOUR(t1.dt), ':', MINUTE(t1.dt), ':', SECOND(t1.dt)) AS time1,
       t1.temp AS temp1,
       t1.shibu,
       t1.condact,
       t1.do_per,
       t1.do_mg,
       CONCAT(HOUR(t2.dt), ':', MINUTE(t2.dt), ':', SECOND(t2.dt)) AS time2,
       t2.temp AS temp2,
       t2.shibu,
       t2.condact,
       t2.do_per,
       t2.do_mg
FROM place1_tank1 AS t1
JOIN place1_tank1 AS t2 ON DATE(t1.dt) = DATE(t2.dt) AND HOUR(t1.dt) = 10 AND HOUR(t2.dt) = 15
WHERE MINUTE(t1.dt) = 0 AND MINUTE(t2.dt) = 0;
```

```
SELECT DATE_FORMAT(t1.dt, '%Y-%m-%d') AS date,
       CONCAT(HOUR(t1.dt), ':', MINUTE(t1.dt), ':', SECOND(t1.dt)) AS time1,
       t1.temp AS temp1,
       t1.shibu,
       t1.condact,
       t1.do_per,
       t1.do_mg
FROM place1_tank1 as t1 where (HOUR(dt) = 10 AND MINUTE(dt) = 0);
```
```
SELECT DATE_FORMAT(t2.dt, '%Y-%m-%d') AS date,
       CONCAT(HOUR(t2.dt), ':', MINUTE(t2.dt), ':', SECOND(t2.dt)) AS time2,
       t2.temp AS temp2,
       t2.shibu,
       t2.condact,
       t2.do_per,
       t2.do_mg
FROM place1_tank1 as t2 where (HOUR(dt) = 15 AND MINUTE(dt) = 0);
```
```
SELECT t1.date, t1.time1, t1.temp1, t1.shibu, t1.condact, t1.do_per, t1.do_mg,
       t2.time2, t2.temp2, t2.shibu, t2.condact, t2.do_per, t2.do_mg
FROM
(
    SELECT DATE_FORMAT(t1.dt, '%Y-%m-%d') AS date,
           CONCAT(HOUR(t1.dt), ':', MINUTE(t1.dt), ':', SECOND(t1.dt)) AS time1,
           t1.temp AS temp1,
           t1.shibu,
           t1.condact,
           t1.do_per,
           t1.do_mg
    FROM place1_tank1 AS t1
    WHERE HOUR(t1.dt) = 15 AND MINUTE(t1.dt) = 0
) AS t1
LEFT JOIN
(
    SELECT DATE_FORMAT(t2.dt, '%Y-%m-%d') AS date,
           CONCAT(HOUR(t2.dt), ':', MINUTE(t2.dt), ':', SECOND(t2.dt)) AS time2,
           t2.temp AS temp2,
           t2.shibu,
           t2.condact,
           t2.do_per,
           t2.do_mg
    FROM place1_tank1 AS t2
    WHERE HOUR(t2.dt) = 10 AND MINUTE(t2.dt) = 0
) AS t2
ON t1.date = t2.date;
```

```

```