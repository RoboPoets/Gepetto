# type: ignore

import os
import bpy
import bpy_extras

from ..core import custom_schemes_manager


class SaveCustomBonesRetargeting(bpy.types.Operator):
    bl_idname = "rsl.save_custom_bones_retargeting"
    bl_label = "Save Custom Bones"
    bl_description = "This saves the currently selected bones and they will then get automatically detected"
    bl_options = {"INTERNAL"}

    def execute(self, context):
        # Save the bone list if the user changed anything
        custom_schemes_manager.save_retargeting_to_list()

        return {"FINISHED"}


class ImportCustomBones(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    bl_idname = "rsl.import_custom_schemes"
    bl_label = "Import Custom Scheme"
    bl_description = "Import a custom naming scheme"
    bl_options = {"REGISTER", "UNDO", "INTERNAL"}

    files: bpy.props.CollectionProperty(
        type=bpy.types.OperatorFileListElement, options={"HIDDEN", "SKIP_SAVE"}
    )
    directory: bpy.props.StringProperty(
        maxlen=1024, subtype="FILE_PATH", options={"HIDDEN", "SKIP_SAVE"}
    )
    filter_glob: bpy.props.StringProperty(default="*.json;", options={"HIDDEN"})

    def execute(self, context):
        import_count = 0
        if self.directory:
            for f in self.files:
                file_name = f.name
                if not file_name.endswith(".json"):
                    continue
                custom_schemes_manager.import_custom_list(self.directory, file_name)
                import_count += 1

        # If this operator is called with no directory but a filepath argument, import that
        elif self.filepath:
            custom_schemes_manager.import_custom_list(
                os.path.dirname(self.filepath), os.path.basename(self.filepath)
            )
            import_count += 1

        custom_schemes_manager.save_to_file_and_update()

        if not import_count:
            self.report({"ERROR"}, "No files were imported.")
            return {"FINISHED"}

        self.report({"INFO"}, "Successfully imported new naming schemes.")
        return {"FINISHED"}


class ExportCustomBones(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    bl_idname = "rsl.export_custom_schemes"
    bl_label = "Export Custom Scheme"
    bl_description = "Export your custom naming schemes"
    bl_options = {"REGISTER", "UNDO", "INTERNAL"}

    filename_ext = ".json"
    filter_glob: bpy.props.StringProperty(default="*.json;", options={"HIDDEN"})

    def execute(self, context):
        file_name = custom_schemes_manager.export_custom_list(self.filepath)

        if not file_name:
            self.report({"ERROR"}, "You don't have any custom naming schemes!")
            return {"FINISHED"}

        self.report({"INFO"}, 'Exported custom naming schemes as "' + file_name + '".')
        return {"FINISHED"}


class ClearCustomBones(bpy.types.Operator):
    bl_idname = "rsl.clear_custom_bones"
    bl_label = "Clear Custom Bones"
    bl_description = "Clear all custom bone naming schemes"
    bl_options = {"INTERNAL"}

    def draw(self, context):
        layout = self.layout

        layout.separator()

        row = layout.row(align=True)
        row.scale_y = 0.5
        row.label(
            text="You are about to delete all stored custom bone naming schemes.",
            icon="ERROR",
        )

        row = layout.row(align=True)
        row.scale_y = 0.5
        row.label(text="Continue?", icon="BLANK1")

        layout.separator()

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)

    def execute(self, context):
        custom_schemes_manager.delete_custom_bone_list()

        self.report({"INFO"}, "Cleared all custom bone naming schemes!")
        return {"FINISHED"}
