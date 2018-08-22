#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ccinn (https://github.com/whiteCcinn)

import configparser
import os
from util.env import Env


class CommonConfig:

    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.path = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(self.path, 'config', Env.get_env("WORK_INI") + '.ini')

        self.cp.read(self.file_path, encoding='UTF-8')

    def echo(self):
        print(self.cp.get('common', 'test'))
