from os import listdir, rename, path

class Renamer:
    @staticmethod
    def renameFile (filename: str, filenameFinally: str) -> None: 
        rename(filename, filenameFinally);

    def renameAllFiles (self, pathToFolder: str, choice: str) -> None:
        index: int = 1;
        for file in listdir(pathToFolder):
            if (path.isfile(pathToFolder+file)):
                name, form = file.split(".");
                if (index < 10):
                    name = "%s0%i.%s" % (choice, index, form);
                else: 
                    name = "%s%i.%s" % (choice, index, form);
                print("%s -> %s" % (file, name));
                self.renameFile(pathToFolder+file, pathToFolder+name);
                index += 1;