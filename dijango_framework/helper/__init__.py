import os.path
from pathlib import Path
from environ import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
print(ROOT_DIR)

env = environ.Env(
    WAIT_TIMEOUT=(int, 10),
    BROWSER=(str, 'CHROME'),
    HEADLESS=(bool, True),
)

if os.path.exists(str(Path(ROOT_DIR / '.env'))):
    env.read_env(str(Path(ROOT_DIR / '.env')))