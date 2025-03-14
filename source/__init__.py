bl_info = {
    "name": "Geppetto",
    "author": "Robo Poets & Rokoko Electronics ApS",
    "category": "Animation",
    "location": "View 3D > Tool Shelf > Geppetto",
    "description": "A set of tools for animation authoring and retargeting",
    "version": (1, 5, 0),
    "blender": (3, 6, 0),
    "wiki_url": "https://github.com/RoboPoets/Geppetto#readme",
}

from . import core
from . import panels
from . import operators
from . import properties

import bpy


classes = [
    operators.detector.SaveCustomBonesRetargeting,
    operators.detector.ImportCustomBones,
    operators.detector.ExportCustomBones,
    operators.detector.ClearCustomBones,
    operators.retargeting.BuildBoneList,
    operators.retargeting.AddBoneListItem,
    operators.retargeting.ClearBoneList,
    operators.retargeting.RetargetAnimation,
    operators.info.LicenseButton,
    operators.info.DocumentationButton,
    panels.retargeting.RSL_UL_BoneList,
    panels.retargeting.RetargetingPanel,
    panels.info.InfoPanel,
    properties.BoneListItem,
]


def register():
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError:
            print("Error: Failed to register class", cls)

    properties.register()
    core.icon_manager.load_icons()
    core.detection_manager.load_detection_lists()


def unregister():
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

    core.icon_manager.unload_icons()


if __name__ == "__main__":
    register()
