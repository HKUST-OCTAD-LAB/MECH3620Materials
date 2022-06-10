#%%
from pyxdsm import XDSM

#%%
opt = 'Optimization'
lpopt = 'LP_Optimization'
solver = 'MDA'
ecomp = 'Analysis'
icomp = 'ImplicitAnalysis'
group = 'Metamodel'
func = 'Function'

#%%
x = XDSM.XDSM()
x.add_system('TbW', opt, (r'T/W', r'\text{Optimization}'))
x.add_system('MTOW', icomp, (r'\text{MTOW}', r'\text{Estimation}'))
x.add_system('tail', ecomp, (r'\text{Tail}', r'\text{Sizing}'))
x.add_system('empty', ecomp, (r'\text{Empty}', r'\text{Weight}'))
x.add_system('drag', ecomp, (r'\text{Drag}', r'\text{Polar}'))
x.add_system('fuel', ecomp, (r'\text{Fuel}', r'\text{Weight}'))
x.add_system('WbS', ecomp, (r'\text{Wing}', r'\text{Loading}'))

#%%
x.connect('MTOW', 'WbS', r'W_0')
x.connect('MTOW', 'TbW', r'W_0')
x.connect('MTOW', 'empty', r'(W_0)_i')
x.connect('empty', 'MTOW', r'W_e/W_0')
x.connect('tail', 'empty', r'S_{HT}, S_{VT}')
x.connect('TbW', 'empty', r'(T_0)_i')
x.connect('fuel', 'MTOW', r'W_f/W_0')
x.connect('drag', 'TbW', (r'C_{D_0}, K, C_{L_{\text{max}}}'))
x.connect('WbS', 'TbW', r'W_0/S_{\text{ref}}')
x.connect('drag', 'fuel', (r'C_{D_0}, K, C_{L_{\text{max}}}'))

#%%
x.add_input('drag', r'c_f, S_{\text{wet}}/S_{\text{ref}}, AR,e')
x.add_input('tail',  (r'S_{\text{ref}}, L_{\text{fus}}, D_{\text{fus}}'))
x.add_input('fuel', r'C, R, E, \rho')
x.add_input('WbS', r'S_{\text{ref}}')
x.add_input('empty', (r'S_{\text{ref}}, L_{\text{fus}}, D_{\text{fus}}', r'c_f, S_{\text{wet}}/S_{\text{ref}}, AR,e'))
x.add_input('TbW', (r's_{FL}, K_S, G, M'))

#%%
x.add_output('MTOW', 'W_0^*')
x.add_output('TbW', '(T/W)^*')

#%%
x.write(
        'DesignFramework', # Filename
        build   = True,    # Build PDF using PDFLaTeX
        cleanup = True,    # Clean up TeX junk
        quiet   = False,   # Write PDFLaTeX output to terminal
        outdir  = '../pics'   # Output directory (relative path)
    )
# %%
