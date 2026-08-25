create database ecommerce;

use ecommerce;

SELECT COUNT(*) FROM channels;
SELECT COUNT(*) FROM deliveries;
SELECT COUNT(*) FROM drivers;
SELECT COUNT(*) FROM hubs;
SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM payments;
SELECT COUNT(*) FROM stores;

SELECT COUNT(*) AS unmatched_orders
FROM orders o
LEFT JOIN stores s
    ON o.store_id = s.store_id
WHERE s.store_id IS NULL;

SELECT COUNT(*) AS unmatched_orders
FROM orders o
LEFT JOIN channels c
    ON o.channel_id = c.channel_id
WHERE c.channel_id IS NULL;

SELECT COUNT(*) AS unmatched_orders
FROM orders o
LEFT JOIN deliveries d
    ON o.delivery_order_id = d.delivery_order_id
WHERE d.delivery_order_id IS NULL;

SELECT COUNT(*) AS unmatched_orders
FROM orders o
LEFT JOIN payments p
    ON o.payment_order_id = p.payment_order_id
WHERE p.payment_order_id IS NULL;

SELECT COUNT(*) AS unmatched_stores
FROM stores s
LEFT JOIN hubs h
    ON s.hub_id = h.hub_id
WHERE h.hub_id IS NULL;

SELECT COUNT(*) AS unmatched_deliveries
FROM deliveries d
LEFT JOIN drivers dr
    ON d.driver_id = dr.driver_id
WHERE d.driver_id IS NOT NULL
  AND dr.driver_id IS NULL;


USE Ecommerce;

DESCRIBE orders;
DESCRIBE deliveries;
DESCRIBE payments;
DESCRIBE stores;
DESCRIBE hubs;
DESCRIBE drivers;
DESCRIBE channels;
CREATE TABLE payment_summary AS
SELECT
    payment_order_id,
    SUM(payment_amount) AS total_payment_amount,
    SUM(payment_fee) AS total_payment_fee,
    COUNT(*) AS payment_count
FROM payments
GROUP BY payment_order_id;


CREATE TABLE delivery_summary AS
SELECT
    delivery_order_id,
    MAX(delivery_distance_meters) AS delivery_distance_meters,
    MAX(delivery_status) AS delivery_status,
    COUNT(*) AS delivery_count
FROM deliveries
GROUP BY delivery_order_id;

use ecommerce;


CREATE TABLE payment_summary AS
SELECT
    payment_order_id,
    SUM(payment_amount) AS total_payment_amount,
    SUM(payment_fee) AS total_payment_fee,
    COUNT(*) AS payment_count
FROM payments
GROUP BY payment_order_id;

DROP TABLE IF EXISTS delivery_summary;

CREATE TABLE delivery_summary AS
SELECT
    delivery_order_id,
    MAX(delivery_distance_meters) AS delivery_distance_meters,
    MAX(delivery_status) AS delivery_status,
    MAX(driver_id) AS driver_id,
    COUNT(*) AS delivery_count
FROM deliveries
GROUP BY delivery_order_id;

CREATE TABLE final_orders AS
SELECT
    o.*,

    s.store_name,
    s.store_segment,
    s.store_plan_price,
    s.store_latitude,
    s.store_longitude,

    c.channel_name,
    c.channel_type,

    d.delivery_distance_meters,
    d.delivery_status,
    d.delivery_count,

    dr.driver_type,
    dr.driver_modal,

    p.total_payment_amount,
    p.total_payment_fee,
    p.payment_count,

    h.hub_name,
    h.hub_city,
    h.hub_state,
    h.hub_latitude,
    h.hub_longitude

FROM orders o

LEFT JOIN stores s
    ON o.store_id = s.store_id

LEFT JOIN channels c
    ON o.channel_id = c.channel_id

LEFT JOIN delivery_summary d
    ON o.delivery_order_id = d.delivery_order_id

LEFT JOIN drivers dr
    ON d.driver_id = dr.driver_id

LEFT JOIN payment_summary p
    ON o.payment_order_id = p.payment_order_id

LEFT JOIN hubs h
    ON s.hub_id = h.hub_id;


SELECT COUNT(*) AS total_rows
FROM final_orders;

SELECT COUNT(DISTINCT order_id) AS unique_orders
FROM final_orders;