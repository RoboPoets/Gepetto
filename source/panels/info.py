import bpy

from .main import ToolPanel, separator
from ..operators import info
from ..core.icon_manager import Icons


class InfoPanel(ToolPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_rsl_info_v2"
    bl_label = "Info"

    def draw(self, context):
        layout = self.layout

        layout.row(align=True).label(text="Geppetto v1.5.0")
        layout.row(align=True).label(text="© 2025 Robo Poets UG")

        separator(layout, 0.1)

        row = layout.row(align=True)
        row.operator(info.LicenseButton.bl_idname)
        row.operator(info.DocumentationButton.bl_idname)
