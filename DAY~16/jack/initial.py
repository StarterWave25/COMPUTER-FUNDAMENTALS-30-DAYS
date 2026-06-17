# file_reader.py - Simple file reading using system calls

import os
import sys

def read_file(filename):
    """
    Open and read a file using system calls
    
    This demonstrates:
    - open() system call (kernel opens file)
    - read() system call (kernel reads data)
    - close() system call (kernel closes file)
    """
    
    try:
        # System call: open()
        # Kernel checks: does file exist? Do I have permission?
        file_handle = open(filename, 'r')
        
        # System call: read()
        # Kernel reads from disk and gives data to program
        data = file_handle.read()
        
        # System call: close()
        # Kernel closes the file handle
        file_handle.close()
        
        return data
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None

# Main program
if __name__ == "__main__":
    # Get filename from command line
    if len(sys.argv) < 2:
        print("Usage: python file_reader.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    content = read_file(filename)
    
    if content:
        print("File contents:")
        print("-" * 50)
        print(content)
        print("-" * 50)