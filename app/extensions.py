import logging
import sys

# def setup_logging(log_file_path):
#     """Set up the custom log for the application."""
#     logger = logging.getLogger('model_serving_logger')
#     logger.setLevel(logging.INFO)
#     formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
#     file_handler = logging.FileHandler(log_file_path)
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#     logger.info("Application initialized")
#     return logger

# def setup_logging(log_file_path):
#     """Set up the custom log for the application."""
#     formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

#     # Configure the root logger to save messages to both file and console
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', handlers=[
#         logging.FileHandler(log_file_path),
#         logging.StreamHandler(sys.stdout)
#     ])

#     logger = logging.getLogger('model_serving_logger')
#     logger.info("Application initialized")
#     return logger