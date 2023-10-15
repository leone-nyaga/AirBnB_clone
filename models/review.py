#!/usr/bin/python3
# AirBnB_clone

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        args
        name : string review email
        """

        super().__init__(*args, **kwargs)
