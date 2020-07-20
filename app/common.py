import time
import datetime


def parse_date(date_str):
    fmt = '%Y-%m-%d'
    time_tuple = time.strptime(date_str, fmt)
    year, month, day = time_tuple[:3]
    new_date = datetime.date(year, month, day)
    return new_date


def reuse(pid, l, r):
    '''生成菜单树
    '''
    l = [e for e in l if e not in r]
    if len(l) == 0:
        return r
    for e in l:
        if e.pid == pid:
            r.append(e)
            r = reuse(e.id, l, r)
    return r


def get_menu(menus):
    '''获取菜单树,菜单管理使用
    '''
    r = []
    res = reuse(0, menus, r)
    return res


def create_tree(pid, data, ret):
    '''生成用于侧边栏折叠的树型结构
    '''
    for d in data:
        c_id = d.id
        c_pid = d.pid
        if pid == c_pid:
            r = {'id': c_id, 'pid': c_pid, 'is_leaf': 1,
                 'name': d.name, 'url': d.url, 'children': []}
            ret['children'].append(r)
            ret['is_leaf'] = 0
            create_tree(c_id, data, r)
