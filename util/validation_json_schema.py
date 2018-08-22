#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ccinn (https://github.com/whiteCcinn)

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from util.function import *
import os
import json
import traceback


class Validation:

    def __init__(self, case_name, response, schema):
        self.case_name = case_name
        self.response = response
        self.schema = schema
        self.path = ''

    def get_schema_file(self):
        self.path = os.path.dirname(os.path.dirname(__file__))
        self.path = os.path.join(self.path, 'jsonschemas', self.case_name, self.schema + '.schema.json')
        return self.path

    def validate(self):
        schema = json.loads(read_file(self.get_schema_file()))
        content = self.response.content.decode(encoding="utf-8")
        content = json.loads(content)
        self.response.jsonschema_error = ''
        try:
            validate(content, schema)
        except ValidationError:
            self.response.jsonschema_error = traceback.format_exc()
