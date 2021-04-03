"""
Grade.py
=========================================
This module contains the enum Grae which is used by the predicting grades package.
"""
import enum

class Grade(enum.Enum):
    """
    This is a enumerator for the different possible grades.
    """

    _init_ = 'value __doc__'

    a = 6, "The top grade"
    b = 5, "The second highest grade"
    c = 4, "The third highest grade and the lowest possible pass"
    d = 3, "The fourth highest grade"
    e = 2, "The fith highest grade"
    f = 1, "The sixth highest grade and the lowest possible grade"
