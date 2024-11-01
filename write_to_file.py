import json
import random
import os
import shutil
from datetime import datetime
from biblegateway_api import get_bible_votd_kjv, get_bible_votd_amp, get_bible_votd_msg

def check_and_write_to_file(filename, bup_file_prefix, new_text):
    # Define the maximum file size in bytes (5 KB)
    max_size = 5 * 1024 * 10
    
    # Get the size of the file
    file_size = os.path.getsize(filename)
    
    if file_size < max_size:
        # Append the new text if the file size is less than 5 KB
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(new_text)
    else:
        # Create a backup with a timestamp if the file size is 5 KB or more
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f"log/{bup_file_prefix}_{timestamp}.txt"
        
        # Copy the original file to the backup file
        shutil.copy2(filename, backup_filename)
        
        # Overwrite the original file with the new text
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(new_text)
            
        print(f"File size exceeded 5 KB. Prompt history cleared and data written. Created backup: {backup_filename}")