import os
from glob import glob

logs = sorted(glob("logs/*.md"))
latest = logs[-1] if logs else None

with open("README.md", "w") as f:
    f.write("# Today I Did 🌱\n\n")
    f.write("| 日付 | 完了タスク |\n|------|------------|\n")
    for log in logs[-7:]:
        date_str = os.path.basename(log).replace(".md","")
        f.write(f"| {date_str} | 0/0 |\n") 
    f.write("\n⏳ 連続更新日数: {}\n".format(len(logs)))
