# Syenasweta Mechanical Keyboard
# Keymaps Layout Author by Nashrullah ALi Fauzi
# Hardware by Raspberry Pi Pico RP2040
# Software by CircuitPython 8.2.6
# Keyboard Firmware by KMK

print("Starting Syenasweta - Synwt 4x12 Ortholinear Mechanical Keyboard")
import microcontroller
import board
import time
import supervisor
import storage
import usb_cdc
import usb_hid
import usb_midi

print(dir(board))

# from board import *
from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence, unicode_string_sequence, unicode_codepoint_sequence
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes, HIDReportTypes, HIDUsage, HIDUsagePage
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.oneshot import OneShot
from kmk.modules.power import Power
from kmk.modules.serialace import SerialACE
from kmk.modules.tapdance import TapDance
from kmk.modules.dynamic_sequences import DynamicSequences
from kmk.modules.capsword import CapsWord
from kmk.modules.rapidfire import RapidFire
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.midi import MidiKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.international import International

# Moduls
layers=Layers()
combos=Combos()
holdtap=HoldTap()
mousekeys=MouseKeys()
oneshot=OneShot()
power=Power()
serialace=SerialACE()
tapdance=TapDance()
dynamicsequences=DynamicSequences()
caps_word=CapsWord(timeout=5000)
rapidfire=RapidFire()
sticky_mod=StickyMod()
midikeys=MidiKeys()

# Moduls Config
holdtap.tap_time=300
mousekeys.max_speed=10 # default is 10
mousekeys.acc_interval=20  # default is 20 (delta ms to apply acceleration)
mousekeys.move_step=1 # default is 1
oneshot.tap_time=1000
tapdance.tap_time=750
caps_word.keys_ignored.append(KC.COMMA)

# Extensions
mediakeys = MediaKeys()
international = International()

# Extensions Config
#

# Keyboard Setting
syenasweta = KMKKeyboard()
syenasweta.debug_enabled = False # or True
syenasweta.modules = [layers, combos, holdtap, mousekeys, oneshot, power, serialace, tapdance, dynamicsequences, caps_word, rapidfire, sticky_mod, midikeys]
syenasweta.extensions = [mediakeys, international]

# Switch Matrix
# COLUMNS = vertical, ROWS = horizontal
# COL2ROW and ROW2COL are equivalent to their meanings in QMK.
# COLUMNS = 0; ROWS = 1
# COL2ROW = COLUMNS; ROW2COL = ROWS

syenasweta.col_pins=[board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11]
syenasweta.row_pins=[board.GP12,board.GP13,board.GP14,board.GP15]
syenasweta.rollover_cols_every_rows=4
syenasweta.diode_orientation=DiodeOrientation.COLUMNS
syenasweta.coord_mapping = [
0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11,
12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47
]

# Synwt Keyboard Layout for Syenasweta Mechanical keyboard
# Author: Nashrullah ALi Fauzi

SYNWT=send_string("Hello, I am Syenasweta.")

# Keyboard Modules

