# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcCentre(Base):
    __tablename__ = "centre"
    #centre_id = db.Column(db.Integer(), primary_key=True)
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    run = db.relationship("TolqcRun", back_populates="centre")
