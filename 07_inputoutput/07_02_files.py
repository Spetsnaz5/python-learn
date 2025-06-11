# 覆蓋寫入
with open("output.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This will overwrite existing content.")
    
# 附加寫入
with open("output.txt", "a") as file:
    file.write("\nAdding a new line at the end.")
    
# 一次讀完整個檔案
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
    
# 逐行讀取
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())