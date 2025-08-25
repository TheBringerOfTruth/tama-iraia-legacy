from pyrosetta import init, pose_from_file

init()
pose = pose_from_file("example.pdb")
score = pose.energies().total_energy()
print("Rosetta Score:", score)
from pyrosetta import init, pose_from_file