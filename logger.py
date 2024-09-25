import logging
import os


def get_logger() -> logging.Logger:
    """Настривает и возвращает логгер под запросы SqlAlchemy."""

    output_file = os.path.join('log', "sqlalchemy.log")

    logging.basicConfig(
        filename=output_file,
        level=logging.INFO,
    )

    # Создание обработчика для вывода логов SQLAlchemy
    sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
    sqlalchemy_logger.setLevel(logging.INFO)

    # Добавление обработчика для записи логов в файл
    file_handler = logging.FileHandler(output_file)
    file_handler.setLevel(logging.INFO)

    # Форматирование логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавление обработчика к логгеру
    sqlalchemy_logger.addHandler(file_handler)

    return sqlalchemy_logger
