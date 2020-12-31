#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

def dsgefull(numshockperiods = 1):
    """
    We see that the only way this yields a solution is if Pi is a state.
    """
    inputdict = {}
    inputdict['equations'] = [
    'Pihat = KAPPA * Xhat + BETA * Pihat_p'
    ,
    'Xhat = Xhat_p - 1/GAMMA*(Ihat - Pihat_p - Rnhat)'
    ,
    'Ihat = PHIpi * Pihat + PHIy * Xhat + Rnhat + ui_0'
    ,
    'Rphat = Ihat - Pihat_p - Rnhat'
    ]

    # add shocks
    for i in range(numshockperiods - 1):
        # 'ui_0_p = ui_1'
        inputdict['equations'].append('ui_' + str(i) + '_p = ui_' + str(i + 1))
    # 'ui_11_p = 0'
    inputdict['equations'].append('ui_' + str(numshockperiods - 1) + '_p = 0')


    inputdict['paramssdict'] = {'BETA': 0.95, 'KAPPA': 0.1, 'GAMMA': 1, 'PHIpi': 1.5, 'PHIy': 0}


    inputdict['controls'] = ['Xhat', 'Pihat', 'Ihat', 'Rphat']
    inputdict['states'] = [] + ['ui_' + str(i) for i in range(numshockperiods)]
    inputdict['shocks'] = ['Rnhat']

    inputdict['mainvars'] = ['Xhat', 'Pihat', 'Rphat', 'Ihat']
    inputdict['showirfs'] = []

    inputdict['loglineareqs'] = True
    sys.path.append(str(__projectdir__ / Path('submodules/dsge-perturbation/')))
    from dsge_bkdiscrete_func import discretelineardsgefull
    discretelineardsgefull(inputdict)

    return(inputdict)


def forwardguidance(numshockperiods = 1):
    inputdict = dsgefull(numshockperiods = numshockperiods)
    Rshockvec = [-0.01] * numshockperiods
    sys.path.append(str(__projectdir__ / Path('submodules/dsge-fixvar-shock/')))
    from forwardsim_func import getshocks_forwardguidance
    getshocks_forwardguidance(inputdict, Rshockvec, shockname = 'ui_', varfgname = 'Rphat', pltshow = True)

# Run:{{{1
forwardguidance(numshockperiods = 20)
