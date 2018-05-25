# https://stackoverflow.com/questions/8609192/differentiate-null-true-blank-true-in-django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

from ..users.models import User


# Create your models here.
class Tag(models.Model):
    """
    表示 Deadline 对应的类型
    依赖Deadline
    """
    # tag 对应的标识, 是TAG的主键，依赖Deadline
    tag_name = models.CharField(max_length=30, primary_key=True, null=False)

    def __str__(self):
        return f"Tag({self.tag_name})"


class LargeDeadline(models.Model):
    """
    Deadline 的小组
    """
    group_name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)


class Deadline(models.Model):
    """
    表示deadline的类
    创建时间、USER是直接绑定的

    """
    # 表示对应用户的字段
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # tag 表示对应的Deadline类型, 希望能被INDEX索引
    tags = models.ManyToManyField(Tag, blank=True)
    # 被创建的时间, 默认调用now
    created_time = models.DateTimeField(default=datetime.datetime.now, editable=False)
    # Deadline 结束的时间，不可以被设置为FALSE
    ending_time = models.DateTimeField(null=False)
    # 邮件订阅，对应的发送邮件 等
    email_subscribe = models.BooleanField(default=False, blank=True)
    # deadline 的小组，包含多个连续deadline 项目, 删除小组是设置成NULL.
    ddl_group = models.ForeignKey(LargeDeadline, null=True, db_index=True, on_delete=models.SET_NULL, blank=True)
    # ddl description
    description = models.TextField(null=True, blank=False)


class Course(models.Model):
    """
    课程对应的信息
    有多个课程评论
    """
    # 课程名称
    course_name = models.CharField(max_length=40, primary_key=True, null=False)
    # 老师名称
    teacher_name = models.CharField(max_length=25, db_index=True)


class CourseComment(models.Model):

    """
    课程的评论
    """
    # 最大、最小的评分
    GRADE_UPPER, GRADE_LOWER = 5, 1
    # 对应的课程
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # 对应的评分(5 分制度)
    grade = models.IntegerField(null=True, validators=[MaxValueValidator(GRADE_UPPER), MinValueValidator(GRADE_LOWER)])
    # comment_text = models.TextField(max_length=150, null=True)


