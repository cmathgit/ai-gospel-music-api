#!/bin/bash

# --- Configuration ---
PROMPT_DIR="./" # Current directory
BIBLE_PROMPT_FILE="bible_prompts.txt"
MNEMONIC_PROMPT_FILE="mnemonic_prompts.txt"
MAX_SIZE_KB=50
MAX_SIZE_BYTES=$((MAX_SIZE_KB * 1024))

# --- Get current timestamp for archive filenames (YYYYMMDD_HHMMSS) ---
TIMESTAMP=$(date +'%Y%m%d_%H%M%S')

echo "Checking prompt files in '${PROMPT_DIR}' for size exceeding ${MAX_SIZE_KB} KB (${MAX_SIZE_BYTES} bytes)..."
echo "Timestamp for archives: ${TIMESTAMP}"
echo ""

# --- Function to process a file ---
process_file() {
    local file_name="$1"
    local archive_prefix="$2"
    local current_file_path="${PROMPT_DIR}/${file_name}"

    if [[ -f "$current_file_path" ]]; then
        # Get file size (stat -c%s works on Linux/Cygwin)
        local file_size
        file_size=$(stat -c%s "$current_file_path")

        echo "'${file_name}' size: ${file_size} bytes."
        if [[ "$file_size" -gt "$MAX_SIZE_BYTES" ]]; then
            echo "Archiving '${file_name}' as it exceeds the size limit."
            local archive_filename="${archive_prefix}_${TIMESTAMP}.txt"
            local archive_path="${PROMPT_DIR}/${archive_filename}"

            # Copy the file
            cp "$current_file_path" "$archive_path"
            if [[ $? -ne 0 ]]; then
                echo "ERROR: Failed to copy '${file_name}' to '${archive_filename}'"
            else
                echo "Copied to '${archive_filename}'"
                # Clear the original file using redirection
                : > "$current_file_path"
                 if [[ $? -ne 0 ]]; then
                    echo "ERROR: Failed to clear original file '${file_name}'"
                else
                    echo "Cleared original file '${file_name}'."
                fi
            fi
        else
            echo "'${file_name}' is within the size limit. No action needed."
        fi
    else
        echo "'${file_name}' not found. Skipping."
    fi
    echo "" # Add a blank line after processing each file
}

# --- Process the files using the function ---
process_file "$BIBLE_PROMPT_FILE" "bible_prompts"
process_file "$MNEMONIC_PROMPT_FILE" "mnemonic_prompts"

echo "Archive check complete."
