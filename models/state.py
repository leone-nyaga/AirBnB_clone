#!/usr/bin/python3
# AirBnB_clone

""" state class """
from models.base_model import BaseModel


class State(BaseModel):
    name = ""


    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
