import pandas as pd
import os
import dotenv

dotenv.load_dotenv()
from supabase import create_client, Client
from src.types import DataType

def login_to_supabase():
    # Import the credentials from the env file
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_SERVICE_ROLE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    return supabase

def get_table_as_dataframe(supabase: Client, table_name: DataType):
    table_data = supabase.table(str(table_name)).select("*").execute()
    print(f'table_data<{table_name}> length: ', len(table_data.data))
    assert(len(table_data.data) > 0)
    return pd.DataFrame(table_data.data)