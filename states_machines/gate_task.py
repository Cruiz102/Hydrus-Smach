# TODO: Create a gate task state machine
class start(smach.state):
    def __init__(self):
        smach.state.__init__(self, outcomes=['gate_found', 'no_gate_found'])

    def execute(self, userdata):
        rospy.loginfo('Executing state start')
        if (deph < 1.5):
            return "Lower Deph"
        else:
            return "Stop"


class Lower_Depth(smach.state):
    def __init__(self):
        smach.state.__init__(self, outcomes=['identify_gate'])

    def execute(self, userdata):
        moveit.pose.z = 10
        rospy.loginfo('Executing state Lower_Depth')
        return "identify_gate"
        
class identify_gate(smach.state):
    def __init__(self):
        smach.state.__init__(self, outcomes=['gate_found', 'no_gate_found'])

    def execute(self, userdata):
        rospy.loginfo('Executing state identify_gate')
        if (objects_detected == "gate"):
            return "Align_with Gate"
        else:
            return "Spin"

class Spin(smach.state):
    def __init__(self):
        smach.state.__init__(self, outcomes=['gate_found', 'no_gate_found'])

    def execute(self, userdata):
        rospy.loginfo('Executing state Spin')
        moveit.pose.rotation.y = 30 grados
        return "identify_gate"

class Align_with_Gate(smach.state):
    def __init__(self):
        smach.state.__init__(self, outcomes=['gate_found', 'no_gate_found'])

    def execute(self, userdata):
        moveit
        rospy.loginfo('Executing state Align_with_Gate')
        if (objects_detected == "gate"):
            return "Align_with Gate"
        else:
            return "Spin"