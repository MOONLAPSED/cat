import requests
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from time import time
from src.cat import FileTypeSelector



def main():
    fs = FileTypeSelector(directory=".", file_extension="md")
    file_dict = fs.select_files()
    
    total_elapsed_time = 0  # Initialize total elapsed time variable
    total_files = FileTypeSelector.count_files(fs.directory)
    start_time = time()
    max_processing_time = 5  # Set maximum allowed processing time per file
    
    for file_path, file_content in file_dict.items():
        print("#" * 50)
        print("File Path:   %s" % file_path)
        print("#" * 50)
        print("File Content:")
        
        try:
            content_start = file_content[:200]  # Get the first 200 characters of the content
            
            elapsed_time = time() - start_time
            if elapsed_time > max_processing_time:
                print(f"Timeout exceeded for file: {file_path}. Skipping...")
                continue
            
            total_elapsed_time += elapsed_time
            time_per_file = total_elapsed_time / total_files
            
            if time_per_file > max_processing_time:
                print("Processing time exceeded. Skipping remaining files.")
                break

            print("%s" % content_start)
            print(f"Elapsed time: {elapsed_time} seconds")
            print(f"Time per file: {time_per_file} seconds")

        except Exception as e:
            print(f"Error reading file: {file_path}")
            print(f"Error message: {str(e)}")
        
        print("@" * 50)
        print("File Path:   %s" % file_path)
        print("@" * 50)


if __name__ == "__main__":
    from pydantic import BaseModel, Field
    from datetime import datetime, date
    from dotenv import load_dotenv
    load_dotenv

    class MySettings(BaseModel):
        required_int: int = Field(0, ge=0)
        required_str: str = "hello world"
        required_date: date = Field(default_factory=datetime.now().date)
    
    MainSettings = MySettings()
    assert MainSettings.required_int == 0
    assert MainSettings.required_str == "hello world"
    print(MainSettings.required_date)
    main()