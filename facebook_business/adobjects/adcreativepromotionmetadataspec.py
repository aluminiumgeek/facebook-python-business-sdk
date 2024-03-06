# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCreativePromotionMetadataSpec(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCreativePromotionMetadataSpec = True
        super(AdCreativePromotionMetadataSpec, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        end_date = 'end_date'
        id = 'id'
        promotion_source = 'promotion_source'
        promotion_type = 'promotion_type'
        promotion_value = 'promotion_value'
        required_code = 'required_code'
        start_date = 'start_date'

    _field_types = {
        'end_date': 'datetime',
        'id': 'string',
        'promotion_source': 'string',
        'promotion_type': 'string',
        'promotion_value': 'float',
        'required_code': 'string',
        'start_date': 'datetime',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


