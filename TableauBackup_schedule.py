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
tableau_auth = TSC.TableauAuth('admin', 'Planit0801!', site_id='')
work_dir_workbook = work_dir + "/workbook"
work_dir_data = work_dir +"/datasource"
work_dir_user = work_dir + "/user"
work_dir_job = work_dir + "/job"
make_folder(work_dir_workbook)
make_folder(work_dir_data)
make_folder(work_dir_user)
make_folder(work_dir_job)

#with server.auth.sign_in(tableau_auth):

# 4) schedule
with server.auth.sign_in(tableau_auth):
    all_schedules, pagination_item = server.schedules.get()
    # print(all_schedules.name)
    f3 = open(work_dir_job + "/schedule.txt", "wt")
    for schedule in all_schedules:
        print(schedule.schedule_type, schedule.name, schedule.priority, schedule.created_at, schedule.next_run_at, schedule.execution_order)

'''
# 5) job
with server.auth.sign_in(tableau_auth):
    print(server.jobs.get.id)s
'''







