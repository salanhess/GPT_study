CREATE TABLE IF NOT EXISTS sqlitemydata (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);