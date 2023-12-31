import os
from time import time
from src.cat import FileTypeSelector
from pydantic import BaseModel, Field
from datetime import datetime, date
from dotenv import load_dotenv

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


class MySettings(BaseModel):
    required_date: date = Field(default_factory=datetime.now().date)
    required_int: int = Field(0, ge=0)  # Set default value here
    state: int = Field(0)  # New field to hold the state value

    def __init__(self):
        super().__init__()
        try:
            self.required_int = int(os.getenv("REQUIRED_INT", default=0))
            self.state = int(os.getenv("STATE", default=0))  # Load 'state' from .env file
        except ValueError:
            pass  # Use the default value

if __name__ == "__main__":
    load_dotenv()  # Load environment variables

    settings = MySettings()
    settings.state = 1  # Set the state to 1
    
    with open('.env', 'w') as env_file:
        env_file.write(f"STATE={settings.state}\n")  # Update state in .env file
    
    fs = FileTypeSelector(directory=".", file_extension="md")
    file_dict = fs.select_files()
    
    # Rest of your code remains unchanged

    main()

    # Update state to 0 after main() completes
    settings.state = 0
    with open('.env', 'w') as env_file:
        env_file.write(f"STATE={settings.state}\n")
