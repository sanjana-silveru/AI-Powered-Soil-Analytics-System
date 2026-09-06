CREATE TABLE farm (
    farm_id SERIAL PRIMARY KEY,
    farm_name VARCHAR(100) NOT NULL,
    location VARCHAR(150),
    farmer_name VARCHAR(100)
);

CREATE TABLE field (
    field_id SERIAL PRIMARY KEY,
    farm_id INT NOT NULL,
    field_name VARCHAR(100) NOT NULL,
    area_acres DECIMAL(10,2),
    FOREIGN KEY (farm_id) REFERENCES farm(farm_id)
);

CREATE TABLE soil_sample (
    sample_id SERIAL PRIMARY KEY,
    field_id INT NOT NULL,
    sample_date DATE NOT NULL,
    nitrogen_n DECIMAL(10,2),
    phosphorus_p DECIMAL(10,2),
    potassium_k DECIMAL(10,2),
    ph DECIMAL(5,2),
    soil_moisture DECIMAL(6,2),
    organic_matter DECIMAL(6,2),
    FOREIGN KEY (field_id) REFERENCES field(field_id)
);
-- SAMPLE FARM RECORDS
INSERT INTO farm (farm_name, location, farmer_name)
VALUES
('Green Valley Farm', 'Telangana', 'Sample Farmer 1'),
('Sunrise Farm', 'Andhra Pradesh', 'Sample Farmer 2');


-- SAMPLE FIELD RECORDS
INSERT INTO field (farm_id, field_name, area_acres)
VALUES
(1, 'Field A', 5.50),
(1, 'Field B', 3.20),
(2, 'Field A', 7.00);


-- SAMPLE SOIL SAMPLE RECORDS
INSERT INTO soil_sample
(field_id, sample_date, nitrogen_n, phosphorus_p, potassium_k,
 ph, soil_moisture, organic_matter)
VALUES
(1, '2026-09-01', 50.55, 53.36, 48.15, 6.47, 20.15, 5.47),
(2, '2026-09-02', 60.00, 45.00, 55.00, 6.80, 22.50, 6.20),
(3, '2026-09-03', 40.00, 35.00, 42.00, 6.20, 18.00, 4.80);