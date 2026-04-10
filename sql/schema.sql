CREATE TABLE adhd_latin_america (
    country VARCHAR(100),
    year INTEGER,
    prevalence_rate FLOAT,
    incidence_rate FLOAT,
    case_numbers BIGINT,
    PRIMARY KEY (country, year)
);
