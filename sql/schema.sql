-- ADHD Latin America Synthetic Dataset Schema
-- v1.2.0

CREATE TABLE adhd_latam_estimates (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    prevalence DECIMAL(10, 5),
    incidence DECIMAL(10, 5),
    n_cases INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_country_year ON adhd_latam_estimates(country, year);
