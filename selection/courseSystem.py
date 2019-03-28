# -*- coding: utf-8 -*-
import pickle
import os


student_info = "student_info"
course_info = 'course_info'
school_info = "school_info"
teacher_info = "teacher_info"
userinfo= 'userinfo'


class Person:

    def show_courses(self):
        # 查看所有课程
        # with open(course_info, 'rb') as f:
        #     count = 0
        #     while True:
        #         try:
        #             count += 1
        #             course_obj = pickle.load(f)
        #             print(count, course_obj.name, course_obj.price, course_obj.period, course_obj.teacher)
        #         except EOFError:
        #             break
        for count, course in enumerate(self.get_from_pickle(course_info), 1):
            print(count, repr(course))

    # @staticmethod
    # def get_student():
    #     with open(student_info, 'rb') as f:
    #         while True:
    #             try:
    #                 stu_obj = pickle.load(f)
    #                 yield stu_obj
    #             except EOFError:
    #                 break
    #
    # @staticmethod
    # def get_course():
    #     with open(course_info, 'rb') as f:
    #         while True:
    #             try:
    #                 stu_obj = pickle.load(f)
    #                 yield stu_obj
    #             except EOFError:
    #                 break

    @staticmethod
    def get_from_pickle(path):
        with open(path, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except EOFError:
                    break


class School:
    # 学校类
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return '学校名称：%s，地址：%s' % (self.name, self.address)


class Teacher(Person):
    # 老师类
    operate_lst = [
        ('查看所有课程', 'show_courses'),
        ('退出', 'exit')]

    def __init__(self, name, course, school):
        self.name = name
        self.course = course
        self.school = school

    def __repr__(self):
        return '%s|%s|%s' % (self.name, self.course, self.school)

    @classmethod
    def init(cls, name):
        for stu in cls.get_from_pickle(teacher_info):
            if stu.name == name:
                return stu
        else:
            print("没有这个老师信息")

    def exit(self):
        exit()


class Course:
    # 课程类
    def __init__(self, name, price, period, teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

    def __str__(self):
        return self.name

    def __repr__(self):
        return ' '.join([self.name, self.price, self.period, self.teacher])


class Student(Person):
    """
    学生类
    """
    operate_lst = [
        ('查看所有课程', 'show_courses'),
        ('选择课程', 'select_course'),
        ('查看已选课程', 'check_selected_course'),
        ('退出', 'exit')]

    def __init__(self, name):
        self.name = name
        self.courses = []

    def __repr__(self):
        course_name = [course.name for course in self.courses]
        return '%s %s' % (self.name, '所选课程：%s' % '|'.join(course_name))

    def __str__(self):
        return self.name

    def select_course(self):
        # 选择课程
        self.show_courses()
        num = int(input('请输入选择课程的编号：'))
        for count, course in enumerate(self.get_from_pickle(course_info), 1):
            if count == num:
                self.courses.append(course)
                print('您选择了%s课程' % course)
                break
        else:
            print('没有您要找的课程')

        # count = 1
        # with open(course_info, 'rb') as f:
        #     while True:
        #         try:
        #             course_obj = pickle.load(f)
        #             if count == num:
        #                 self.courses.append(course_obj)
        #                 print('您选择了%s课程' % (course_obj.name))
        #                 break
        #             count += 1
        #         except EOFError:
        #             print('没有您选择的课程')
        #             break

    def check_selected_course(self):
        # 已经选的课程
        for index, course in enumerate(self.courses, 1):
            print(index, course.name, course.teacher)

    def exit(self):
        print('退出系统！')
        with open(student_info + '_bak', 'wb') as f:
            for stu in self.get_from_pickle(student_info):
                if stu.name == self.name:
                    pickle.dump(self, f)
                else:
                    pickle.dump(stu, f)
        # with open(student_info, 'rb') as f1, open('student_info_bak', 'wb') as f2:
        #     while True:
        #         try:
        #             student_obj = pickle.load(f1)
        #             if student_obj.name == self.name:
        #                 '''
        #                 如果从原文件找到了学生对象和我当前的对象是一个名字，就认为是一个人
        #                 应该把现在新的学生对象写到文件中
        #                 反之，应该原封不动的把学生对象写回f2
        #                 '''
        #                 pickle.dump(self, f2)
        #             else:
        #                 pickle.dump(student_obj, f2)
        #         except EOFError:
        #             break
        os.remove(student_info)
        os.rename(student_info + "_bak", student_info)
        exit()

    @classmethod
    def init(cls, name):
        for stu in cls.get_from_pickle(student_info):
            if stu.name == name:
                return stu
        else:
            print("没有这个学生")


class Manager(Person):
    """
    超级管理员类
    """
    operate_lst = [('创建课程', 'create_course'),
                   ('创建学生', 'create_student'),
                   ('创建学校', 'create_school'),
                   ('创建老师', 'create_teacher'),
                   ('查看所有课程', 'show_courses'),
                   ('查看所有学生', 'show_students'),
                   ('查看所有学校', 'show_school'),
                   ('查看所有老师情况', 'show_teacher'),
                   ('查看所有学生的选课情况', 'show_student_course'),
                   ('退出', 'exit')]

    def __init__(self, name):
        self.name = name

    def create_course(self):
        # 创建课程
        name = input("课程的名称：")
        price = input("课程的价格：")
        period = input("课程的周期：")
        teacher = input("课程的老师：")
        course_obj = Course(name, price, period, teacher)
        with open(course_info, 'ab') as f:
            pickle.dump(course_obj, f)
        print("%s课程创建成功" % name)

    def create_student(self):
        # 创建学生
        # 用户密码记录到userinfo文件，将学生对象存储在student_info文件中
        stu_name = input("学生姓名：").strip()
        stu_pwd = input("学生密码：").strip()
        stu_auth = '%s|%s|Student\n' % (stu_name, stu_pwd)
        stu_obj = Student(stu_name)
        with open(userinfo, 'a', encoding='utf-8') as f:
            f.write(stu_auth)
        with open(student_info, 'ab') as f:
            pickle.dump(stu_obj, f)
        print("%s学生，创建成功" % stu_name)

    def create_school(self):
        # 创建学校
        name = input("学校名称：")
        address = input("学校地址：")
        school_obj = School(name, address)
        with open(school_info, 'ab') as f:
            pickle.dump(school_obj, f)
        print("%s学校创建成功" % name)

    def create_teacher(self):
        # 创建老师
        name = input("老师姓名：").strip()
        pwd = input("老师密码：").strip()
        course = input("老师教的课程：").strip()
        school = input("老师的学校：").strip()
        auth = '%s|%s|Teacher\n' % (name, pwd)
        obj = Teacher(name, course, school)
        with open(userinfo, 'a', encoding='utf-8') as f:
            f.write(auth)
        with open(teacher_info, 'ab') as f:
            pickle.dump(obj, f)
        print("%s老师，创建成功" % name)

    def show_students(self):
        # 查看所有的学生
        for count, stu in enumerate(self.get_from_pickle(student_info), 1):
            print(count, stu.name)
        # with open(student_info, 'rb') as f:
        #     count = 0
        #     while True:
        #         try:
        #             count += 1
        #             student_obj = pickle.load(f)
        #             print(count, student_obj.name)
        #         except EOFError:
        #             break

    def show_student_course(self):
        # 查看所有学生的选课情况
        for stu in self.get_from_pickle(student_info):
            print(repr(stu))

        # with open(student_info, 'rb') as f:
        #     while True:
        #         try:
        #             student_obj = pickle.load(f)
        #             course_name = [course.name for course in student_obj.courses]
        #             print(student_obj.name, '所选课程：%s' % '|'.join(course_name))
        #         except EOFError:
        #             break

    def show_school(self):
        # 查看所有学校
        for x in self.get_from_pickle(school_info):
            print(repr(x))

    def show_teacher(self):
        # 查看所有老师情况
        for x in self.get_from_pickle(teacher_info):
            print(repr(x))

    def exit(self):
        print('退出系统！')
        exit()

    @classmethod
    def init(cls, name):
        return cls(name)


def login():
    username = input("username:")
    password = input("password:")
    with open(userinfo, encoding='utf-8') as f:
        for line in f:
            user, pwd, identify = line.strip().split("|")
            if user == username and pwd == password:
                return {"result": True, "name": username, "id": identify}
        else:
            return {"result": False, "name": username}

