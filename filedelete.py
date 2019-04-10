import os
path = 'D:/TableauBackup'
file_list = os.listdir(path)

for files in range(0,len(file_list)):
    file_date = os.path.getatime(path+'/'+file_list[files])
    print(file_list[files],file_date)

while 1:
    if len(file_list) <= 10 :
        print("break...")
        break
    else :
        os.system('forfiles /p "D:\TableauBackup" /s /m *.* /d -10 /c "cmd /c del @path"')
        print("10개이상 파일 삭제...")
        break
