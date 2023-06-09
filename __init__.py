#TODO
# optimize simplify functions


'''
Copyright (C) 2018 Samy Tichadou (tonton)
samytichadou@gmail.com

Created by Samy Tichadou

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "CSimplify",
    "description": "Custom Simplify Operator",
    "author": "Samy Tichadou (tonton)",
    "version": (1, 0, 2),
    "blender": (3, 0, 0),
    "location": "3D Viewport and Render/Object Properties",
    "wiki_url": "https://github.com/samytichadou/CSimplify/blob/master/README.md",
    "tracker_url": "https://github.com/samytichadou/CSimplify/issues/new",
    "category": "Render" }

# IMPORT SPECIFICS
##################################

from . import (
    preferences,
    properties,
    gui,
    fix_simplify_operator,
)

# register
##################################

def register():
    preferences.register()
    properties.register()
    gui.register()
    fix_simplify_operator.register()

def unregister():
    preferences.unregister()
    properties.unregister()
    gui.unregister()
    fix_simplify_operator.unregister()
