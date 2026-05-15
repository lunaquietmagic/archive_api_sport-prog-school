AVAILABLE_REQUESTS =  {
        "MULTIPLE_TARGETS": [
            { "id": 1, "request": "/get_all_items", "description": "Получить полный список объектов из всех категорий"},
            { "id": 2, "request": "/get_all_films", "description": "Получить список всех фильмов"},
            { "id": 3, "request": "/get_all_games", "description": "Получить список всех игр"},
            { "id": 4, "request": "/get_all_anime", "description": "Получить список всех аниме"},
            { "id": 5, "request": "/get_all_series", "description": "Получить список всех сериалов"},
            { "id": 6, "request": "/get_all_books", "description": "Получить список всех книг"},
        ], 
        "SINGLE_TARGET": [
            { "id": 1, "request": "/get_film?id=1", "description": "Получить всю информацию о фильме по ID или по названию"},
            { "id": 2, "request": "/get_game/?name=Cyberpunk 2077", "description": "Получить всю информацию об игре по ID или по названию"},
            { "id": 3, "request": "/get_anime/?id=4", "description": "Получить всю информацию о аниме по ID или по названию"},
            { "id": 4, "request": "/get_series/?id=5", "description": "Получить всю информацию о сериале по ID или по названию"},
            { "id": 5, "request": "/get_book/?name=Гарри Поттер и Кубок огня", "description": "Получить всю информацию о книге по ID или по названию"},
        ]
    }
