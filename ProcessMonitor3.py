import os
import psutil
import time
import argparse

def create_log_directory(log_dir="Marvellous"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def get_running_processes():
    process_list = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            pinfo = proc.info
            vms_mb = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms_mb
            process_list.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_list

def log_processes(log_dir="Marvellous"):
    create_log_directory(log_dir)
    separator = "-" * 80
    log_path = os.path.join(log_dir, f"MarvellousLog{time.strftime('%Y-%m-%d %H-%M-%S')}.log")

    with open(log_path, 'w') as f:
        f.write(f"{separator}\n")
        f.write(f"Marvellous Infosystems Process Logger: {time.ctime()}\n")
        f.write(f"{separator}\n")

        processes = get_running_processes()
        for process in processes:
            f.write(f"{process}\n")

def main():
    parser = argparse.ArgumentParser(description="Log record of running processes")
    parser.add_argument("log_dir", help="Directory to save log files")
    args = parser.parse_args()

    try:
        log_processes(args.log_dir)
        print("Process information logged successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
