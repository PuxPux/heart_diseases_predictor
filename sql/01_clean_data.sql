DROP TABLE IF EXISTS ml_patients;

CREATE TABLE ml_patients AS 
SELECT
    CAST (age AS REAL) AS age, 
    CAST (anaemia AS INTEGER) AS anaemia, 
    CAST (creatinine_phosphokinase AS INTEGER) as cpk,
    CAST (diabetes AS INTEGER) AS diabetes, 
    CAST (ejection_fraction AS INTEGER ) as ejection_fraction,
    CAST (high_blood_pressure AS INTEGER) as high_bp, 
    CAST (platelets AS REAL) AS platelets, 
    CAST (serum_creatinine AS REAL) AS serum_creatinine, 
    CAST (serum_sodium AS INTEGER) AS serum_sodium, 
    CAST (sex AS INTEGER) AS sex, 
    CAST (smoking AS INTEGER) AS smoking, 
    CAST (time AS INTEGER) as days_followed,
    CAST ("DEATH_EVENT" AS INTEGER) AS target
FROM raw_patients;
