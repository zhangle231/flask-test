import pytest
import logging

from app.project_manager import (
    parse_file,save_task_list,del_task_list
)

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

def test_parse_file(app):
    with app.app_context():
        project_name = '数仓'
        file_path = 'tests/数仓详细工作计划-含交换平台-2020-04-28.xlsx'
        result = parse_file(project_name,file_path)

def test_save_task_list(app):
    with app.app_context():
        project_name = '数仓'
        file_path = 'tests/数仓详细工作计划-含交换平台-2020-04-28.xlsx'
        result = parse_file(project_name,file_path)
        del_task_list(project_name)
        save_task_list(result)
