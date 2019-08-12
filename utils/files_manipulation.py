"""Files Manipulation."""
import sys

"""
   Created At: 10/08/2019
      Contact: jessika.milhomem@gmail.com
"""

def import_file(p_file) :
    file_path = "files/" + p_file
    
    with open(file_path, "r") as file:
        file_treated = [x.strip() for x in file.readlines()]
        file_read = [x.split(",") for x in file_treated]
    
    return file_read
