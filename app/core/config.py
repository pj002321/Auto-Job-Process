# Last Updated : 2026-08-27

""" 전역 상수,설정 값등을 정의한다.
    경로, 모델 이름, 전역 변수, 표준 라이브러리 및 경로 등을 정의
"""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT / 'data'
DB_PATH = DATA_DIR / ''
EMBED_MODEL = ...
EMBED_TOKENIZER = ...

EMBED_MAX_TOKENS = ...
EMBED_BATCH_SIZE = ...
EMBED_DEVICE = "cpu"

EMBED_NORMALIZE = ...

if not Path(DB_PATH).exists():
    print(f"알림: DB가 아직 없다 -> {DB_PATH}")