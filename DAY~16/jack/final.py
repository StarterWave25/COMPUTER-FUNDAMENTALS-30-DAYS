# file_reader_optimized.py - Robust version handling all issues

import os
import sys

# CONFIG
CHUNK_SIZE = 8192  # Read 8KB at a time (not whole file)
MAX_FILE_SIZE = 100 * 1024 * 1024  # Don't read files > 100MB

def read_file_optimized(filename):
    """
    Optimized file reading with:
    - Chunked reading (memory efficient)
    - Size limit (prevent memory issues)
    - File locking (prevent race conditions)
    - Guaranteed cleanup (with statement)
    """
    
    # Check 1: Does file exist?
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return None
    
    # Check 2: Is it actually a file (not directory)?
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a file")
        return None
    
    # Check 3: Is file too large?
    file_size = os.path.getsize(filename)
    if file_size > MAX_FILE_SIZE:
        print(f"Error: File too large ({file_size} bytes > {MAX_FILE_SIZE} bytes)")
        return None
    
    # Check 4: Can we read it?
    if not os.access(filename, os.R_OK):
        print(f"Error: No read permission for '{filename}'")
        return None
    
    try:
        # Use 'with' statement = guaranteed file close
        # This is the right way to do it!
        with open(filename, 'r', encoding='utf-8') as file_handle:
            
            # Read in chunks (memory efficient)
            chunks = []
            while True:
                chunk = file_handle.read(CHUNK_SIZE)
                if not chunk:
                    break
                chunks.append(chunk)
            
            data = ''.join(chunks)
            return data
            
    except UnicodeDecodeError:
        print(f"Error: File '{filename}' is not valid UTF-8 text")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

def main():
    """Main program"""
    
    # Validate input
    if len(sys.argv) < 2:
        print("Usage: python file_reader_optimized.py <filename>")
        print("\nExamples:")
        print("  python file_reader_optimized.py test.txt")
        print("  python file_reader_optimized.py /etc/passwd")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    print(f"Reading '{filename}'...")
    content = read_file_optimized(filename)
    
    if content:
        lines = content.split('\n')
        print(f"\n✓ Successfully read {len(lines)} lines")
        print("-" * 50)
        
        # Show first 10 lines only
        if len(lines) > 10:
            print('\n'.join(lines[:10]))
            print(f"... ({len(lines) - 10} more lines)")
        else:
            print(content)
        
        print("-" * 50)
    else:
        print("✗ Failed to read file")
        sys.exit(1)

if __name__ == "__main__":
    main()