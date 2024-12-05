import sqlite3


class DatabaseManager:

    def __init__(self, db_name="scoreBase.db"):
        self.db_name = db_name
        self.db = None
        self.connect()

    def connect(self):
        try:
            self.db = sqlite3.connect(self.db_name)
            print(f"Connected to the database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close_database(self):
        try:
            if self.db:
                self.db.close()
                print("Database connection closed.")
            else:
                print("No database connection to close.")
        except sqlite3.Error as e:
            print(f"Error closing the database: {e}")

    def create_database(self):
        try:
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS Records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    score INTEGER UNIQUE,
                    time INTEGER
                )
            """)
            print("Table 'Records' is ready.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def delete_record(self, score, time):
        try:
            self.db.execute(
                "DELETE FROM Records WHERE score=? AND time=?",
                [score, time]
            )
            print(f"Record deleted: Score = {score}, Time = {time}")
        except sqlite3.Error as e:
            print(f"Error deleting record: {e}")

    def fetch_ranked_scores(self):
        try:
            stats = self.db.execute("""
                SELECT ROW_NUMBER() OVER (ORDER by score DESC, time), score, time
                FROM Records
            """).fetchall()
            return stats
        except sqlite3.Error as e:
            print(f"Error fetching ranked scores: {e}")
            return []

    def get_last_score(self):
        try:
            last_score = self.db.execute(
                "SELECT score FROM Records ORDER BY score DESC LIMIT 1"
            ).fetchone()[0]
            return last_score
        except sqlite3.Error as e:
            print(f"Error fetching last score: {e}")
            return None

    def get_last_time(self):
        try:
            last_time = self.db.execute(
                "SELECT time FROM Records ORDER BY score DESC LIMIT 1"
            ).fetchone()[0]
            return last_time
        except sqlite3.Error as e:
            print(f"Error fetching last time: {e}")
            return None

    def get_max_score(self):
        try:
            max_score = self.db.execute("SELECT MAX(score) FROM Records").fetchone()[0]
            return max_score
        except sqlite3.Error as e:
            print(f"Error fetching max score: {e}")
            return None

    def get_table_count(self):
        try:
            table_count = self.db.execute("SELECT COUNT(score) FROM Records").fetchone()[0]
            return table_count
        except sqlite3.Error as e:
            print(f"Error fetching table count: {e}")
            return 0

    def insert_score(self, score, time):
        try:
            self.db.execute(
                "INSERT INTO Records (score, time) VALUES (?, ?)",
                [score, time]
            )
            print(f"Record inserted: Score = {score}, Time = {time}")
        except sqlite3.Error as e:
            print(f"Error inserting record: {e}")