from time import sleep

## Globals ##
STDOUT_CLEAR = "\x1b[2K"

def countdown(minutes):
    for i in range(minutes*60, 0, -1):
        print(" {}{}:{:0>2d}".format(STDOUT_CLEAR, i//60, i%60), end="\r", flush=True)
        sleep(1)
    stdout.write("\n")


def main():
    countdown(int(input("Enter a time in minutes: ")))

if __name__ == "__main__":
    main()
