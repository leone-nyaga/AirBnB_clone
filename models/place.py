#!/usr/bin/python3
# AirBnB_clone

from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    desc = ""
    num_rooms = 0
    num_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
