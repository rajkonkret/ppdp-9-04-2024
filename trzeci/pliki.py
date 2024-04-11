# pliki - context manager
# with - context manager

# open() - otwieranie pliku
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("kolejne\n")
    fh.write("Jeszcze jedno\n")

# plik zostanie w całości nadpisany !!!
with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Radek\n")

# # dla opcji 'x' dostaniemy błąd, że plik istnieje. FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', 'x') as fh:
#     fh.write("Test")

with open('test.log', 'a', encoding='utf-8') as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")
    file.write("Dośdane\n")
    file.write("Dośćąźdane\n")

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
# Radek
# Dodane
# Dodane
# Dodane
# Dośdane
