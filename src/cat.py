import datetime
import dotenv
import logging
import matplotlib.pyplot as plt
import numpy as np
import openai
import os
import pandas as pd
import pathlib
import re
import requests
import select
import signal
import subprocess
import sys
import time
import typing
import typing_extensions

class FileTypeSelector:
    """
    This class helps you select files of a specific type from a directory and its subdirectories.
    """

    def __init__(self, directory="..", file_extension="txt", logging_level=logging.INFO):
        """
        Args:
            directory: The directory to search for files. Defaults to the current directory.
            file_extension: The file extension to select. Defaults to "txt".
            logging_level: The logging level for the class. Defaults to logging.INFO.
        """
        self.directory = directory
        self.file_extension = file_extension
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging_level)

    def select_files(self):
        """
        This method selects files of the specified type and returns a dictionary containing their paths and contents.

        Returns:
            A dictionary where each key is a file path and each value is the contents of the corresponding file.
        """
        file_dict = {}
        for file_path in pathlib.Path(self.directory).glob(f"**/*.{self.file_extension}"):
            try:
                with open(file_path, "r") as file:
                    file_content = file.read()
                file_dict[str(file_path)] = file_content
                self.logger.info(f"Processed file: {file_path}")
            except IOError as e:
                self.logger.error(f"Error processing file: {file_path}", exc_info=True)

        if not file_dict:
            self.logger.info(f"No files found with extension '{self.file_extension}'")

        return file_dict
