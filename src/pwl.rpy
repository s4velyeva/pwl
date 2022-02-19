#       Copyright (C) 2021 vicsave
# GNU General Public License
#

init python:

    # -- Constants -- #
    PWL_ROOT = 'mods/pwl/'
    PWL_IMG = 'mods/pwl/res/img/'
    PWL_AUDIO = 'mods/pwl/res/audio/'
    PWL_SPR = 'mods/pwl/res/img/spr/'
    PWL_CG = 'mods/pwl/res/img/cg/'
    PWL_BG = 'mods/pwl/res/img/bg/'
    PWL_MUS = 'mods/pwl/res/audio/music/'
    PWL_SFX = 'mods/pwl/res/audio/sound/'

    PWL_NAMESPACE = 'pwl'
    PWL_START_LABEL = 'pwl_main_menu_begin'

    # - Checks mod namespace conflicts - #
    def CheckModConflicts(namespace):
        if namespace in mods:
            return True
        else: return False

    mods[PWL_START_LABEL] = 'PROJ.OWL code: alice-amber'
    config.developer = True
    config.autoreload = True
# eof
