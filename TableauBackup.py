# -*- coding: utf-8 -*-
import tableauserverclient as TSC
import os
import time

# 오늘 날짜 가져옴
def get_today() :
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year,now.tm_mon,now.tm_mday)
    return s
# 폴더 생성
def make_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

root_dir = "D:/TableauBackup"
today = get_today()
work_dir = root_dir + "/" + today

make_folder(work_dir)


# create an auth object
'''tableau_auth = TSC.TableauAuth('admin', 'dpfwlghkgkr2018!')'''
tableau_auth = TSC.TableauAuth('admin', 'Planit0801!')
# create an instance for your server
'''server = TSC.Server('http://150.150.103.183:80')'''
server = TSC.Server('http://121.162.253.213:8000')

'''화학버전server.version = '3.1'''
server.version = '3.0'

# get 1) workbook id list and download workbook
#     2) datasource
#for i in range(0,len(sitelist)):
#여기!!!!!
'''tableau_auth = TSC.TableauAuth('admin', 'dpfwlghkgkr2018!', site_id='')'''
tableau_auth = TSC.TableauAuth('admin', 'Planit0801!', site_id='MktSales')
work_dir_workbook = work_dir + "/workbook"
work_dir_data = work_dir +"/datasource"
work_dir_user = work_dir + "/user"
work_dir_job = work_dir + "/job"
make_folder(work_dir_workbook)
make_folder(work_dir_data)
make_folder(work_dir_user)
make_folder(work_dir_job)

#with server.auth.sign_in(tableau_auth):

# 1) workbook
#with server.auth.sign_in(tableau_auth):
with server.auth.sign_in(tableau_auth):
    print(tableau_auth)
    all_workbooks, pagination_item = server.workbooks.get()
    workbooklist = []
    workbookname =[]
    #get workbook id list
    for workbook in (all_workbooks):
        workbooklist.append(workbook.id)
        workbookname.append(workbook.name)
    print("GET 워크북 리스트 성공")
    print(workbooklist)
    # download workbook
    for i in range(0, len(workbooklist)):
        server.workbooks.download(workbooklist[i], filepath=work_dir_workbook+"/"+workbookname[i]+".twbx")
    print("DOWN 워크북 리스트 성공")

# 2) datasource
    #get datasource id list

    all_datasources, pagination_item = server.datasources.get()
    datasourcelist = []
    datasourcename = []
    for datasource in (all_datasources):
        datasourcelist.append(datasource.id)
        datasourcename.append(datasource.name)
    print(datasourcelist)
    print("GET datasource 리스트 성공")
    # download workbook
    for j in range(0, len(datasourcelist)):
        server.datasources.download(datasourcelist[j], filepath=work_dir_data+"/"+datasourcename[j]+".tdsx")
    print("DOWN datasource 리스트 성공")

# 3) group

    f = open(work_dir_user+"/group.txt","wt")
    # get the groups on the server
    all_groups, pagination_item = server.groups.get()
    grouplist = []
    for group in (all_groups):
        grouplist.append(group.name)
        f.write(group.name)
        f.write("\n")
        f.close
    print(grouplist)
    # get user information
    for k in range(0,len(all_groups)):
        mygroup = all_groups[k]
        f2 = open(work_dir_user + "/user.txt", "wt")
        f2.write("그룹명;사용자;권한\n")
        pagination_item = server.groups.populate_users(mygroup)
        for user in mygroup.users :
            f2.write(mygroup.name)
            f2.write(";")
            f2.write(user.name)
            f2.write(";")
            f2.write(user.site_role)
            f2.write("\n")
            f2.close

# 4) schedule
    all_schedules, pagination_item = server.schedules.get()
    #print(all_schedules.name)
    f3 = open(work_dir_job+"/schedule.txt","wt")
    f3.write("schedule_type;schedule_name;created_at;next_run_at\n")
    for schedule in all_schedules :
        f3.write(schedule.schedule_type)
        f3.write(";")
        f3.write(schedule.name)
        f3.write(";")
        f3.write(str(schedule.created_at))
        f3.write(";")
        f3.write(str(schedule.next_run_at))
        f3.write("\n")

        f3.write("\n")
        f3.close
print(">>>>>>>>>>>>>>>백업완료<<<<<<<<<<<<<<<<<<<")
'''
# 5) job
with server.auth.sign_in(tableau_auth):
    print(server.jobs.get.id)s
'''







