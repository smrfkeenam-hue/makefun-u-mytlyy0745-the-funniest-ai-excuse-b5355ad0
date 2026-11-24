import os


def excuse():
    return "I finished your report, then asked myself to double-check it and deleted the good version."


def main():
    if not os.path.isdir("/output"):
        os.makedirs("/output")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(excuse())


if __name__ == "__main__":
    main()
