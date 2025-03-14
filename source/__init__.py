# Important plugin info for Blender
bl_info = {
    "name": "Geppetto",
    "author": "Robo Poets & Rokoko Electronics ApS",
    "category": "Animation",
    "location": "View 3D > Tool Shelf > Geppetto",
    "description": "A set of tools for animation authoring and retargeting",
    "version": (1, 5, 0),
    "blender": (4, 0, 0),
    "wiki_url": "https://github.com/RoboPoets/rokoko-studio-live-blender#readme",
}

from . import core
from . import panels
from . import operators
from . import properties

import bpy


classes = [
    panels.objects.ObjectsPanel,
    panels.command_api.CommandPanel,
    panels.retargeting.RetargetingPanel,
    panels.info.InfoPanel,
    operators.recorder.RecorderStart,
    operators.recorder.RecorderStop,
    operators.detector.DetectFaceShapes,
    operators.detector.DetectActorBones,
    operators.detector.SaveCustomShapes,
    operators.detector.SaveCustomBones,
    operators.detector.SaveCustomBonesRetargeting,
    operators.detector.ImportCustomBones,
    operators.detector.ExportCustomBones,
    operators.detector.ClearCustomBones,
    operators.detector.ClearCustomShapes,
    operators.actor.InitTPose,
    operators.actor.ResetTPose,
    operators.actor.PrintCurrentPose,
    operators.command_api.CommandTest,
    operators.command_api.StartCalibration,
    operators.command_api.Restart,
    operators.command_api.StartRecording,
    operators.command_api.StopRecording,
    operators.retargeting.BuildBoneList,
    operators.retargeting.AddBoneListItem,
    operators.retargeting.ClearBoneList,
    operators.retargeting.RetargetAnimation,
    panels.retargeting.RSL_UL_BoneList,
    panels.retargeting.BoneListItem,
    operators.info.LicenseButton,
    operators.info.DocumentationButton,
]


def register():
    register_count = 0

    for cls in classes:
        try:
            bpy.utils.register_class(cls)
            register_count += 1
        except ValueError:
            print("Error: Failed to register class", cls)

    if register_count < len(classes):
        print("Skipped", len(classes) - register_count, " classes.")

    properties.register()
    core.icon_manager.load_icons()

    # Load bone detection list
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
