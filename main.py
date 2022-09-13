
# import pandas as pd
from typing import Literal
import pandas as pd
from src._supabase import login_to_supabase, get_table_as_dataframe
from datetime import datetime
from typing import get_args

from src.types import DataType
DATA_PKL_DIR = 'data/pkl/'



def save_df_to_pickle(df: pd.DataFrame, type: DataType):
    filename = f'{str(type)}_{datetime.now().isoformat()}.pkl'
    df.to_pickle(f'{DATA_PKL_DIR}{filename}')
    print(f'Saved to pickle file: {filename} in directory: {DATA_PKL_DIR}')

def main():
    # login to supabase as service-role
    supabase = login_to_supabase()
    # Get the data from all supabase tables 
    for type in get_args(DataType):
        df = get_table_as_dataframe(supabase, type)
        save_df_to_pickle(df, type)

if __name__ == '__main__':
    main()