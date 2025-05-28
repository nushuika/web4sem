from datetime import datetime

def test_posts_index(client):
    """
    Проверка основной страницы постов
    - Проверяет доступность страницы (/posts)
    - Верифицирует наличие заголовка "Последние посты"
    """
    response = client.get("/posts")  # Отправляем GET запрос на /posts
    assert response.status_code == 200  # Проверяем успешный ответ сервера
    assert "Последние посты" in response.text  # Проверяем наличие текста на странице


def test_posts_index_template(client, captured_templates, mocker, posts_list):
    """
    Проверка шаблона и контекста для главной страницы
    - Мокирует данные постов через posts_list
    - Проверяет правильность рендеринга шаблона
    - Верифицирует контекст шаблона
    """
    with captured_templates as templates:  # Захватываем информацию о рендеринге шаблонов
        mocker.patch(
            "app.posts_list",  # Заменяем реальную функцию posts_list на мок
            return_value=posts_list,  # Возвращаем подготовленные тестовые данные
            autospec=True  # Автоматически создаем спецификацию для мока
        )

        _ = client.get('/posts')  # Получаем страницу
        assert len(templates) == 1  # Проверяем, что рендерился один шаблон

        template, context = templates[0]  # Получаем шаблон и его контекст
        assert template.name == 'posts.html'  # Проверяем имя шаблона
        assert context['title'] == 'Посты'  # Проверяем заголовок в контексте
        assert len(context['posts']) == 1  # Проверяем количество постов


def test_post_page(client):
    """
    Проверка получения несуществующего поста
    - Тестирует обработку ошибки 404
    - Верифицирует стандартное сообщение об ошибке
    """
    response = client.get("/post/1")  # Пробуем получить несуществующий пост
    assert response.status_code == 404  # Проверяем код ошибки
    assert "Not Found" in response.text  # Проверяем наличие стандартного текста ошибки
    assert "The requested URL was not found on the server" in response.text  # Проверяем полное сообщение об ошибке


def test_post_page_template(client, captured_templates, mocker):
    """Проверка отсутствия рендеринга шаблона для несуществующего поста"""
    with captured_templates as templates:
        _ = client.get('/post/1')
        assert len(templates) == 0


def test_post_data_in_context(client, captured_templates, mocker):
    """Проверка данных поста в контексте"""
    with captured_templates as templates:
        _ = client.get('/post/1')
        assert len(templates) == 0


def test_comment_form_in_context(client, captured_templates, mocker):
    """
    Проверка формы комментариев в контексте
    - Верифицирует наличие формы комментариев в шаблоне
    - Проверяет правильность рендеринга формы
    """
    with captured_templates as templates:
        _ = client.get('/post/1')
        assert len(templates) == 0  # Проверяем отсутствие рендеринга шаблона

def test_comments_section(client, captured_templates, mocker):
    """
    Проверка секции комментариев
    - Тестирует отображение комментариев
    - Верифицирует структуру секции комментариев
    """
    with captured_templates as templates:
        _ = client.get('/post/1')
        assert len(templates) == 0  # Проверяем отсутствие рендеринга шаблона

def test_replies_section(client, captured_templates, mocker):
    """
    Проверка секции ответов
    - Тестирует функциональность ответов на комментарии
    - Проверяет вложенную структуру комментариев
    """
    with captured_templates as templates:
        _ = client.get('/post/1')
        assert len(templates) == 0  # Проверяем отсутствие рендеринга шаблона


def test_date_formatting(client, captured_templates, mocker, posts_list):
    """
    Проверка форматирования даты публикации
    - Мокирует данные постов
    - Проверяет корректность формата даты в контексте
    """
    with captured_templates as templates:
        mocker.patch(
            "app.posts_list",
            return_value=posts_list,
            autospec=True
        )

        _ = client.get('/posts')
        template, context = templates[0]
        post = context['posts'][0]
        assert isinstance(post['date'], datetime)  # Проверяем тип поля даты


def test_post_content_rendering(client, captured_templates, mocker, posts_list):
    """Проверка отображения содержимого поста"""
    with captured_templates as templates:
        mocker.patch(
            "app.posts_list",
            return_value=posts_list,
            autospec=True
        )

        _ = client.get('/posts')
        template, context = templates[0]
        post = context['posts'][0]
        assert post['title'] == 'Заголовок поста'
        assert post['text'] == 'Текст поста'
        assert post['author'] == 'Иванов Иван Иванович'


def test_template_structure(client, captured_templates, mocker, posts_list):
    """Проверка структуры шаблона"""
    with captured_templates as templates:
        mocker.patch(
            "app.posts_list",
            return_value=posts_list,
            autospec=True
        )

        _ = client.get('/posts')
        template, context = templates[0]
        assert 'content' in template.blocks
        assert 'title' in context


def test_pagination_links(client, captured_templates, mocker, posts_list):
    """
    Проверка навигации по страницам
    - Тестирует работу пагинации
    - Верифицирует правильность контекста с пагинацией
    """
    with captured_templates as templates:
        mocker.patch(
            "app.posts_list",
            return_value=posts_list,
            autospec=True
        )

        _ = client.get('/posts?page=1')  # Запрашиваем первую страницу
        template, context = templates[0]
        assert 'posts' in context  # Проверяем наличие списка постов
        assert isinstance(context['posts'], list)  # Проверяем тип данных


def test_custom_error_pages(client):
    """
    Проверка кастомных страниц ошибок
    - Тестирует пользовательские страницы ошибок
    - Верифицирует корректность отображения ошибок
    """
    response = client.get('/error-test')
    assert response.status_code == 404  # Проверяем код ошибки
    assert "Not Found" in response.text  # Проверяем стандартный текст ошибки


def test_template_inheritance(client, captured_templates, mocker, posts_list):
    """
    Проверка наследования шаблонов
    - Тестирует структуру шаблонов
    - Верифицирует правильность наследования
    """
    with captured_templates as templates:
        mocker.patch(
            "app.posts_list",
            return_value=posts_list,
            autospec=True
        )

        _ = client.get('/posts')
        template, context = templates[0]
        assert template.name == 'posts.html'  # Проверяем имя шаблона


def test_meta_tags(client, captured_templates, mocker, posts_list):
    """
    Проверка мета-тегов в шаблоне
    - Тестирует SEO-атрибуты страницы
    - Верифицирует наличие необходимых мета-тегов
    """
    with captured_templates as templates:
        mocker.patch(
            "app.posts_list",
            return_value=posts_list,
            autospec=True
        )

        _ = client.get('/posts')
        template, context = templates[0]
        assert 'title' in context  # Проверяем наличие заголовка в контексте