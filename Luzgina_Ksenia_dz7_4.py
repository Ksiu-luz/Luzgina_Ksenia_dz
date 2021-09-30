import os

files = []

print(os.getcwd())

for r, d, f in os.walk(os.getcwd()):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)

max_size = max(files)

i = 1
result_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    result_dict[i] = 0

for file in files:
    result_dict[10 ** len(str(file))] += 1

print(result_dict)
