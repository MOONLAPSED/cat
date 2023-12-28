import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
