import logging
import os
from typing import Optional

class TodoLogger:
    def __init__(self, log_file: str = "logs/Todo.log", log_level=logging.DEBUG):
        self.log_file = log_file
        self.log_level = log_level
        self.logger = logging.getLogger("todo_logger")
        self.logger.setLevel(self.log_level)
        self._setup_handlers()

    def _setup_handlers(self):
        # Avoid adding multiple handlers during app reloads (e.g. with uvicorn)
        if self.logger.handlers:
            return

        # Ensure the log directory exists
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # File handler
        file_handler = logging.FileHandler(self.log_file, mode='a')
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        ))

        # Console output handler (optional)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        ))

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def info(self, msg: str): 
        self.logger.info(msg)

    def debug(self, msg: str): 
        self.logger.debug(msg)

    def warning(self, msg: str): 
        self.logger.warning(msg)

    def error(self, msg: str): 
        self.logger.error(msg)

    def critical(self, msg: str): 
        self.logger.critical(msg)

    def exception(self, msg: str, exc: Optional[Exception] = None):
        self.logger.error(f"{msg} - Exception: {exc}", exc_info=True)
