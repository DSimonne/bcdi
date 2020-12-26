# -*- coding: utf-8 -*-

# BCDI: tools for pre(post)-processing Bragg coherent X-ray diffraction imaging data
#   (c) 07/2017-06/2019 : CNRS UMR 7344 IM2NP
#   (c) 07/2019-present : DESY PHOTON SCIENCE
#       authors:
#         Jerome Carnis, carnis_jerome@yahoo.fr

from numbers import Number, Real


def valid_container(obj, container_types, length=None, min_length=None, item_types=None, allow_none=False,
                    strictly_positive=False, name=None):
    """
    Check that the input object as three elements fulfilling the defined requirements.

    :param obj: the object to be tested
    :param container_types: list of the allowed types for obj
    :param length: required length
    :param min_length: mininum length (inclusive)
    :param item_types: list of the allowed types for the object items
    :param allow_none: True if the container items are allowed to be None
    :param strictly_positive: True is object values must all be strictly positive.
    :param name: name of the calling object appearing in exception messages
    """
    # check the validity of the requirements
    if container_types is None:
        raise ValueError('at least one type must be specified for the container')
    container_types = tuple(container_types)
    if not len(container_types):
        raise ValueError('at least one type must be specified for the container')
    if not all(isinstance(val, type) for val in container_types):
        raise TypeError('container_types should be a collection of valid types')

    if length is not None:
        if not isinstance(length, int) or length <= 0:
            raise ValueError('length should be a strictly positive integer')

    if min_length is not None:
        if not isinstance(min_length, int) or min_length < 0:
            raise ValueError('min_length should be a positive integer')

    if item_types is not None:
        item_types = tuple(item_types)
        if not all(isinstance(val, type) for val in item_types):
            raise TypeError('type_elements should be a collection of valid types')

    if not isinstance(allow_none, bool):
        raise TypeError('allow_none should be a boolean')

    if not isinstance(strictly_positive, bool):
        raise TypeError('strictly_positive should be a boolean')

    if allow_none and strictly_positive:
        raise TypeError("'>' not supported between instances of 'NoneType' and 'Number'")

    name = name or 'obj'

    # check the type of obj
    if not isinstance(obj, container_types):
        raise TypeError(f'type({name})={type(obj)}, allowed is {container_types}')

    # check the length of obj
    if length is not None:
        try:
            if len(obj) != length:
                raise ValueError(f'{name} should be of length {length}')
        except TypeError as ex:
            raise TypeError(f'method __len__ not defined for the type(s) {container_types}') from ex

    # check the min_length of obj
    if min_length is not None:
        try:
            if len(obj) < min_length:
                raise ValueError(f'{name}: the container should be of length >= {min_length}')
        except TypeError as ex:
            raise TypeError(f'method __len__ not defined for the type(s) {container_types}') from ex

    # check the presence of None in the items
    if not allow_none:
        if any(val is None for val in obj):
            raise ValueError(f'{name}: None is not allowed')

    # check the type of the items in obj
    if item_types is not None:
        for val in obj:
            if val is not None and not isinstance(val, item_types):
                raise TypeError(f'{name}: wrong type for items, allowed is {item_types} or None')

    # check the positivity of the items in obj
    if strictly_positive:
        if all(isinstance(val, Real) for val in obj) and not all(val > 0 for val in obj):
            raise ValueError(f'{name}: all items in the container should be strictly positive')


def valid_kwargs(kwargs, allowed_kwargs, name=None):
    """
    Check if the provided parameters belong to the set of allowed kwargs.

    :param kwargs: dictionnary of kwargs to check
    :param allowed_kwargs: set of allowed keys
    :param name: name of the calling object appearing in exception messages
    """
    # check the validity of the parameters
    if not isinstance(kwargs, dict):
        raise TypeError('kwargs should be a dictionnary')

    valid_container(obj=allowed_kwargs, container_types=(tuple, list, set), min_length=1, name='valid_kwargs')

    # check the kwargs
    for k in kwargs.keys():
        if k not in allowed_kwargs:
            raise Exception(f"{name}: unknown keyword argument given:", k)


def valid_number(value, allowed_types, min_included=None, min_excluded=None, max_included=None, max_excluded=None,
                 allow_none=False, name=None):
    """
    Check that the input object as three elements fulfilling the defined requirements.

    :param value: the value to be tested
    :param allowed_types: allowed types of the object values
    :param min_included: minimum allowed value (inclusive)
    :param min_excluded: minimum allowed value (exclusive)
    :param max_included: maximum allowed value (inclusive)
    :param max_excluded: maximum allowed value (exclusive)
    :param allow_none: True if the container items are allowed to be None
    :param name: name of the calling object appearing in exception messages
    """
    # check the validity of the requirements
    if allowed_types is None:
        raise ValueError('at least one allowed type must be specified for the value')
    allowed_types = tuple(allowed_types)
    if not len(allowed_types):
        raise ValueError('at least one allowed type must be specified for the value')
    if not all(isinstance(val, type) for val in allowed_types):
        raise TypeError('allowed_types should be a collection of valid types')

    if min_included is not None:
        if not isinstance(min_included, Real):
            raise ValueError('min_included should be a real number')

    if min_excluded is not None:
        if not isinstance(min_excluded, Real):
            raise ValueError('min_excluded should be a real number')

    if max_included is not None:
        if not isinstance(max_included, Real):
            raise ValueError('max_included should be a real number')

    if max_excluded is not None:
        if not isinstance(max_excluded, Real):
            raise ValueError('max_excluded should be a real number')

    if not isinstance(allow_none, bool):
        raise TypeError('allow_none should be a boolean')

    name = name or 'obj'

    # check if value is None
    if not allow_none and value is None:
        raise ValueError(f'{name}: None is not allowed')

    # check the type of obj
    if value is not None and not isinstance(value, allowed_types):
        raise TypeError(f'{name}: wrong type for value, allowed is {allowed_types}')

    # check min_included
    if min_included is not None:
        if value < min_included:
            raise ValueError(f'{name}: value should be larger or equal to {min_included}')

    # check min_excluded
    if min_excluded is not None:
        if value <= min_excluded:
            raise ValueError(f'{name}: value should be strictly larger than {min_excluded}')

    # check max_included
    if max_included is not None:
        if value > max_included:
            raise ValueError(f'{name}: value should be smaller or equal to {max_included}')

    # check max_excluded
    if max_excluded is not None:
        if value >= max_excluded:
            raise ValueError(f'{name}: value should be strictly smaller than {max_excluded}')