from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.note import NotesRepository, Note
from src.domain.category import CategoryRepository, Category


def test_should_return_empty_list_of_categories():
    category_repository = CategoryRepository(temp_file())
    app = create_app(repositories={"category": category_repository})
    client = app.test_client()

    response = client.get("/api/categories")

    assert response.json == []


def test_should_save_category_and_return_list_of_categories():
    category_repository = CategoryRepository(temp_file())
    app = create_app(repositories={"category": category_repository})
    client = app.test_client()

    category_repository.save(Category("cat-1", "Deporte"))
    category_repository.save(Category("cat-2", "Comida"))

    response = client.get(
        "/api/categories", headers={"Authorization": "Joseba_1"})

    assert response.json == [
        {
            "id_cat": "cat-1",
            "name": "Deporte",
        },
        {
            "id_cat": "cat-2",
            "name": "Comida",
        }

    ]
