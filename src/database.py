import sqlite3

class DatabaseManager:
    """Class which manages game's database.

    Attributes:
        db_name: File identification.'
        db: Database abstraction.
        connect(): Calls the function needed to establish a database connection.
    """

    def __init__(self, db_name="scoreBase.db"):
        self.db_name = db_name
        self.db = None
        self.connect()

    def connect(self):
        """Establishes database connection.
        """
        try:
            self.db = sqlite3.connect(self.db_name)
            print(f"Connected to the database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close_database(self):
        """Closes database connection.
        """
        try:
            if self.db:
                self.db.close()
                print("Database connection closed.")
            else:
                print("No database connection to close.")
        except sqlite3.Error as e:
            print(f"Error closing the database: {e}")

    def create_database(self):
        """Create a database if it does not already exist.
        """
        try:
            self.db = sqlite3.connect(self.db_name)
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT name FROM sqlite_master WHERE type='table' AND name='Records';
            """)
            table_exists = cursor.fetchone()

            if not table_exists:
                self.db.execute("""
                    CREATE TABLE Records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        score INTEGER UNIQUE,
                        time INTEGER
                    )
                """)
                print("Table 'Records' created.")
            else:
                print("Table 'Records' already exists.")

            cursor.close()

        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def delete_record(self, score, time):
        """Deletes game score records from database
        when the data is no longer statistically significant.

        Args:
            score (int): Game's point score.
            time (str): Game's time score.
        """
        try:
            self.db.execute(
                "DELETE FROM Records WHERE score=? AND time=?",
                (score, time)
            )
            print(f"Record deleted: Score = {score}, Time = {time}")
        except sqlite3.Error as e:
            print(f"Error deleting record: {e}")

    def fetch_ranked_scores(self):
        """Imports the five best score from the database.
        """
        try:
            stats = self.db.execute("""
                SELECT ROW_NUMBER() OVER (ORDER BY score DESC, time), score, time
                FROM Records
            """).fetchall()
            return stats
        except sqlite3.Error as e:
            print(f"Error fetching ranked scores: {e}")
            return []

    def get_last_score(self):
        """Imports the last score from database.

        Returns:
            str: The last score.
        """
        try:
            last_score = self.db.execute(
                "SELECT score FROM Records ORDER BY score DESC LIMIT 1"
            ).fetchone()[0]
            return last_score
        except sqlite3.Error as e:
            print(f"Error fetching last score: {e}")
            return None

    def get_last_time(self):
        """Imports the last time score from database.

        Returns:
            str: The last time score.
        """
        try:
            last_time = self.db.execute(
                "SELECT time FROM Records ORDER BY score DESC LIMIT 1"
            ).fetchone()[0]
            return last_time
        except sqlite3.Error as e:
            print(f"Error fetching last time: {e}")
            return None

    def get_max_score(self):
        """Imports the best score from database.

        Returns:
            str: The best score.
        """
        try:
            max_score = self.db.execute("SELECT MAX(score) FROM Records").fetchone()[0]
            return max_score
        except sqlite3.Error as e:
            print(f"Error fetching max score: {e}")
            return None

    def get_table_count(self):
        """Imports the number of scores from database.

        Returns:
            str: Number of scores.
        """
        try:
            table_count = self.db.execute("SELECT COUNT(score) FROM Records").fetchone()[0]
            return table_count
        except sqlite3.Error as e:
            print(f"Error fetching table count: {e}")
            return 0

    def insert_score(self, score, time):
        """Adds a new score to database.

        Args:
            score (int): Thel last point score.
            time (str): The last time score.
        """
        try:
            self.db.execute(
                "INSERT INTO Records (score, time) VALUES (?, ?)",
                (score, time)
            )
            self.db.commit()
            print(f"Record inserted: Score = {score}, Time = {time}")
        except sqlite3.Error as e:
            print(f"Error inserting record: {e}")
