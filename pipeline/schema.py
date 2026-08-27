# Last Updated : 2026-08-27

""" data폴더에 있는 *.csv 파일들을 *.db 파일로 적재한다.

"""

import csv
import sqlite3
import sys
from pathlib import Path
from app.core.config import DB_PATH,ROOT,DATA_DIR

def read_csv(path: str):
    pass

def looks_int(text: str):
    pass

def looks_real(text: str):
    pass

def looks_date(text: str):
    pass

def infer_type(values: str):
    pass

def infer_pk(columns: str, rows: str):
    pass

def owner_of(columns: str, tables: str):
    pass