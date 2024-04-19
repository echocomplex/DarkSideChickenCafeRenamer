from Renamer import Renamer
import os


def main () -> None:
    path: str = input("Enter path >> ");
    assert os.path.exists(path), "DEBIL! NET PAPKI!";
    assert os.path.isdir(path), "THIS IS NOT A FOLDER DEBIL";
    choice: str = input("boot/force? >> ");
    assert (choice in ("boot", "force")), "Da blyat, boot or force?";
    unit = Renamer();
    unit.renameAllFiles("/Users/mac/Documents/project-codes/Python/4raven/", choice);

if (__name__ == "__main__"):
    main();