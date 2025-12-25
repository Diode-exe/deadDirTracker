import os
from datetime import datetime

class deadDirScanCls():
    def scan(root):
        data = []
        for dirpath, dirnames, filenames in os.walk(root):
            for name in filenames:
                path = os.path.join(dirpath, name)
                try:
                    mtime = os.path.getmtime(path)
                    human_time = datetime.fromtimestamp(mtime).astimezone()
                    human_time = human_time.replace(microsecond=0)
                    formatted_human_time = human_time.strftime("%Y-%m-%d %H:%M:%S %z")
                    data.append((path, mtime, human_time.isoformat()))
                    # print(data)
                except (PermissionError, FileNotFoundError, OSError):
                    continue
        data.sort(key=lambda item: item[1])
        print(data)
        with open("deadDir.txt", "w", encoding="utf-8") as f:
            for path, mtime, human_time_iso in data:
                f.write(f"{path} {mtime} {human_time_iso}\n")

root = r"C:\\Users\\Rohan\\Documents\\python"
deadDirScanCls.scan(root)