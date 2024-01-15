import maya.cmds as cmds

def snapObjects():
    """A tool to snap object A to the position and rotation of object B.
    Useful in situations of getting a prop into character's hand, etc.

    Returns:
        Selection of object A
    """

    user_clicks = cmds.ls(selection=True)

    if len(user_clicks) == 2:
        #Snapping position and rotation of object A to object B with parent constraint connection
        cmds.parentConstraint(user_clicks[1],user_clicks[0])
        #Removes the constraint's connection while maintaining new position
        cmds.delete(user_clicks[0], cn=True)
    elif len(user_clicks) > 2:
        print("Only select parent and child object to snap.")
    else:
        print("Select minimum 2 object to snap.")

    return user_clicks[0]

snapObjects()