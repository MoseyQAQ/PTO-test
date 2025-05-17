
# UniPero
# from deepmd.calculator import DP
# calc = DP(model='UniPero.pb')

# CHGNET
# from chgnet.model.dynamics import CHGNetCalculator
# from chgnet.model import CHGNet
# chgnet_model = CHGNet().from_file('chgnet_0.3.0_e29f68s314m37.pth.tar')
# calc = CHGNetCalculator(chgnet_model)

# ORB
# from orb_models.forcefield import pretrained
# from orb_models.forcefield.calculator import ORBCalculator
# orbff = pretrained.orb_v2(device='cuda')
# calc = ORBCalculator(orbff, device='cuda')

# SevenNet
# from sevenn.calculator import SevenNetCalculator
# calc = SevenNetCalculator(model='7net-l3i5', device='cuda')

# MACE
# from mace.calculators import mace_mp
# calc = mace_mp(model="mace_agnesi_medium.model", dispersion=False, device='cuda')

# GPTFF
# from gptff.model.mpredict import ASECalculator
# calc = ASECalculator("gptff_v2.pth", "cuda")

# M3GNET
# from matgl.ext.ase import PESCalculator
# import matgl
# pot = matgl.load_model("M3GNet-MP-2021.2.8-PES") 
# calc = PESCalculator(pot)
