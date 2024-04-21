from dotenv import dotenv_values
import libsql_experimental as libsql


# Get .env variable from dotenv lib
config = dotenv_values(".env")

#print(config.get("DB_URL"))

# Connect to the database
url = config.get("TURSO_DB_URL")
auth_token = config.get("TURSO_AUTH_TOKEN")

print(url, auth_token)
conn = libsql.connect("sql3i", sync_url=url, auth_token=auth_token)
conn.sync()


# Create a table

# conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);")


# Insert data

# conn.execute("INSERT INTO users (name, age) VALUES ('Alice', 30);")
# conn.execute("INSERT INTO users (name, age) VALUES ('devnull', 27);")
# conn.commit()


# CRUD operations

# Create

# conn.execute("INSERT INTO users (name, age) VALUES ('Bob', 25);")
# print(conn.execute("SELECT * FROM users;").fetchall())
#conn.commit()


# Update
# conn.execute("UPDATE users SET name = 'devnull' WHERE name = 'kodzer0' AND id = 2;")
# conn.commit()



# Delete
# conn.execute("DELETE FROM users WHERE name = 'Bob';")
# conn.commit()


# Read
print(conn.execute("SELECT * FROM users;").fetchall())