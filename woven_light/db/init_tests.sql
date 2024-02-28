CREATE TABLE test_tasks (
    id SERIAL PRIMARY KEY,
    schedule_time TIMESTAMP NOT NULL,
    tfl_url TEXT,
    tfl_response TEXT,
    scrape_time TIMESTAMP
);


INSERT INTO test_tasks (schedule_time, tfl_url) VALUES (NOW() + INTERVAL '3 minute', 'bakerloo,jubilee');
INSERT INTO test_tasks (schedule_time, tfl_url) VALUES (NOW() + INTERVAL '3 minute', 'bakerloo,victoria');
INSERT INTO test_tasks (schedule_time, tfl_url) VALUES (NOW() - INTERVAL '10 minute', 'central,jubilee');