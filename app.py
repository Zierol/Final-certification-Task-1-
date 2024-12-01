import os
import sys
import datetime

path = '/'

def main():
 if len(sys.argv) > 1:
  name = sys.argv[1]
 else:
  name = "User"

 current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 print(f"Hello, {name}! Current time: {current_time}")

 total_files = count_files(path)
 print(f"Total number of files: {total_files}")

 largest_files = top_10_largest_files(path)
 print("Top 10 largest files (in KB):")
 for file, size in largest_files:
  print(f"{file}: {size:.2f} KB")
def count_files(directory):
    return sum([len(files) for _, _, files in os.walk(directory)])

def top_10_largest_files(directory):
    files_with_size = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(filepath) / 1024  # в Кб
                files_with_size.append((filepath, size))
            except OSError:
                continue

    top_files = sorted(files_with_size, key=lambda x: x[1], reverse=True)[:10]
    return top_files



if __name__ == "__main__":
    main()