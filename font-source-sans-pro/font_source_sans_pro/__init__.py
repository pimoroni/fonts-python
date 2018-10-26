import os
import glob

font_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files')

font_files_ttf = {}
font_files_otf = {}

for font in list(glob.glob(os.path.join(font_directory, "*.otf"))):
    font_name = os.path.basename(font).replace(".otf", "").replace("-Regular", "").replace("-", "")
    font_files_otf[font_name] = font
    globals()[font_name] = font

for font in list(glob.glob(os.path.join(font_directory, "*.ttf"))):
    font_name = os.path.basename(font).replace(".ttf", "").replace("-Regular", "").replace("-", "")
    font_files_ttf[font_name] = font

