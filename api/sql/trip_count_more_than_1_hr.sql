SELECT
  TO_CHAR(r.pickup_time, 'YYYY-MM') AS month,
  CONCAT(a.first_name, ' ', a.last_name) AS full_name,
  COUNT(
    CASE
      WHEN EXTRACT(EPOCH FROM (re.created_at - r.pickup_time)) > 3600
      THEN 1
    END
  ) AS "Count of Trips > 1 hr"
FROM
  api_ride r
JOIN
  api_rideevent re ON r.id = re.id_ride_id
JOIN
  api_user a ON a.id = r.id_driver_id
WHERE
  r."status" = 'DroppedOff'
GROUP BY
  r.id_driver_id,
  a.first_name,
  a.last_name,
  TO_CHAR(r.pickup_time, 'YYYY-MM')
ORDER BY
  full_name,
  month,
  r.id_driver_id;
