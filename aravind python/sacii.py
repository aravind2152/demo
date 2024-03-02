from ascii_magic import AsciiArt

my_art = AsciiArt.from_image('i.jpg')
my_art.to_html_file('ascii_art.html', columns=200, width_ratio=2)