import os
from pathlib import Path

def main():
    check_desktop = os.path.exists(r"C:\Users\tomis\Desktop")
    check_directory = os.path.isdir(r"C:\Users\tomis\Desktop\write_code")
    check_cwd = os.getcwd()


    print(check_desktop)
    print(check_directory)
    print(check_cwd)


    if check_cwd.endswith("justcode"):
        print("Du bist im richtigen Verzeichnis")
    else:
        print("fuckin Loser!")


    if check_desktop:
        print(r"Desktop befindet sich unter -> C:\Users\tomis\Desktop")
    else:
        print("No Desktop here!")


if __name__ == "__main__":
    main()