# IfcOpenShell - IFC toolkit and geometry engine
# Copyright (C) 2021 Dion Moult <dion@thinkmoult.com>
#
# This file is part of IfcOpenShell.
#
# IfcOpenShell is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IfcOpenShell is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with IfcOpenShell.  If not, see <http://www.gnu.org/licenses/>.
import ifcopenshell
from typing import Any


def edit_person(file: ifcopenshell.file, person: ifcopenshell.entity_instance, attributes: dict[str, Any]) -> None:
    """Edits the attributes of an IfcPerson

    For more information about the attributes and data types of an
    IfcPerson, consult the IFC documentation.

    :param person: The IfcPerson entity you want to edit
    :type person: ifcopenshell.entity_instance
    :param attributes: a dictionary of attribute names and values.
    :type attributes: dict
    :return: None
    :rtype: None

    Example:

    .. code:: python

        person = ifcopenshell.api.run("owner.add_person", model,
            identification="bobthebuilder", family_name="Thebuilder", given_name="Bob")
        ifcopenshell.api.run("owner.edit_person", model, person=person,
            attributes={"MiddleNames": ["The"], "FamilyName": "Builder"})
    """
    settings = {"person": person, "attributes": attributes}

    for name, value in settings["attributes"].items():
        setattr(settings["person"], name, value)
