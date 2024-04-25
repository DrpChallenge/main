from pathlib import Path
import subprocess

# xml の読み込み
from xml.dom import minidom

def run_ccbs(map_path: Path, task_path: Path) -> None:
    print(f"./CCBS_binary {map_path} {task_path}")

    proc = subprocess.run([
        "./CCBS_binary", 
        map_path, task_path, "./config.xml"
    ], capture_output=True)  # 出力をキャプチャする

    if proc.returncode != 0:
        raise RuntimeError("CCBS failed")
    else:
        stdout = proc.stdout.decode()
        solution_found = "true" in stdout.lower()
        print(f"Solution found: {solution_found}")
        print("----------")


if __name__ == "__main__":
    tasks_path = Path.cwd() / "tasks"
    maps_path = Path.cwd() / "maps"

    for task_path in tasks_path.glob("*[!_log].xml"):
        doc = minidom.parse(str(task_path))
        # map_name は、task_path の task_dd_map_xxxx.xml の map_xxxx の部分
        map_name = f"map_{task_path.stem.split('_')[-1]}"
        map_path = maps_path / map_name / "map.xml"

        run_ccbs(map_path, task_path)
