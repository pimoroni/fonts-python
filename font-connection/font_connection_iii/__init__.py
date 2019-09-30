import os
import glob

font_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files')

font_files = {}

for font in list(glob.glob(os.path.join(font_directory, "*.otf"))):
    font_name = os.path.basename(font).replace(".otf", "").replace("-Regular", "").replace("-", "")
    font_files[font_name] = font
    globals()[font_name] = font
