import pkg_resources

pkg_resources.declare_namespace(__name__)

font_files = {}

for entry_point in pkg_resources.iter_entry_points('fonts_fonts'):
    font_files.update(entry_point.load())

for font in font_files:
    globals()[font] = font_files[font]
