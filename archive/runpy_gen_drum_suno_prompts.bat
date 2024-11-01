:: run python scripts
:: python data_dictionary_dump.py

@echo off
setlocal enabledelayedexpansion

REM Set the path to your Python script
set PYTHON_SCRIPT=generate_drum_loop_prompts_suno_ai.py

REM Loop 100 times
for /L %%i in (1,1,1000) do (
    echo Running iteration %%i...
    python !PYTHON_SCRIPT!
)

echo All iterations completed.
pause
