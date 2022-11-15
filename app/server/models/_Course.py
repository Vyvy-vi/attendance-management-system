from mongoengine import Document
from mongoengine.fields import *
from datetime import datetime
from enum import Enum


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class Class(Document):
    class_code = IntField()
    class_time = DateTimeField()
    class_day = Day


class Course(Document):
    course_code = IntField()
    course_name = StringField()
    course_classes = EmbeddedDocumentListField(Class)
    course_teacher = StringField()
    student_strength = LongField()
    course_sections = ListField(StringField(), default=None)
