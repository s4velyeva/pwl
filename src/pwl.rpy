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
    PWL_START_LABEL = 'pwl_JUDGE'

    PWL_GIT = None
    PWL_OS = None
    PWL_ENABLE_LINUX_FEATURES = None

    PWL_NOTICE_TEXT = 'You are using Windows.\nMost features will be disabled.'

    # - Checks mod namespace conflicts - #
    def CheckModConflicts(namespace):
        if namespace in mods:
            return True
        else: return False

    import os

    PWL_GIT = True if os.path.exists('../.git') else False
    PWL_OS = os.uname()[0]

    if 'linux' in PWL_OS.lower():
        PWL_ENABLE_LINUX_FEATURES = True 
        PWL_NOTICE_TEXT = 'Huh, you are using Linux! Thanks!\nOSI4life))'

    del os

    mods[PWL_START_LABEL] = 'PROJECT OWL : HEADCRASHER'
    config.developer = True
    config.autoreload = True
