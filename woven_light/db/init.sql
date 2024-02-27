CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    schedule_time TIMESTAMP NOT NULL,
    tfl_url TEXT,
    tfl_response TEXT
);