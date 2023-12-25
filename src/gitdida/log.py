"""
自定义 logging 的设置，提供get_logger 函数。
耗费了一周左右，才得到正确的文件 😭
"""
import logging
import logging.config
from datetime import datetime
from pathlib import Path
from gitdida.config import settings

# Default log file like: logs/2023-12.log
# 增加代码确保 log 路径可用
log_path_str = settings.LOG_PATH
log_path = Path(log_path_str)
log_path.mkdir(parents=True, exist_ok=True)
log_file_name = log_path / f"{datetime.now().strftime('%Y-%m')}.log"


def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter


log_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {"format": "%(asctime)s [%(levelname)s] %(name)s - %(message)s"},
        "simple_no_time": {"format": "===%(levelname)s=== %(name)s - %(message)s"},
    },
    "filters": {"warnings_and_below": {"()": filter_maker, "level": "WARNING"}},
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple_no_time",
            "stream": "ext://sys.stdout",
            "filters": ["warnings_and_below"],  # 避免高级错误重复显示。
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple_no_time",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "filename": log_file_name,
            "mode": "a",
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
        },
        "Rotatefile": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": log_file_name,
            "maxBytes": 1024 * 1024 * 1024 * 1,  # 1M
            "backupCount": "5",
            "encoding": "utf-8",
        },
    },
    "root": {"level": logging.DEBUG, "handlers": ["stderr", "stdout", "file"]},
}


logging.config.dictConfig(log_config)


def get_logger(name=None):
    """
    其他模块引用 logger 入口。
    """
    if name is None:
        return logging.getLogger("root")
    else:
        return logging.getLogger(name)
