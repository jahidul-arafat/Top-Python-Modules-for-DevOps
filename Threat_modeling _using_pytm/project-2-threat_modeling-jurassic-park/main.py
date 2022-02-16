#!/usr/bin/env python3
from pytm import (
    TM,
    Boundary,
    ExternalEntity,
    Process,
    Datastore,
    Dataflow,
    Classification,
    Data
)

# Step-0: Initialize the threat model
tm = TM("Jurassic Park Threat Modeling")
tm.description = """
#### Jurassic Park Threat modeling: The Post Mortem Scenarios for which we are designing our today's threat model
- Post Mortem (1/7): Jahidul Arafat, developer, embeds malware in his deliverable to shut down the security system,
allowing him access to embryo storage.
- Post Mortem (2/7): Jahidul's malware is activated, shutting down the security system and cutting power to some electric fences.
- Post Mortem (3/7): JajVir shut down the entire park system, terminating Jahidul's malware.
- Post Mortem (4/7): JajVir restarts the system, but only on backup power, disabling remaining fences.
- Post Mortem (5/7): Ellie Sattler starts additional power generators in a far-away maintenance shed
- Post Mortem (6/7): Lex Murphy reboots the security system via the Silicon Graphics Terminal
- Post Mortem (7/7): Full security system operation is restored.

"""

tm.isOrdered = True
tm.mergeResponses = True
tm.assumptions = [
    "list your assumptions here",
    "One",
    "Two"
]

# Step-1: Defining the System Components
# 1A. Define the core systems
silicon_graphics_fsn = Process("Silicon Graphics File System Navigator")
silicon_graphics_fsn.OS = "Unix"

file_server = Datastore("Park File Server")
file_server.OS = "Unix"

park_security_system = Process("Park Security System")
park_security_system.maxClassification = Classification.SENSITIVE
park_security_system.controls.handlesCrashes = False

# 1B. Define External Entities
locks = ExternalEntity("Doors/Fences")
staff = ExternalEntity("Staff")
raptors = ExternalEntity("Raptors")

# Step-2: Defining the Dataflows
# 2A. terminal >> file server
silicon_graphics_fsn_to_file_server = Dataflow(silicon_graphics_fsn,file_server, "Workstation File Server Access")
silicon_graphics_fsn_to_file_server.protocol = "NFS"
silicon_graphics_fsn_to_file_server.dstPort = 2049
silicon_graphics_fsn_to_file_server.data = Data("Complete Park Records", classification=Classification.TOP_SECRET)

# 2B. Park Security System >> File Server
park_security_system_to_file_server = Dataflow(park_security_system,file_server,"Security System Data")
park_security_system_to_file_server.protocol = "NFS"
park_security_system_to_file_server.dstPort = 2049
park_security_system_to_file_server.data = Data("Physical Security Instructions", classification=Classification.SENSITIVE)

# 2C. Park Security System >> locks
# Actuator - a device that causes a machine or other device to operate.
park_security_system_to_locks = Dataflow(park_security_system,locks,"Actuator Instructions")
park_security_system_to_locks.protocol = "HTTP"
park_security_system_to_locks.data = Data("Door and fence activations", classification=Classification.SENSITIVE)

# 2D. staff >> silicon graphics file system navigator
staff_to_fsn = Dataflow(staff,silicon_graphics_fsn,"")
staff_to_fsn.protocol = "Physical"

# 2E. raptors >> locks
raptors_to_locks = Dataflow(raptors,locks,"")
raptors_to_locks.protocol = "Physical"

# Step-3: Define Boundaries
dino_free = Boundary("Dino Free Boundary")
control_room = Boundary("Control Room")
silicon_graphics_fsn.inBoundary=control_room
file_server.inBoundary=control_room
park_security_system.inBoundary=control_room
control_room.inBoundary=dino_free
staff.inBoundary=dino_free
locks.inBoundary=dino_free

if __name__ == "__main__":
    tm.process()






