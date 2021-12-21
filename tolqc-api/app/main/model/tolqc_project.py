# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import SubBase, db


class TolqcProject(SubBase):
    __tablename__ = "project"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    accession_id = db.Column(db.Integer())
    allocation = db.relationship("TolqcAllocation", back_populates="project")
