import sqlite3

# Connect to the database (creates database.db if it doesn’t exist)
conn = sqlite3.connect('database.db')

# Create users table (if it doesn’t already exist)
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    pin TEXT,
    role TEXT
)
''')

# Create profiles table (linked to users by email)
conn.execute('''
CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT UNIQUE,
    bio TEXT,
    skills TEXT,
    experience_level TEXT,
    rate_per_video TEXT,
    budget_range TEXT,
    niche TEXT,
    FOREIGN KEY (user_email) REFERENCES users(email)
)
''')

# Insert a test user (only if not already in database)
conn.execute('''
INSERT OR IGNORE INTO users (name, email, pin, role)
VALUES ('Test User', 'test@example.com', '1234', 'Content Creator')
''')

conn.commit()
conn.close()

print('✅ Database setup complete with test user: test@example.com / 1234')
