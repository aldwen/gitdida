"""Log"""
import logging
from datetime import datetime
from pathlib import Path
from gitdida.config import settings

# 目前不支持设置日志记录级别，感觉没有意义
# file_log_level_str = str(settings.LOGLEVEL).upper()
# file_log_level = logging.getLevelName(file_log_level_str)

# Default log file like: logs/2023-12.log
# 增加代码确保 log 路径可用
# 如果 logpath 没有读取到，应当报错跳出。
log_path_str = settings.LOG_PATH
log_path = Path(log_path_str)
log_path.mkdir(parents=True, exist_ok=True)
log_file_name = log_path / f"{datetime.now().strftime('%Y-%m')}.log"

# 不支持设置日志格式
# if settings.log_verbose:
#     log_format = (
#         "%(asctime)s [%(name)s] [%(levelname)s] %(process)d %(thread)d %(message)s"
#     )
# else:
log_format = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"

# 配置根日志记录器
logging.basicConfig(
    format=log_format,
    level=logging.INFO,
    # datefmt="%Y-%m-%dT%H:%M:%S.%s+0800",  # 如果需要带时区的时间戳
)

# 添加控制台处理器 使用 DEBUG 级别
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
console_handler.setLevel(logging.DEBUG)
# logging.getLogger().addHandler(console_handler)

if not any(
    isinstance(handler, logging.StreamHandler)
    for handler in logging.getLogger().handlers
):
    logging.getLogger().addHandler(console_handler)

# 添加文件处理器 使用 INFO 级别
file_handler = logging.FileHandler(log_file_name)
file_handler.setFormatter(logging.Formatter(log_format))
file_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(file_handler)


def get_logger(name=None):
    if name is None:
        return logging.getLogger("Default")
    else:
        return logging.getLogger(name)
