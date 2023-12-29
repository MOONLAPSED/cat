import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    from time import time
    from src.cat import FileTypeSelector
    fs = FileTypeSelector(directory=".", file_extension="md")
    file_dict = fs.select_files()
    
    max_processing_time = 5  # Maximum allowed processing time in seconds
    max_chars = 2_000_000  # Maximum allowed characters
    
    for file_path, file_content in file_dict.items():
        print("#" * 50)
        print("File Path:   %s" % file_path)
        print("#" * 50)
        print("File Content:")
        
        start_time = time()
        
        try:
            # Get the first 200 characters of the content
            content_start = file_content[:200]  
            
            # Check if the content exceeds the character limit
            if len(file_content) > max_chars:
                content_start = file_content[:max_chars]
                print("File truncated due to character limit:", file_path)
                
            # Check elapsed time and break if it exceeds the maximum allowed time
            elapsed_time = time() - start_time
            if elapsed_time > max_processing_time:
                print(f"Timeout exceeded for file: {file_path}. Skipping...")
                continue
            
            print("%s" % content_start)
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