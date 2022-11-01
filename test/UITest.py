from time import sleep

from modulepy.Manager import Manager
from pathlib import Path


if __name__ == '__main__':
    manager = Manager(Path.cwd() / "modules")
    try:
        manager.start()
        while manager.data.get("do_run"):
            sleep(0.1)
    except KeyboardInterrupt:
        manager.stop()
        manager.join()
