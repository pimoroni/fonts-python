import pkg_resources

fonts = {}

for entry_point in pkg_resources.iter_entry_points('pyfont_fonts'):
    fonts.update(entry_point.load())

print(fonts)

