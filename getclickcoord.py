import subprocess
import threading

def read_output(pipe):
    while True:
        line: str = pipe.readline()
        if not line:
            break
        if 'ABS_MT_POSITION_X' in line or 'ABS_MT_POSITION_Y' in line:
            tokens = line.split()
            print(tokens[-2], int(tokens[-1], 16))

# ADB 命令
adb_command = "adb -s emulator-5560 shell getevent -l"

# 執行 ADB 命令
process = subprocess.Popen(adb_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

# 创建线程来读取标准输出和标准错误
thread_stdout = threading.Thread(target=read_output, args=(process.stdout,))
thread_stderr = threading.Thread(target=read_output, args=(process.stderr,))

# 启动线程
thread_stdout.start()
thread_stderr.start()

# 等待线程完成
thread_stdout.join()
thread_stderr.join()
