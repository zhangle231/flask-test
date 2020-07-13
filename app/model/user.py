from app import my_db

class User(my_db.Model):
    '''
    用户编号  用户名称 用户昵称 部门 手机号码 状态 创建时间 操作
    用户编号  用户名称 部门 手机号码 状态 创建时间 操作
    '''
    id = my_db.Column(my_db.Integer, primary_key=True)
    username = my_db.Column(my_db.String(50))
    password = my_db.Column(my_db.String(50))
    dep = my_db.Column(my_db.String(50))
    phone = my_db.Column(my_db.String(20))
    mail = my_db.Column(my_db.String(50))
    status = my_db.Column(my_db.Integer)
    post = my_db.Column(my_db.String(50))
    remarks = my_db.Column(my_db.String(100))
    create_time = my_db.Column(my_db.DateTime())


    def __repr__(self):
        return 'User id:%r, username:%r, password:%r, dep:%r, phone:%r, mail:%r, status:%r, post:%r, remarks:%r, create_time:%r' % (self.id, self.username, self.password, self.dep, self.phone, self.mail, self.status, self.post, self.remarks, self.create_time)