LT_1_TO_15=KC.LT(1,KC.TO(15),prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_2_KC_BSLS=KC.LT(2,KC.BSLS,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_3_KC_LBRC=KC.LT(3,KC.LBRC,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_4_KC_APP=KC.LT(4,KC.APP,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_5_KC_CW=KC.LT(5,KC.CW,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_6_KC_SLSH=KC.LT(6,KC.SLSH,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_7_KC_RBRC=KC.LT(7,KC.RBRC,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_8_KC_GESC=KC.LT(8,KC.GESC,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_9_KC_COMM=KC.LT(9,KC.COMM,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_10_KC_SCLN=KC.LT(10,KC.SCLN,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_11_KC_QUOT=KC.LT(11,KC.QUOT,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_12_KC_EQL=KC.LT(12,KC.EQL,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_13_KC_DOT=KC.LT(13,KC.DOT,prefer_hold=True,tap_interrupted=False,tap_time=250)
LT_14_KC_MINS=KC.LT(14,KC.MINS,prefer_hold=True,tap_interrupted=False,tap_time=250)

OS_LCTL=KC.OS(KC.LCTL,tap_time=None)
OS_LSFT=KC.OS(KC.LSFT,tap_time=None)
OS_LALT=KC.OS(KC.LALT,tap_time=None)
OS_LGUI=KC.OS(KC.LGUI,tap_time=1000)

HT_T_RCTL=KC.HT(KC.T,KC.RCTRL,prefer_hold=True,tap_interrupted=False,tap_time=300,repeat=HoldTapRepeat.ALL) # T and Right CTRL
HT_M_RSFT=KC.HT(KC.M,KC.RSFT,prefer_hold=True,tap_interrupted=False,tap_time=300,repeat=HoldTapRepeat.ALL) # M and Right Shift
HT_P_RALT=KC.HT(KC.P,KC.RALT,prefer_hold=True,tap_interrupted=False,tap_time=300,repeat=HoldTapRepeat.ALL) # P and Right ALT
HT_Z_RGUI=KC.HT(KC.Z,KC.RGUI,prefer_hold=True,tap_interrupted=False,tap_time=300,repeat=HoldTapRepeat.ALL) # Z and Right GUI

# Makrkdown Keys
# MD_=simple_key_sequence(())
# MD_=send_string("")

# MD_NUMBER=KC.TD(KC.N0,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,tap_time=80)

MD_HEADING1=simple_key_sequence((KC.HASH,KC.SPC))
MD_HEADING2=simple_key_sequence((KC.HASH,KC.HASH,KC.SPC))
MD_HEADING3=simple_key_sequence((KC.HASH,KC.HASH,KC.HASH,KC.SPC))
MD_HEADING4=simple_key_sequence((KC.HASH,KC.HASH,KC.HASH,KC.HASH,KC.SPC))
MD_HEADING5=simple_key_sequence((KC.HASH,KC.HASH,KC.HASH,KC.HASH,KC.HASH,KC.SPC))
MD_HEADING6=simple_key_sequence((KC.HASH,KC.HASH,KC.HASH,KC.HASH,KC.HASH,KC.HASH,KC.SPC))
MD_HEADINGID=simple_key_sequence((KC.SPC,KC.LCBR,KC.HASH,KC.RCBR))

# MD_HEADING=KC.TD(MD_HEADING1,MD_HEADING2,MD_HEADING3,MD_HEADING4,MD_HEADING5,MD_HEADING6,tap_time=80)

MD_BLOCKQUOTE=simple_key_sequence((KC.RABK,KC.SPC))
MD_NESTEDBLOCKQUOTE=simple_key_sequence((KC.RABK,KC.RABK,KC.SPC))
MD_DEFINITIONLIST=simple_key_sequence((KC.T,KC.E,KC.R,KC.M,KC.ENT,KC.COLN,KC.SPC,KC.D,KC.E,KC.F,KC.I,KC.N,KC.I,KC.T,KC.I,KC.T,KC.I,KC.O,KC.N))
MD_FENCEDCODEBLOCK=simple_key_sequence((KC.ENT,KC.ENT,KC.GRV,KC.GRV,KC.GRV,KC.ENT))
MD_TASKLISTCOMPLETE=send_string("- [x] ")
MD_TASKLISTINCOMPLETE=send_string("- [ ] ")

# MD_ORDEREDLIST_NUMBER=KC.TD(KC.N0,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,tap_time=80)
# MD_ORDEREDLIST_DOTSPACE=simple_key_sequence((KC.DOT,KC.SPC))
MD_ORDEREDLIST=simple_key_sequence((KC.DOT,KC.SPC))
MD_UNORDEREDLIST=simple_key_sequence((KC.MINS,KC.SPC))
# MD_TABLE=send_string("")
MD_FOOTNOTE=simple_key_sequence((KC.LBRC,KC.CIRC,KC.RBRC))
MD_REFERENCE=simple_key_sequence((KC.LBRC,KC.CIRC,KC.RBRC,KC.COLN,KC.SPC))
MD_HORIZONTALRULE=simple_key_sequence((KC.ENT,KC.ENT,KC.MINS,KC.MINS,KC.MINS,KC.ENT,KC.ENT))
MD_YAMLFRONTMATTER=simple_key_sequence((KC.MINS,KC.MINS,KC.MINS,KC.ENT,KC.ENT,KC.MINS,KC.MINS,KC.MINS))

MD_STRONG=simple_key_sequence((KC.ASTR,KC.ASTR))
MD_EMPHASIS=KC.ASTR
MD_STRONGEMPHASIS=simple_key_sequence((KC.ASTR,KC.ASTR,KC.ASTR))
MD_UNDERLINE=send_string("<u></u>")
MD_CODE=KC.GRV
MD_STRIKETHROUGHT=simple_key_sequence((KC.TILD,KC.TILD))

MD_HIGHTLIGHT=simple_key_sequence((KC.EQL,KC.EQL))
MD_COMMENT=send_string("<!---->")
MD_SUBSCRIPT=KC.TILD
MD_SUPERSCRIPT=KC.CIRC
MD_LINK=send_string("[title](https://example.com)")
MD_IMAGE=send_string("![alt text](image.jpg)")

# Git and CLI Keys 
# GIT_=simple_key_sequence(())
# GIT_=send_string("")

CONSL_AMPR=simple_key_sequence((KC.SPC,KC.AMPR,KC.AMPR,KC.SPC))
CONSL_ENT=KC.ENT

APT_UPDATE=simple_key_sequence((KC.A,KC.P,KC.T,KC.SPC,KC.U,KC.P,KC.D,KC.A,KC.T,KC.E))
APT_UPGRADE=simple_key_sequence((KC.A,KC.P,KC.T,KC.SPC,KC.U,KC.P,KC.G,KC.R,KC.A,KC.D,KC.E))
APT_INSTALL=simple_key_sequence((KC.A,KC.P,KC.T,KC.SPC,KC.I,KC.N,KC.S,KC.T,KC.A,KC.L,KC.L,KC.SPC))
APT_REMOVE=simple_key_sequence((KC.A,KC.P,KC.T,KC.SPC,KC.R,KC.E,KC.M,KC.O,KC.V,KC.E,KC.SPC))
APT_AUTOREMOVE=((KC.A,KC.P,KC.T,KC.SPC,KC.A,KC.U,KC.T,KC.O,KC.R,KC.E,KC.M,KC.O,KC.V,KC.E))
APT_CLEAN=simple_key_sequence((KC.A,KC.P,KC.T,KC.SPC,KC.C,KC.L,KC.E,KC.A,KC.N))
APT_CLEAR=simple_key_sequence((KC.A,KC.P,KC.T,KC.SPC,KC.C,KC.L,KC.E,KC.A,KC.R))

APT_UPDATE_ENT=simple_key_sequence((APT_UPDATE,CONSL_ENT))
APT_UPGRADE_ENT=simple_key_sequence((APT_UPGRADE,CONSL_ENT))
APT_UPD_UPG_ENT=simple_key_sequence((APT_UPDATE,CONSL_AMPR,APT_UPGRADE,CONSL_ENT))

GIT_CLONE=simple_key_sequence((KC.G,KC.I,KC.T,KC.SPC,KC.C,KC.L,KC.O,KC.N,KC.E,KC.SPC))
GIT_STATUS=simple_key_sequence((KC.G,KC.I,KC.T,KC.SPC,KC.S,KC.T,KC.A,KC.T,KC.U,KC.S))
GIT_ADD=simple_key_sequence((KC.G,KC.I,KC.T,KC.SPC,KC.A,KC.D,KC.D,KC.SPC,KC.DOT))
GIT_COMMIT=simple_key_sequence((KC.G,KC.I,KC.T,KC.SPC,KC.C,KC.O,KC.M,KC.M,KC.I,KC.T,KC.SPC,KC.MINS,KC.M,KC.SPC,KC.DQUO,KC.E,KC.D,KC.I,KC.T,KC.DQUO))
GIT_AC=simple_key_sequence((GIT_ADD,CONSL_AMPR,GIT_COMMIT))
GIT_PUSH=simple_key_sequence((KC.G,KC.I,KC.T,KC.SPC,KC.P,KC.U,KC.S,KC.H))
GIT_ACP=simple_key_sequence((GIT_ADD,CONSL_AMPR,GIT_COMMIT,GIT_PUSH))
GIT_PULL=simple_key_sequence((KC.G,KC.I,KC.T,KC.SPC,KC.P,KC.U,KC.L,KC.L))

GIT_ACP_ENT=simple_key_sequence((GIT_ADD,CONSL_AMPR,GIT_COMMIT,GIT_PUSH,CONSL_ENT))
GIT_PULL_ENT=simple_key_sequence((GIT_PULL,CONSL_ENT))

# All Keymaps
syenasweta.keymap=[
    [ # Layer 0 (Sywnt Keys)
    OS_LCTL,	LT_4_KC_APP,	LT_8_KC_GESC,	LT_12_KC_EQL,	LT_14_KC_MINS,	KC.TAB,	KC.BKDL,	KC.S,	KC.Y,	KC.N,	KC.W,	HT_T_RCTL,
    OS_LSFT,	LT_3_KC_LBRC,	LT_7_KC_RBRC,	LT_11_KC_QUOT,	KC.A,	KC.U,	KC.O,	KC.C,	KC.F,	KC.K,	KC.G,	HT_M_RSFT,
    OS_LALT,	LT_2_KC_BSLS,	LT_6_KC_SLSH,	LT_10_KC_SCLN,	KC.I,	KC.E,	KC.B,	KC.D,	KC.H,	KC.J,	KC.L,	HT_P_RALT,
    OS_LGUI,	LT_1_TO_15,	LT_5_KC_CW,	LT_9_KC_COMM,	LT_13_KC_DOT,	KC.SPC,	KC.ENT,	KC.Q,	KC.R,	KC.V,	KC.X,	HT_Z_RGUI
    ],
    [ # Layer 1 (Number & Fn Keys)
    OS_LCTL,	KC.NO,	KC.NO,	KC.N7,	KC.N8,	KC.N9,	KC.F10,	KC.F11,	KC.F12,	KC.F22,	KC.F23,	KC.F24,
    OS_LSFT,	KC.NO,	KC.NO,	KC.N4,	KC.N5,	KC.N6,	KC.F7,	KC.F8,	KC.F9,	KC.F19,	KC.F20,	KC.F21,
    OS_LALT,	KC.NO,	KC.NO,	KC.N1,	KC.N2,	KC.N3,	KC.F4,	KC.F5,	KC.F6,	KC.F16,	KC.F17,	KC.F18,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.N0,	KC.GRV,	KC.NO,	KC.F1,	KC.F2,	KC.F3,	KC.F13,	KC.F14,	KC.F15
    ],
    [ # Layer 2 (Keypad, Arrow Keys & Homekey)
    OS_LCTL,	KC.NO,	KC.NO,	KC.P7,	KC.P8,	KC.P9,	KC.NLCK,	KC.NO,	KC.SLCK,	KC.PSCR,	KC.NO,	KC.HOME,
    OS_LSFT,	KC.NO,	KC.NO,	KC.P4,	KC.P5,	KC.P6,	KC.PAST,	KC.PSLS,	KC.NO,	KC.UP,	KC.NO,	KC.PGUP,
    OS_LALT,	KC.NO,	KC.NO,	KC.P1,	KC.P2,	KC.P3,	KC.PPLS,	KC.PMNS,	KC.LEFT,	KC.DOWN,	KC.RGHT,	KC.PGDN,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.P0,	KC.PDOT,	KC.PCMM,	KC.PEQL,	KC.PENT,	KC.PAUS,	KC.INS,	KC.DEL,	KC.END
    ],
    [ # Layer 3 (US ANSI Shifted Symbols Keys)
    OS_LCTL,	KC.NO,	KC.NO,	KC.AMPR,	KC.ASTR,	KC.LPRN,	KC.PIPE,	KC.QUES,	KC.DQUO,	KC.NO,	KC.NO,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.DLR,	KC.PERC,	KC.CIRC,	KC.LABK,	KC.RABK,	KC.COLN,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.EXLM,	KC.AT,	KC.HASH,	KC.PLUS,	KC.LCBR,	KC.RCBR,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.RPRN,	KC.TILD,	KC.GRV,	KC.UNDS,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 4 (Application Keys)
    OS_LCTL,	KC.NO,	KC.NO,	KC.LCTL(KC.C),	KC.LCTL(KC.V),	KC.LCTL(KC.F),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.LCTL(KC.Y),	KC.LCTL(KC.Z),	KC.LCTL(KC.X),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.APP,	KC.LCTL(KC.A),	KC.RSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.LSFT(KC.F1),	KC.LALT(KC.F2),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 5 (Multimedia Keys)
    OS_LCTL,	KC.NO,	KC.NO,	KC.MPRV,	KC.MNXT,	KC.VOLD,	KC.VOLU,	KC.MRWD,	KC.MFFD,	KC.NO,	KC.NO,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.MSTP,	KC.MUTE,	KC.MPLY,	KC.EJCT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.BRID,	KC.BRIU,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 6 (Mouse Keys)
    OS_LCTL,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.MB_BTN4,	KC.MB_MMB,	KC.MB_BTN5,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.MW_UP,	KC.MB_LMB,	KC.MS_UP,	KC.MB_RMB,	KC.MW_RT,
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.MW_LT,	KC.MS_LT,	KC.MS_DN,	KC.MS_RT,	KC.MW_DN,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO	
    ],
    [ # Layer 7 (Midi Keys)
    OS_LCTL,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 8 (Markdown Keys)
    OS_LCTL,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	MD_HEADINGID,	MD_HEADING1,	MD_HEADING2,	MD_HEADING3,	MD_HEADING4,	MD_HEADING5,	MD_HEADING6,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	MD_BLOCKQUOTE,	MD_NESTEDBLOCKQUOTE,	MD_DEFINITIONLIST,	MD_FENCEDCODEBLOCK,	MD_TASKLISTCOMPLETE,	MD_TASKLISTINCOMPLETE,
    OS_LALT,	KC.NO,	KC.NO,	MD_HIGHTLIGHT,	MD_SUBSCRIPT,	MD_LINK,	MD_ORDEREDLIST,	MD_UNORDEREDLIST,	MD_FOOTNOTE,	MD_REFERENCE,	MD_HORIZONTALRULE,	MD_YAMLFRONTMATTER,
    OS_LGUI,	KC.TO(0),	KC.NO,	MD_COMMENT,	MD_SUPERSCRIPT,	MD_IMAGE,	MD_STRONG,	MD_EMPHASIS,	MD_STRONGEMPHASIS,	MD_UNDERLINE,	MD_CODE,	MD_STRIKETHROUGHT
    ],
    [ # Layer 9 (Git and CLI Keys)
    OS_LCTL,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 10 (Shortcut Layer for …)
    OS_LCTL,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 11 (Shortcut Layer for …)
    OS_LCTL,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 12 (Shortcut Layer for …)
    OS_LCTL,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 13 (Ignore This Layer)
    KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    KC.NO,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO
    ],
    [ # Layer 14 (Internal KMK Key)
    OS_LCTL,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.RESET,	KC.RELOAD,	KC.NO,	KC.NO,	KC.PS_ON,	KC.PS_OFF,	KC.PS_TOG,
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.DEBUG,	KC.ANY,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.ANY,	KC.ANY,	KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.NO,	KC.BKDL,	KC.GESC,	KC.UC_MODE_NOOP,	KC.UC_MODE_LINUX,	KC.UC_MODE_MACOS,	KC.UC_MODE_WINC,	KC.MACRO_SLEEP_MS(300)
    ],
    [ # Layer 15 (Keyboard Layer Navigation)
    OS_LCTL,	KC.NO,	KC.NO,	SYNWT,	KC.DF(12),	KC.DF(13),	KC.DF(14),	KC.DF(15),	KC.TO(12),	KC.TO(13),	KC.TO(14),	KC.TO(15),
    OS_LSFT,	KC.NO,	KC.NO,	KC.NO,	KC.DF(8),	KC.DF(9),	KC.DF(10),	KC.DF(11),	KC.TO(9),	KC.TO(8),	KC.TO(10),	KC.TO(11),
    OS_LALT,	KC.NO,	KC.NO,	KC.NO,	KC.DF(4),	KC.DF(5),	KC.DF(6),	KC.DF(7),	KC.TO(4),	KC.TO(5),	KC.TO(6),	KC.TO(7),
    OS_LGUI,	KC.TO(0),	KC.NO,	KC.NO,	KC.DF(0),	KC.DF(1),	KC.DF(2),	KC.DF(3),	KC.TO(0),	KC.TO(1),	KC.TO(2),	KC.TO(3)
    ]
]

if __name__ == '__main__':
    syenasweta.go(hid_type=HIDModes.USB) # Wired USB enable
