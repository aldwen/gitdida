import logging
from datetime import datetime

log_format = "%(asctime)s [%(name)s] [%(levelname)s] %(message)s"

# Todo: 从配置文件里读取自定义 log 路径
# Default log file like: logs/2023-12.log
log_file_name = f"logs/{datetime.now().strftime('%Y-%m')}.log"

# 添加控制台处理器
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logging.getLogger().addHandler(console_handler)

# 添加文件处理器
file_handler = logging.FileHandler(log_file_name)
file_handler.setFormatter(logging.Formatter(log_format))
logging.getLogger().addHandler(file_handler)

# 配置根日志记录器
logging.basicConfig(
    format=log_format,
    level=logging.INFO,
    datefmt="%Y-%m-%dT%H:%M:%S.%s+0800",  # 如果需要带时区的时间戳
)


def get_logger(name=None):
    if name is None:
        return logging.getLogger("Default")
    else:
        return logging.getLogger(name)


# -------
# """Log"""
# import logging
# import os
# from logging.config import dictConfig

# from gitdida.config import settings

# os.makedirs(settings.LOGPATH, exist_ok=True)


# def verbose_formatter(verbose: int) -> str:
#     """formatter factory"""
#     if verbose is True:
#         return "verbose"
#     return "simple"


# def update_log_level(debug: bool, level: str) -> str:
#     """update log level"""
#     if debug is True:
#         level_num = logging.DEBUG
#     else:
#         level_num = logging.getLevelName(level)
#     settings.set("LOGLEVEL", logging.getLevelName(level_num))
#     return settings.LOGLEVEL


# def init_log() -> None:
#     """Init log config."""
#     log_level = update_log_level(settings.DEBUG, str(settings.LOGLEVEL).upper())

#     log_config = {
#         "version": 1,
#         "disable_existing_loggers": False,
#         "formatters": {
#             "verbose": {
#                 "format": "%(asctime)s %(levelname)s %(name)s %(process)d %(thread)d %(message)s",
#             },
#             "simple": {
#                 "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
#             },
#         },
#         "handlers": {
#             "console": {
#                 "formatter": verbose_formatter(settings.VERBOSE),
#                 "level": "DEBUG",
#                 "class": "logging.StreamHandler",
#             },
#             "file": {
#                 "class": "logging.handlers.RotatingFileHandler",
#                 "level": "DEBUG",
#                 "formatter": verbose_formatter(settings.VERBOSE),
#                 "filename": os.path.join(settings.LOGPATH, "all.log"),
#                 "maxBytes": 1024 * 1024 * 1024 * 200,  # 200M
#                 "backupCount": "5",
#                 "encoding": "utf-8",
#             },
#         },
#         "loggers": {
#             "": {"level": log_level, "handlers": ["console"]},
#         },
#     }

#     dictConfig(log_config)
