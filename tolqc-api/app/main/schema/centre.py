# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcCentre

from .base import BaseSchema, BaseMeta


class CentreSchema(BaseSchema):
    class Meta(BaseMeta):
        model = TolqcCentre
        type_ = "centres"

#TODO see if this can be moved into __init__ safely
CentreSchema.setup()
