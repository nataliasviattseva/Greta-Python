import os


class FilePath():
    def __init__(self, fichier):
        self.fichier = str(fichier)

    def __str__(self):
        abs_path = os.path.abspath(__file__)
        pth_dir_1 = os.path.dirname(abs_path)
        pth_dir_2 = os.path.dirname(pth_dir_1)
        fch_path = os.path.join(pth_dir_2, self.fichier)
        return fch_path

