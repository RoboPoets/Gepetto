# Initializes the Geppetto panel in the toolbar
class ToolPanel(object):
    bl_label = "Geppetto"
    bl_idname = "VIEW3D_TS_geppetto"
    bl_category = "Geppetto"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


# Adds a small separator
def separator(layout, scale=1):
    row = layout.row(align=True)
    row.scale_y = scale
    row.label(text="")
