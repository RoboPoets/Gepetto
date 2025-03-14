# type: ignore

from bpy.types import Scene, Object, PropertyGroup
from bpy.props import (
    IntProperty,
    StringProperty,
    EnumProperty,
    BoolProperty,
    FloatProperty,
    CollectionProperty,
    PointerProperty,
)

from .core import animation_lists, state_manager, recorder, retargeting


class BoneListItem(PropertyGroup):
    """Properties of the bone list items"""

    bone_name_source: StringProperty(
        name="Source Bone", description="The source bone name", default=""
    )

    bone_name_target: StringProperty(
        name="Target Bone", description="The target bone name", default=""
    )

    bone_name_key: StringProperty(
        name="Auto Detection Key",
        description="The automatically detected bone key",
        default="",
    )

    is_custom: BoolProperty(
        description="This determines if the field is a custom one source bone one",
        default=False,
    )


def register():
    # Receiver

    Scene.rsl_reset_scene_on_stop = BoolProperty(
        name="Reset Scene on Stop",
        description="This will reset the location and position of animated objects to the state of before starting the receiver",
        default=True,
    )
    Scene.rsl_recording = BoolProperty(
        name="Toggle Recording",
        description="Start and stop recording of the data from Rokoko Studio",
        default=False,
        update=recorder.toggle_recording,
    )

    # Retargeting
    Scene.rsl_retargeting_armature_source = PointerProperty(
        name="Source",
        description="Select the armature with the animation that you want to retarget",
        type=Object,
        poll=retargeting.poll_source_armatures,
        update=retargeting.clear_bone_list,
    )
    Scene.rsl_retargeting_armature_target = PointerProperty(
        name="Target",
        description="Select the armature that should receive the animation",
        type=Object,
        poll=retargeting.poll_target_armatures,
        update=retargeting.clear_bone_list,
    )
    Scene.rsl_retargeting_auto_scaling = BoolProperty(
        name="Auto Scale",
        description="This will scale the source armature to fit the height of the target armature."
        "\nBoth armatures have to be in T-pose for this to work correctly",
        default=True,
    )
    Scene.rsl_retargeting_use_pose = EnumProperty(
        name="Use Pose",
        description="Select which pose of the source and target armature to use to retarget the animation."
        "\nBoth armatures should be in the same pose before retargeting",
        items=[
            ("REST", "Rest", "Select this to use the rest pose during retargeting."),
            (
                "CURRENT",
                "Current",
                "Select this to use the current pose during retargeting.",
            ),
        ],
    )
    Scene.rsl_retargeting_bone_list = CollectionProperty(type=BoneListItem)
    Scene.rsl_retargeting_bone_list_index = IntProperty(
        name="Index for the retargeting bone list", default=0
    )

    # Objects
    Object.rsl_use_custom_scale = BoolProperty(
        name="Use Custom Scale",
        description="Select this if the objects scene scaling should be overwritten",
        default=False,
    )
    Object.rsl_custom_scene_scale = FloatProperty(
        name="Custom Scene Scaling",
        description="This allows you to scale the position independently from the scene scale.",
        default=1,
        precision=3,
        step=1,
    )

    # Face shapekeys
    for shape in animation_lists.face_shapes:
        setattr(
            Object,
            "rsl_face_" + shape,
            StringProperty(
                name=shape,
                description="Select the shapekey that should be animated by this shape",
            ),
        )

    # Actor bones
    for bone in animation_lists.get_bones().keys():
        setattr(
            Object,
            "rsl_actor_" + bone,
            StringProperty(
                name=bone,
                description="Select the bone that corresponds to the actors bone",
            ),
        )
