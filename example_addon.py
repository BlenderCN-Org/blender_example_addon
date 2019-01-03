# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>

bl_info = {
    "name": "Example Addon", # Addon name
    "author": "Andrew Palmer", # Author name(s)
    "version": (0, 1, 0), # Addon version
    "blender": (2, 80, 0), # Blender version
    "location": "Properties panel > Example Addon", # Where the addon is located
    "description": "An example addon",  # Brief description of the addon
    "warning": "", # Warning for users
    "wiki_url": "", # URL for documentation
    "tracker_url": "", # URL for bug reports"
    "category": "Mesh", # Category of the addon (e.g. Mesh, Curve, Paint, etc.)
}


import bpy
from bpy.types import (
    Operator,
    Panel,
)
from bpy.props import (
    IntProperty,
)


class EXAMPLE_OT_ExampleOperator(Operator):
    """Tooltip"""
    bl_idname = "example.example_operator"
    bl_label = "Example Operator"
    bl_description = "Doesn't do anything. Example code"
    bl_options = {'REGISTER', 'UNDO'}

    example_property: IntProperty(
        name="Example Property",
        description="Integer property",
        default=1,
        min=0,
        max=10,
    )

    def execute(self, context):
        print("Example Operator: {0}", self.example_property)

        return {'FINISHED'}


class EXAMPLE_PT_ExampleAddon(Panel):
    """Example addon as a quick starting point for new addons"""
    bl_label = "Example Addon"
    bl_idname = "EXAMPLE_PT_ExampleOperator"
    bl_space_type ="VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        row = col.row()
        row.label(text="Example Addon Operator")
        row = col.row()
        row.operator("example.example_operator", text="Click Me")


classes = (
    EXAMPLE_PT_ExampleAddon,
    EXAMPLE_OT_ExampleOperator,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()