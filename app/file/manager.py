# -*- coding: utf-8 -*-
import os
from os.path import join

'''
for root,dirs,files in os.walk('/Users/lixin/Downloads/'):
    for file in files:
        if file.endswith('.mp4'):
            print(os.path.join(root,file))
        i = i+1
'''

movie_list = {}
root = '/Users/lixin/Downloads/'
files=os.listdir(root)
for file in files:
    if file.endswith('.mp4') or file.endswith('.mkv'):
        head = file.split('.')[0]
        movies = None
        if head not in movie_list:
           movie_list[head] = []
        movies = movie_list[head] 
        movies.append(file)
#特殊处理
if 'A' in movie_list:
    movies = movie_list['A']
    movie = movies[0]
    new_movie = ".".join((movie.split('.')[4:]))
    old = os.path.join(root,movie)
    new = os.path.join(root,new_movie)
    #os.rename(old,new)

#处理合集
dst_root = '/Users/lixin/Downloads/Movies'
for key in movie_list:
    movies = movie_list[key]
    if len(movies) == 1:
        continue
    print(key)
    folder = os.path.join(dst_root,key)
    print(folder)
    if not os.path.exists(folder):
        os.makedirs(folder)
    for movie in movies:
        old = os.path.join(root,movie)
        new = os.path.join(folder,movie)
        os.rename(old,new)

#处理单片
for key in movie_list:
    movies = movie_list[key]
    if len(movies) == 1:
        for movie in movies:
            new_movie = "".join(movie.split('.')[:1])
            #创建新目录
            folder = os.path.join(dst_root, new_movie)
            if not os.path.exists(folder):
                print(folder)
                os.makedirs(folder)
            #稳动文件
            old = os.path.join(root,movie)
            new = os.path.join(folder,movie)
            os.rename(old,new)

import logging

#处理二级目录
def mv_file_level2():
    with os.scandir(root) as it:
        for e in it:
            if e.is_dir():
                for name in os.listdir(e.path):
                    if name.endswith('.mkv') or name.endswith('.mp4'):
                        new_name = ".".join(e.name.split('.')[:2])
                        new_path = os.path.join(dst_root,new_name)
                        if not os.path.exists(new_path):
                            os.makedirs(new_path)
                        name = ".".join(e.name.split('.')[:3])
                        new = os.path.join(new_path,name)
                        old = e.path
                        os.rename(old,new)
                        print(new)
                        print(old)
                        break
    

if __name__ == '__main__':
    mv_file_level2()
