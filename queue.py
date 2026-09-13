def run_cmd_with_queue(cmd, queue):
    # pass

queue = []

def main():
    n = int(input())

    for _ in range(n):
        command = input().split()
        run_cmd_with_queue(command, queue)

if __name__ == "__main__":
    main()