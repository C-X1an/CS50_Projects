-- Schema only. No user records, password hashes or activity data.

CREATE TABLE buy_history (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
user_id INT NOT NULL,
symbol TEXT NOT NULL,
price DECIMAL(10,2) NOT NULL,
time DATETIME NOT NULL,
quantity INT NOT NULL,
FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE sell_history (
user_id INT NOT NULL,
symbol TEXT NOT NULL,
price DECIMAL(10,2) NOT NULL,
time DATETIME NOT NULL,
quantity INT NOT NULL,
FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE transaction_history (
user_id INT NOT NULL,
symbol TEXT NOT NULL,
price DECIMAL(10,2) NOT NULL,
time DATETIME NOT NULL,
quantity INT NOT NULL,
FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL, cash NUMERIC NOT NULL DEFAULT 10000.00);

CREATE UNIQUE INDEX username ON users (username);
