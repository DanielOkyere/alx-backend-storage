-- SQL scripts that ranks the country origins of bands, order by the num

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
