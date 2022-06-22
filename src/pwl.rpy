# Copyright (c) 2022 rekendo-ua
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


init python:

    # constants
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

    PWL_VERSION = '0.0.1-build20220622-git'

    # checks mod namespace conflicts
    def CheckModConflicts(namespace):
        if namespace in mods:
            return True
        else: return False

    mods[PWL_START_LABEL] = 'PROJ.OWL code: alice-amber'
    config.developer = True
    config.autoreload = True

    try:
        modsImages[PWL_START_LABEL] = (PWL_IMG + 'etc/mods_image_logo_320x180.jpg', False, PWL_START_LABEL)
    except:
        pass


# init for variables
init:
    define persistent.show_now_playing = True
    define gui.accent_color = "#eb244b"
    define gui.text_font = PWL_ROOT + "res/fonts/ubuntu.ttf"
