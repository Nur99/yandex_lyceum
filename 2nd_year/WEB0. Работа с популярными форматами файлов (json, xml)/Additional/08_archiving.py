import shutil
from datetime import datetime


def make_reserve_arc(source, dest):
    try:
        name = datetime.now().strftime('arch %Y-%m-%d %H-%M-%S')
        shutil.make_archive(name, 'zip', root_dir=source)
        shutil.copyfile(name + '.zip', f'{dest}{name}.zip')
        return True
    except Exception as E:
        print(E)
        return False


if __name__ == "__main__":
    make_reserve_arc(input(), input())
