from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()
connection_str = os.environ["MONGO_HOST_URI"]

db_client: AsyncIOMotorClient = None
database = None
student_collection = None


class DB:
    def __init__(self, _mongo_uri: str):
        self._mongo_uri = _mongo_uri
        self.db_client: AsyncIOMotorClient = None
        self.db = None
        self.student_collection = None
        self.course_collection = None
        self.lecture_collection = None

    async def get_db_client(self) -> AsyncIOMotorClient:
        """Return database client instance."""
        return self.db_client

    async def connect_db(self):
        """Create database connection."""
        self.db_client = AsyncIOMotorClient(self._mongo_uri, serverSelectionTimeoutMS=5000)
        try:
            await self.db_client.server_info()
            self.db = self.db_client.students
            self.student_collection = self.db.get_collection("students_collection")
            self.course_collection = self.db.get_collection("course_collection")
            self.lecture_collection = self.db.get_collection("lecture_collection")
            self.attendance_collection = self.db.get_collection("attendance_collection")

        except Exception:
            print("Unable to connect to the server.")

    async def close_db(self):
        """Close database connection."""
        self.db_client.close()


db = DB(connection_str)
