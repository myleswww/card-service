DROP TABLE IF EXISTS card_scans;

CREATE TABLE card_scans(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id TEXT NOT NULL,
    scan_timestamp TEXT NOT NULL,
    logged_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );