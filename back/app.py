import sqlite3
from src.domain.category import CategoryRepository
from src.webserver import create_app
from src.domain.note import NotesRepository
from src.domain.info import InfoRepository
from src.domain.user import UserRepository


database_path = "data/database.db"

repositories = {
    "note": NotesRepository(database_path),
    "info": InfoRepository(database_path),
    "user": UserRepository(database_path),
    "category": CategoryRepository(database_path)
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
