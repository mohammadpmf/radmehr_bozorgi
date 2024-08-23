from pathlib import Path
directory = Path(r'C:\Users\Mohammad\Desktop\My own students\3 Radmehr Bozorgi\44 20 Mordad 1403')
file_path = directory/'yourfile'
directory.mkdir(parents=True, exist_ok=True)
file_path.open('w')