#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ccinn (https://github.com/whiteCcinn)

import os


class Env:
    LOADED = False

    __CONFIG_KEYS = (
        'AUTHOR',
        'GITHUB',
        'WORK_INI'
    )

    CONFIG = {}

    def __init__(self):
        pass

    @staticmethod
    def get_env(variable):
        if Env.LOADED:
            if variable in Env.CONFIG.keys():
                return Env.CONFIG[variable]
            else:
                return None
        else:
            Env.__init()
            return Env.get_env(variable)

    @classmethod
    def __init(cls):
        for key in Env.__CONFIG_KEYS:
            Env.CONFIG[key] = os.environ[key]
        cls.LOADED = True

    @staticmethod
    def get_env_all():
        if Env.LOADED:
            return Env.CONFIG
        else:
            Env.__init()
            return Env.get_env_all()
