<h1>Geppetto Plugin for Blender</h1>

**Geppetto** is a Blender plugin for retargeting animations and streamlining animation workflows.

## Requirements
- Blender **3.6** or higher

## Features
- Easily retarget motion capture animations
- Retarget from and to skeletons with different rest poses

## Retargeting
In order to retarget an animation in Blender you will need to do the following:

- Open the Retargeting panel
- Select an armature with an animation as the source armature, select an armature that should receive the animation as the target armature and then press "Build Bone List"
- Check if the bones got filled in correctly and fix any incorrect or missing bones
- Select "Auto Scale" if the armatures differ in size or resize them manually
- In "Use Pose:" select the pose that should be used for retargeting
- Important: Make sure that both armature are in the same pose for correct retargeting
- Press "Retarget Animation"
- Done!
