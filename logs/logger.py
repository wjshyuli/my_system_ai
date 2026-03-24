import logging
import os
from logging.handlers import RotatingFileHandler

# 项目根目录（关键）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# logs目录
LOG_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def get_logger(name: str):
    """
    根据模块名创建logger
    每个模块一个独立日志文件
    """

    logger = logging.getLogger(name)

    # 防止重复添加handler（非常重要）
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # 日志文件名（按模块名）
    log_file = os.path.join(LOG_DIR, f"{name}.log")

    # 文件日志（自动轮转）
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5MB
        backupCount=3,
        encoding="utf-8"
    )

    # 控制台日志
    console_handler = logging.StreamHandler()

    # 格式
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger