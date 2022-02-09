from pyxdsm import XDSM

opt = 'Optimization'
lpopt = 'LP_Optimization'
solver = 'MDA'
ecomp = 'Analysis'
icomp = 'ImplicitAnalysis'
group = 'Metamodel'
func = 'Function'

#%% Generate object
x = XDSM.XDSM()

# x.add_system('MTOW', icomp, (r'\text{MTOW}', r'\text{Estimation}'))
# x.add_system('Empty Weight', ecomp, (r'\text{Empty}', r'\text{Weight}'))
# x.add_system('tail', ecomp, (r'\text{Tail}', r'\text{Sizing}'))

#%% Mission
x.add_system('mission', ecomp, (r'\text{Mission Segment}', r'\text{Fuel Fraction}'), stack=True, faded = True)

#%% Fuel fractions
x.add_system('ff', ecomp, (r'\text{Fuel-Weight}', r'\text{Estimation}'), faded = True)

#%% Maximum takeoff weight
x.add_system('mtow', icomp, (r'\text{Takeoff Weight }', r'\text{Estimation}'), faded = True)

#%% Empty weight
x.add_system('empty', ecomp, (r'\text{Empty Weight}', r'\text{Estimation}'),)# faded = True)

#%% Connections
x.connect('mtow', 'empty', r'W_0')
x.connect('mission', 'ff', r'FFs')
x.connect('ff', 'mtow', r'W_f/W_0')
x.connect('empty', 'mtow', r'W_e/W_0')

#%% Processes
x.add_process(['mission', 'ff', 'mtow', 'empty', 'mtow'])

#%% Inputs
x.add_input('mission', r'\text{Mission Data}')
x.add_input('mtow', r'W_\text{crew}, W_\text{payload}, W_{0_\text{init}}')

#%% Outputs
x.add_output('mtow', r'W_0^*')

#%% Writing
x.write(
        'XDSMEmpty',     # Filename
        build   = True,  # Build PDF using PDFLaTeX
        cleanup = True,  # Clean up TeX junk
        quiet   = False, # Write PDFLaTeX output to terminal
        outdir  = 'pics' # Output directory (relative path)
    )