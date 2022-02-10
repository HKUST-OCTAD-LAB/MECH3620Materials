from pyxdsm.XDSM import XDSM

opt = 'Optimization'
lpopt = 'LP_Optimization'
solver = 'MDA'
ecomp = 'Analysis'
icomp = 'ImplicitAnalysis'
group = 'Metamodel'
func = 'Function'

x = XDSM(use_sfmath = False)

x.add_system('TbW', opt, (r'(P/W) \text{ and } (W/S)', r'\text{Optimization}'))
x.add_system('drag', ecomp, (r'\text{Drag}', r'\text{Polar}'))
x.add_system('stall', icomp, (r'\text{Stall Speed}', r'\text{Constraint}'))
x.add_system('climb', icomp, (r'\text{Climb}', r'\text{Constraints}'), stack = True)
x.add_system('cruise', icomp, (r'\text{Cruise}', r'\text{Constraint}'))
x.add_system('cons', icomp, (r'\text{Other Mission}', r'\text{Constraints}'), stack = True)

x.connect('drag', 'cruise', (r'C_{D_0}, k'))
x.connect('drag', 'stall', (r'C_{D_0}, k'))
x.connect('drag', 'climb', (r'C_{D_0}, k'), stack = True)
x.connect('drag', 'cons', (r'C_{D_0}, k'), stack = True)
x.connect('TbW', 'cruise', r'(W/S)')
x.connect('TbW', 'climb', r'(W/S)', stack = True)
x.connect('TbW', 'cons', r'(W/S)', stack = True)
x.connect('stall', 'TbW', r'(W/S)_\text{stall}')
x.connect('cruise', 'TbW',  r'(P/W)_\text{cruise}')
x.connect('climb', 'TbW', r'(P/W)_\text{climb}', stack = True)
x.connect('cons', 'TbW', r'(P/W)_\text{mission}', stack = True)

x.add_input('drag', (r'c_f, S_{\text{wet}}/S_{\text{ref}}', r'AR, e, C_{L_{\alpha = 0}}'))
x.add_input('cruise', r'V_\text{cruise}, \eta_\text{prop}')
x.add_input('climb', r'V_{R/C}, \eta_\text{prop}')
x.add_input('stall', r'C_{L_\text{max}}, V_\text{stall}, \eta_\text{prop}')
x.add_input('cons', r'V, \eta_\text{prop}, \ldots')
x.add_input('TbW', (r'(P/W)_0, (W/S)_0'))

x.add_output('TbW', r'(P/W)^*, (W/S)^*')

x.write(
        'MatchingChart', # Filename
        build   = True,  # Build PDF using PDFLaTeX
        cleanup = True,  # Clean up TeX junk
        quiet   = False, # Write PDFLaTeX output to terminal
        outdir  = 'pics' # Output directory (relative path)
    )