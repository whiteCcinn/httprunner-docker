#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ccinn (https://github.com/whiteCcinn)

from util.env import Env
from parameters.common import Common
from parameters.header import Header
from util.validation_json_schema import Validation

header = Header()
common = Common()


# common function

def get_base_url():
    return common.get_base_url()


# header function
def get_host():
    return header.get_host()


def get_connection():
    return header.get_connection()


def get_pragma():
    return header.get_pragma()


def get_cache_control():
    return header.get_cache_control()


def get_user_agent():
    return header.get_user_agent()


def get_upgrade_insecure_requests():
    return header.get_upgrade_insecure_requests()


def get_accept():
    return header.get_accept()


def get_accept_encoding():
    return header.get_accept_encoding()


def get_accept_language():
    return header.get_accept_language()


# env function

def get_env(variable):
    return Env.get_env(variable)


# hooks function

def hook_prepare(request):
    pass


def hook_teardown(case_name, response, schema):
    Validation(case_name, response, schema).validate()

#  custom function
# def your function
