"""
Helper function to serialize MongoDb data
"""


def serialize_dict(dict_object):
    return {str(k): str(v) for k, v in dict_object.items()}
