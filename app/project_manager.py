from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
import xlrd

import os
import logging
from datetime import date

from app import my_db
#from app.db import get_db

from app.common import parse_date

bp = Blueprint('project', __name__, url_prefix='/project')

#上传接口
@bp.route('/upload', methods=('GET', 'POST'))
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename

        # 存文件
        dst_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        # 解析入库
        project_name = '数仓'
        result = parse_file(project_name,dst_path)
        del_task_list(project_name)
        save_task_list(result)

        return dst_path
        #return str(dir(file))
    return render_template('project/upload.html')

# 解析文件
def parse_file(project_name,file_path):
    logging.info(file_path)
    data = xlrd.open_workbook(file_path)

    task_list = []

    table = data.sheets()[0] 
    for i in range(1,60):
    	project = project_name
    	desc = table.cell(i,1).value
    	owner = table.cell(i,7).value
    	begin = table.cell(i,4)
    	end = table.cell(i,5)
    	
    	begin = xlrd.xldate.xldate_as_datetime(int(begin.value), 0)
    	end = xlrd.xldate.xldate_as_datetime(int(end.value), 0)
    	
    	if str(owner) == "empty:''":
    	    continue
    	cell = {
    	        "project":project,
    	        "desc":desc,
    	        "owner":owner,
    	        "begin":begin,
    	        "end":end
    	}
    	task_list.append(cell)
    
    return  task_list 

class Task(my_db.Model):
    id = my_db.Column(my_db.Integer, primary_key=True)
    project = my_db.Column(my_db.String(80))
    desc = my_db.Column(my_db.String(240))
    owner = my_db.Column(my_db.String(240))
    begin = my_db.Column(my_db.DATE())
    end = my_db.Column(my_db.DATE())
    
    def __repr__(self):
        return 'Task project:%r, desc:%r, owner:%r, begin:%r, end:%r' % (self.project, 
            self.desc,
            self.owner,
            self.begin,
            self.end,
            )

# 数据入库
def save_task_list(task_list):
    for task in task_list:
        entity = Task()
        entity.project = task['project']
        entity.desc = task['desc']
        entity.owner = task['owner']
        entity.begin = task['begin']
        entity.end= task['end']
        logging.debug(entity)
        my_db.session.add(entity)
        my_db.session.commit()
    pass 

# 删除数据
def del_task_list(project):
    my_db.session.query(Task).filter(Task.project == project).delete()
    my_db.session.commit()



