SELECT `family`, COUNT(*), MIN(`masse_surfacique`), MAX(`masse_surfacique`), MIN(`masse_combustible`), MAX(`masse_combustible`)
FROM `materials`
GROUP BY `family`