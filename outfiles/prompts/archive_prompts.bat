@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

:: --- Configuration ---
SET "PROMPT_DIR=./"
SET "BIBLE_PROMPT_FILE=bible_prompts.txt"
SET "MNEMONIC_PROMPT_FILE=mnemonic_prompts.txt"
SET /A MAX_SIZE_KB=50
SET /A MAX_SIZE_BYTES=%MAX_SIZE_KB% * 1024

:: --- Get current timestamp for archive filenames (YYYYMMDD_HHMMSS) ---
FOR /F "tokens=2 delims==" %%I in ('wmic os get LocalDateTime /value') do SET "dt=%%I"
SET "YYYY=%dt:~0,4%"
SET "MM=%dt:~4,2%"
SET "DD=%dt:~6,2%"
SET "HH=%dt:~8,2%"
SET "Min=%dt:~10,2%"
SET "Sec=%dt:~12,2%"
SET "TIMESTAMP=%YYYY%%MM%%DD%_%HH%%Min%%Sec%"

ECHO Checking prompt files in "%PROMPT_DIR%" for size exceeding %MAX_SIZE_KB% KB (%MAX_SIZE_BYTES% bytes)...
ECHO Timestamp for archives: %TIMESTAMP%
ECHO.

:: --- Process Bible Prompts File ---
SET "CURRENT_FILE_PATH=%PROMPT_DIR%\%BIBLE_PROMPT_FILE%"
IF EXIST "%CURRENT_FILE_PATH%" (
    FOR %%F IN ("%CURRENT_FILE_PATH%") DO SET /A FILE_SIZE=%%~zF
    ECHO "%BIBLE_PROMPT_FILE%" size: !FILE_SIZE! bytes.
    IF !FILE_SIZE! GTR %MAX_SIZE_BYTES% (
        ECHO Archiving "%BIBLE_PROMPT_FILE%" as it exceeds the size limit.
        :: Construct the desired archive filename: bible_prompts._YYYYMMDD_HHMMSS.txt
        SET "ARCHIVE_FILENAME=bible_prompts_!TIMESTAMP!.txt"
        SET "ARCHIVE_PATH=!PROMPT_DIR!\!ARCHIVE_FILENAME!"
        COPY "!CURRENT_FILE_PATH!" "!ARCHIVE_PATH!" > NUL
        IF ERRORLEVEL 1 (
            ECHO ERROR: Failed to copy "!BIBLE_PROMPT_FILE!" to "!ARCHIVE_FILENAME!"
        ) ELSE (
            ECHO Copied to "!ARCHIVE_FILENAME!"
            :: Clear the original file
            COPY NUL "!CURRENT_FILE_PATH!" /Y > NUL
            IF ERRORLEVEL 1 (
                ECHO ERROR: Failed to clear original file "!BIBLE_PROMPT_FILE!"
            ) ELSE (
                ECHO Cleared original file "!BIBLE_PROMPT_FILE!".
            )
        )
    ) ELSE (
        ECHO "%BIBLE_PROMPT_FILE%" is within the size limit. No action needed.
    )
) ELSE (
    ECHO "%BIBLE_PROMPT_FILE%" not found. Skipping.
)
ECHO.

:: --- Process Mnemonic Prompts File ---
SET "CURRENT_FILE_PATH=%PROMPT_DIR%\%MNEMONIC_PROMPT_FILE%"
IF EXIST "%CURRENT_FILE_PATH%" (
    FOR %%F IN ("%CURRENT_FILE_PATH%") DO SET /A FILE_SIZE=%%~zF
    ECHO "%MNEMONIC_PROMPT_FILE%" size: !FILE_SIZE! bytes.
    IF !FILE_SIZE! GTR %MAX_SIZE_BYTES% (
        ECHO Archiving "%MNEMONIC_PROMPT_FILE%" as it exceeds the size limit.
        :: Construct the desired archive filename: mnemonic_prompts_YYYYMMDD_HHMMSS.txt
        SET "ARCHIVE_FILENAME=mnemonic_prompts_!TIMESTAMP!.txt"
        SET "ARCHIVE_PATH=!PROMPT_DIR!\!ARCHIVE_FILENAME!"
        COPY "!CURRENT_FILE_PATH!" "!ARCHIVE_PATH!" > NUL
        IF ERRORLEVEL 1 (
            ECHO ERROR: Failed to copy "!MNEMONIC_PROMPT_FILE!" to "!ARCHIVE_FILENAME!"
        ) ELSE (
            ECHO Copied to "!ARCHIVE_FILENAME!"
            :: Clear the original file
            COPY NUL "!CURRENT_FILE_PATH!" /Y > NUL
            IF ERRORLEVEL 1 (
                ECHO ERROR: Failed to clear original file "!MNEMONIC_PROMPT_FILE!"
            ) ELSE (
                ECHO Cleared original file "!MNEMONIC_PROMPT_FILE!".
            )
        )
    ) ELSE (
        ECHO "%MNEMONIC_PROMPT_FILE%" is within the size limit. No action needed.
    )
) ELSE (
    ECHO "%MNEMONIC_PROMPT_FILE%" not found. Skipping.
)
ECHO.

ECHO Archive check complete.
ENDLOCAL
PAUSE
