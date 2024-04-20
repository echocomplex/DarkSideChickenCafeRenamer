from Renamer import Renamer
import os


def main () -> None:
    path: str = input("Enter path >> ");
    assert os.path.exists(path), "DEBIL! NET PAPKI!";
    assert os.path.isdir(path), "THIS IS NOT A FOLDER DEBIL";
    if (path[-1] != "/"):
        path += "/"
    choice: str = input("boot/font/force/blst/clsh? >> ");
    assert (choice in ("boot", "font", "force", "blst", "clsh")), "Da blyat, boot or font or force or blst or clsh?";
    unit = Renamer();
    unit.renameAllFiles(path, choice);

if (__name__ == "__main__"):
    main();
