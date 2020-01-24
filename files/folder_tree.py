import pathlib


def folder_tree(f):
    t = "\n"
    for folder in pathlib.Path(f).iterdir():
        t += f"{folder}\n"
        try:
            folder = "C:\\" + folder[3:]
            for subfolder in pathlib.Path(folder).iterdir():
                t += f"\t{subfolder}\n"
        except "'WindowsPath' object is not subscriptable":
            continue
        except "catching classes that do not inherit from BaseException is not allowed":
            continue
    print(t)


if __name__ == "__main__":
    folder_tree("C:\\")