:: run python scripts
:: python data_dictionary_dump.py

@echo off
setlocal enabledelayedexpansion

REM Set the path to your Python script
set PYTHON_SCRIPT=your_python_script.py

REM Loop 100 times
for /L %%i in (1,1,100) do (
    echo Running iteration %%i...
    python generate_song_prompts_suno_ai.py
)

echo All iterations completed.
pause
