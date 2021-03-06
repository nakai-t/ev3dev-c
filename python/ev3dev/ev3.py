# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ev3', [dirname(__file__)])
        except ImportError:
            import _ev3
            return _ev3
        if fp is not None:
            try:
                _mod = imp.load_module('_ev3', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ev3 = swig_import_helper()
    del swig_import_helper
else:
    import _ev3
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


EV3_BRICK = _ev3.EV3_BRICK

def ev3_init():
  return _ev3.ev3_init()
ev3_init = _ev3.ev3_init

def ev3_uninit():
  return _ev3.ev3_uninit()
ev3_uninit = _ev3.ev3_uninit

def ev3_write_binary(*args):
  return _ev3.ev3_write_binary(*args)
ev3_write_binary = _ev3.ev3_write_binary

def ev3_write(*args):
  return _ev3.ev3_write(*args)
ev3_write = _ev3.ev3_write

def ev3_write_bool(*args):
  return _ev3.ev3_write_bool(*args)
ev3_write_bool = _ev3.ev3_write_bool

def ev3_write_int(*args):
  return _ev3.ev3_write_int(*args)
ev3_write_int = _ev3.ev3_write_int

def ev3_write_dword(*args):
  return _ev3.ev3_write_dword(*args)
ev3_write_dword = _ev3.ev3_write_dword

def ev3_write_byte(*args):
  return _ev3.ev3_write_byte(*args)
ev3_write_byte = _ev3.ev3_write_byte

def ev3_write_float(*args):
  return _ev3.ev3_write_float(*args)
ev3_write_float = _ev3.ev3_write_float

def ev3_read_binary(*args):
  return _ev3.ev3_read_binary(*args)
ev3_read_binary = _ev3.ev3_read_binary

def ev3_read(*args):
  return _ev3.ev3_read(*args)
ev3_read = _ev3.ev3_read

def ev3_read_bool(*args):
  return _ev3.ev3_read_bool(*args)
ev3_read_bool = _ev3.ev3_read_bool

def ev3_read_int(*args):
  return _ev3.ev3_read_int(*args)
ev3_read_int = _ev3.ev3_read_int

def ev3_read_dword(*args):
  return _ev3.ev3_read_dword(*args)
ev3_read_dword = _ev3.ev3_read_dword

def ev3_read_byte(*args):
  return _ev3.ev3_read_byte(*args)
ev3_read_byte = _ev3.ev3_read_byte

def ev3_read_float(*args):
  return _ev3.ev3_read_float(*args)
ev3_read_float = _ev3.ev3_read_float

def ev3_listdir(*args):
  return _ev3.ev3_listdir(*args)
ev3_listdir = _ev3.ev3_listdir

def ev3_poweroff():
  return _ev3.ev3_poweroff()
ev3_poweroff = _ev3.ev3_poweroff
EV3_GREEN_LEFT = _ev3.EV3_GREEN_LEFT
EV3_GREEN_RIGHT = _ev3.EV3_GREEN_RIGHT
EV3_RED_LEFT = _ev3.EV3_RED_LEFT
EV3_RED_RIGHT = _ev3.EV3_RED_RIGHT
EV3_LED_OUTA = _ev3.EV3_LED_OUTA
EV3_LED_OUTB = _ev3.EV3_LED_OUTB
EV3_LED_OUTC = _ev3.EV3_LED_OUTC
EV3_LED_OUTD = _ev3.EV3_LED_OUTD
LED__COUNT_ = _ev3.LED__COUNT_
TRIGGER_NONE = _ev3.TRIGGER_NONE
TRIGGER_MMC0 = _ev3.TRIGGER_MMC0
TRIGGER_TIMER = _ev3.TRIGGER_TIMER
TRIGGER_HEARTBEAT = _ev3.TRIGGER_HEARTBEAT
TRIGGER_DEFAULT_ON = _ev3.TRIGGER_DEFAULT_ON
TRIGGER_TRANSIENT = _ev3.TRIGGER_TRANSIENT
TRIGGER_LEGOEV3_BATTERY_CHARGING_OR_FULL = _ev3.TRIGGER_LEGOEV3_BATTERY_CHARGING_OR_FULL
TRIGGER_LEGOEV3_BATTERY_CHARGING = _ev3.TRIGGER_LEGOEV3_BATTERY_CHARGING
TRIGGER_LEGOEV3_BATTERY_FULL = _ev3.TRIGGER_LEGOEV3_BATTERY_FULL
TRIGGER_LEGOEV3_BATTERY_CHARGING_BLINK_FULL_SOLID = _ev3.TRIGGER_LEGOEV3_BATTERY_CHARGING_BLINK_FULL_SOLID
TRIGGER_RFKILL0 = _ev3.TRIGGER_RFKILL0
TRIGGER_PHY0RX = _ev3.TRIGGER_PHY0RX
TRIGGER_PHY0TX = _ev3.TRIGGER_PHY0TX
TRIGGER_PHY0ASSOC = _ev3.TRIGGER_PHY0ASSOC
TRIGGER_PHY0RADIO = _ev3.TRIGGER_PHY0RADIO
TRIGGER_RFKILL1 = _ev3.TRIGGER_RFKILL1
TRIGGER__COUNT_ = _ev3.TRIGGER__COUNT_
LED_ATTR__COUNT_ = _ev3.LED_ATTR__COUNT_

def get_led_brightness(*args):
  return _ev3.get_led_brightness(*args)
get_led_brightness = _ev3.get_led_brightness

def set_led_brightness(*args):
  return _ev3.set_led_brightness(*args)
set_led_brightness = _ev3.set_led_brightness

def get_led_delay_off(*args):
  return _ev3.get_led_delay_off(*args)
get_led_delay_off = _ev3.get_led_delay_off

def set_led_delay_off(*args):
  return _ev3.set_led_delay_off(*args)
set_led_delay_off = _ev3.set_led_delay_off

def get_led_delay_on(*args):
  return _ev3.get_led_delay_on(*args)
get_led_delay_on = _ev3.get_led_delay_on

def set_led_delay_on(*args):
  return _ev3.set_led_delay_on(*args)
set_led_delay_on = _ev3.set_led_delay_on

def get_led_max_brightness(*args):
  return _ev3.get_led_max_brightness(*args)
get_led_max_brightness = _ev3.get_led_max_brightness

def get_led_trigger(*args):
  return _ev3.get_led_trigger(*args)
get_led_trigger = _ev3.get_led_trigger

def set_led_trigger(*args):
  return _ev3.set_led_trigger(*args)
set_led_trigger = _ev3.set_led_trigger

def get_led_trigger_inx(*args):
  return _ev3.get_led_trigger_inx(*args)
get_led_trigger_inx = _ev3.get_led_trigger_inx

def set_led_trigger_inx(*args):
  return _ev3.set_led_trigger_inx(*args)
set_led_trigger_inx = _ev3.set_led_trigger_inx

def ev3_led_trigger(*args):
  return _ev3.ev3_led_trigger(*args)
ev3_led_trigger = _ev3.ev3_led_trigger
LED_DIR = _ev3.LED_DIR
LIT_LEFT = _ev3.LIT_LEFT
LIT_RIGHT = _ev3.LIT_RIGHT
LIT__LOC__ = _ev3.LIT__LOC__
LIT_OFF = _ev3.LIT_OFF
LIT_GREEN = _ev3.LIT_GREEN
LIT_RED = _ev3.LIT_RED
LIT_AMBER = _ev3.LIT_AMBER
LIT__COL__ = _ev3.LIT__COL__

def set_light(*args):
  return _ev3.set_light(*args)
set_light = _ev3.set_light

def get_light(*args):
  return _ev3.get_light(*args)
get_light = _ev3.get_light

def set_light_trigger(*args):
  return _ev3.set_light_trigger(*args)
set_light_trigger = _ev3.set_light_trigger

def get_light_trigger(*args):
  return _ev3.get_light_trigger(*args)
get_light_trigger = _ev3.get_light_trigger

def set_light_blink(*args):
  return _ev3.set_light_blink(*args)
set_light_blink = _ev3.set_light_blink

def get_light_blink(*args):
  return _ev3.get_light_blink(*args)
get_light_blink = _ev3.get_light_blink
OUTPUT_DIR = _ev3.OUTPUT_DIR
OUTPUT__BASE_ = _ev3.OUTPUT__BASE_
OUTPUT_A = _ev3.OUTPUT_A
OUTPUT_B = _ev3.OUTPUT_B
OUTPUT_C = _ev3.OUTPUT_C
OUTPUT_D = _ev3.OUTPUT_D
OUTPUT__COUNT_ = _ev3.OUTPUT__COUNT_
OUTPUT_AUTO = _ev3.OUTPUT_AUTO
OUTPUT_EV3_TACHO_MOTOR = _ev3.OUTPUT_EV3_TACHO_MOTOR
OUTPUT_RCX_MOTOR = _ev3.OUTPUT_RCX_MOTOR
OUTPUT_RCX_LED = _ev3.OUTPUT_RCX_LED
OUTPUT_RAW = _ev3.OUTPUT_RAW
OUTPUT_MODE__COUNT_ = _ev3.OUTPUT_MODE__COUNT_

def ev3_output_inx(*args):
  return _ev3.ev3_output_inx(*args)
ev3_output_inx = _ev3.ev3_output_inx

def ev3_output_name(*args):
  return _ev3.ev3_output_name(*args)
ev3_output_name = _ev3.ev3_output_name

def get_output_mode(*args):
  return _ev3.get_output_mode(*args)
get_output_mode = _ev3.get_output_mode

def set_output_mode(*args):
  return _ev3.set_output_mode(*args)
set_output_mode = _ev3.set_output_mode

def get_output_modes(*args):
  return _ev3.get_output_modes(*args)
get_output_modes = _ev3.get_output_modes

def get_output_pin5_mv(*args):
  return _ev3.get_output_pin5_mv(*args)
get_output_pin5_mv = _ev3.get_output_pin5_mv

def get_output_state(*args):
  return _ev3.get_output_state(*args)
get_output_state = _ev3.get_output_state

def ev3_output_mode(*args):
  return _ev3.ev3_output_mode(*args)
ev3_output_mode = _ev3.ev3_output_mode

def get_output_mode_inx(*args):
  return _ev3.get_output_mode_inx(*args)
get_output_mode_inx = _ev3.get_output_mode_inx

def set_output_mode_inx(*args):
  return _ev3.set_output_mode_inx(*args)
set_output_mode_inx = _ev3.set_output_mode_inx
INPUT_DIR = _ev3.INPUT_DIR
INPUT__BASE_ = _ev3.INPUT__BASE_
INPUT_1 = _ev3.INPUT_1
INPUT_2 = _ev3.INPUT_2
INPUT_3 = _ev3.INPUT_3
INPUT_4 = _ev3.INPUT_4
INPUT__COUNT_ = _ev3.INPUT__COUNT_
INPUT_AUTO = _ev3.INPUT_AUTO
INPUT_EV3_ANALOG = _ev3.INPUT_EV3_ANALOG
INPUT_EV3_UART = _ev3.INPUT_EV3_UART
INPUT_NXT_ANALOG = _ev3.INPUT_NXT_ANALOG
INPUT_NXT_COLOR = _ev3.INPUT_NXT_COLOR
INPUT_NXT_I2C = _ev3.INPUT_NXT_I2C
INPUT_OTHER_UART = _ev3.INPUT_OTHER_UART
INPUT_RAW = _ev3.INPUT_RAW
INPUT_MODE__COUNT_ = _ev3.INPUT_MODE__COUNT_

def ev3_input_inx(*args):
  return _ev3.ev3_input_inx(*args)
ev3_input_inx = _ev3.ev3_input_inx

def ev3_input_name(*args):
  return _ev3.ev3_input_name(*args)
ev3_input_name = _ev3.ev3_input_name

def get_input_mode(*args):
  return _ev3.get_input_mode(*args)
get_input_mode = _ev3.get_input_mode

def set_input_mode(*args):
  return _ev3.set_input_mode(*args)
set_input_mode = _ev3.set_input_mode

def get_input_modes(*args):
  return _ev3.get_input_modes(*args)
get_input_modes = _ev3.get_input_modes

def get_input_pin1_mv(*args):
  return _ev3.get_input_pin1_mv(*args)
get_input_pin1_mv = _ev3.get_input_pin1_mv

def get_input_pin6_mv(*args):
  return _ev3.get_input_pin6_mv(*args)
get_input_pin6_mv = _ev3.get_input_pin6_mv

def get_input_state(*args):
  return _ev3.get_input_state(*args)
get_input_state = _ev3.get_input_state

def ev3_input_mode(*args):
  return _ev3.ev3_input_mode(*args)
ev3_input_mode = _ev3.ev3_input_mode

def get_input_mode_inx(*args):
  return _ev3.get_input_mode_inx(*args)
get_input_mode_inx = _ev3.get_input_mode_inx

def set_input_mode_inx(*args):
  return _ev3.set_input_mode_inx(*args)
set_input_mode_inx = _ev3.set_input_mode_inx
INPUT_MUX__NONE_ = _ev3.INPUT_MUX__NONE_
INPUT_MUX_1 = _ev3.INPUT_MUX_1
INPUT_MUX_2 = _ev3.INPUT_MUX_2
INPUT_MUX_3 = _ev3.INPUT_MUX_3
INPUT_MUX_4 = _ev3.INPUT_MUX_4
INPUT_MUX__BASE_ = _ev3.INPUT_MUX__BASE_
INPUT_MUX__COUNT_ = _ev3.INPUT_MUX__COUNT_
INPUT_MUX_ANALOG = _ev3.INPUT_MUX_ANALOG
INPUT_MUX_I2C = _ev3.INPUT_MUX_I2C
INPUT_MUX_MODE__COUNT_ = _ev3.INPUT_MUX_MODE__COUNT_

def nxt_input_mux_inx(*args):
  return _ev3.nxt_input_mux_inx(*args)
nxt_input_mux_inx = _ev3.nxt_input_mux_inx

def nxt_input_mux_name(*args):
  return _ev3.nxt_input_mux_name(*args)
nxt_input_mux_name = _ev3.nxt_input_mux_name

def get_input_mux_mode(*args):
  return _ev3.get_input_mux_mode(*args)
get_input_mux_mode = _ev3.get_input_mux_mode

def set_input_mux_mode(*args):
  return _ev3.set_input_mux_mode(*args)
set_input_mux_mode = _ev3.set_input_mux_mode

def get_input_mux_modes(*args):
  return _ev3.get_input_mux_modes(*args)
get_input_mux_modes = _ev3.get_input_mux_modes

def nxt_input_mux_mode(*args):
  return _ev3.nxt_input_mux_mode(*args)
nxt_input_mux_mode = _ev3.nxt_input_mux_mode

def get_input_mux_mode_inx(*args):
  return _ev3.get_input_mux_mode_inx(*args)
get_input_mux_mode_inx = _ev3.get_input_mux_mode_inx

def set_input_mux_mode_inx(*args):
  return _ev3.set_input_mux_mode_inx(*args)
set_input_mux_mode_inx = _ev3.set_input_mux_mode_inx
EV3_PORT__NONE_ = _ev3.EV3_PORT__NONE_

def ev3_port_inx(*args):
  return _ev3.ev3_port_inx(*args)
ev3_port_inx = _ev3.ev3_port_inx

def ev3_port_name(*args):
  return _ev3.ev3_port_name(*args)
ev3_port_name = _ev3.ev3_port_name
SENSOR_DIR = _ev3.SENSOR_DIR
class EV3_SENSOR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EV3_SENSOR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EV3_SENSOR, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type_inx"] = _ev3.EV3_SENSOR_type_inx_set
    __swig_getmethods__["type_inx"] = _ev3.EV3_SENSOR_type_inx_get
    if _newclass:type_inx = _swig_property(_ev3.EV3_SENSOR_type_inx_get, _ev3.EV3_SENSOR_type_inx_set)
    __swig_setmethods__["port"] = _ev3.EV3_SENSOR_port_set
    __swig_getmethods__["port"] = _ev3.EV3_SENSOR_port_get
    if _newclass:port = _swig_property(_ev3.EV3_SENSOR_port_get, _ev3.EV3_SENSOR_port_set)
    __swig_setmethods__["extport"] = _ev3.EV3_SENSOR_extport_set
    __swig_getmethods__["extport"] = _ev3.EV3_SENSOR_extport_get
    if _newclass:extport = _swig_property(_ev3.EV3_SENSOR_extport_get, _ev3.EV3_SENSOR_extport_set)
    __swig_setmethods__["addr"] = _ev3.EV3_SENSOR_addr_set
    __swig_getmethods__["addr"] = _ev3.EV3_SENSOR_addr_get
    if _newclass:addr = _swig_property(_ev3.EV3_SENSOR_addr_get, _ev3.EV3_SENSOR_addr_set)
    def __init__(self): 
        this = _ev3.new_EV3_SENSOR()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ev3.delete_EV3_SENSOR
    __del__ = lambda self : None;
EV3_SENSOR_swigregister = _ev3.EV3_SENSOR_swigregister
EV3_SENSOR_swigregister(EV3_SENSOR)
ev3 = _ev3.ev3
LIT_COLOR = ev3.LIT_COLOR

SENSOR_DESC__LIMIT_ = _ev3.SENSOR_DESC__LIMIT_
SENSOR__NONE_ = _ev3.SENSOR__NONE_
SENSOR_TYPE__NONE_ = _ev3.SENSOR_TYPE__NONE_
EV3_ANALOG_XX = _ev3.EV3_ANALOG_XX
NXT_ANALOG = _ev3.NXT_ANALOG
HT_NXT_COLOR = _ev3.HT_NXT_COLOR
HT_NXT_ANGLE = _ev3.HT_NXT_ANGLE
HT_NXT_ACCEL = _ev3.HT_NXT_ACCEL
HT_NXT_BAROMETRIC = _ev3.HT_NXT_BAROMETRIC
HT_NXT_COLOR_V2 = _ev3.HT_NXT_COLOR_V2
HT_NXT_EOPD = _ev3.HT_NXT_EOPD
HT_NXT_FORCE = _ev3.HT_NXT_FORCE
HT_NXT_GYRO = _ev3.HT_NXT_GYRO
HT_NXT_IR_LINK = _ev3.HT_NXT_IR_LINK
HT_NXT_IR_RECEIVER = _ev3.HT_NXT_IR_RECEIVER
HT_NXT_PIR = _ev3.HT_NXT_PIR
HT_NXT_COMPASS = _ev3.HT_NXT_COMPASS
HT_NXT_MAG = _ev3.HT_NXT_MAG
HT_NXT_IR_SEEKER_V2 = _ev3.HT_NXT_IR_SEEKER_V2
HT_NXT_SMUX = _ev3.HT_NXT_SMUX
HT_SUPER_PRO = _ev3.HT_SUPER_PRO
EV3_UART_30 = _ev3.EV3_UART_30
EV3_UART_32 = _ev3.EV3_UART_32
EV3_UART_29 = _ev3.EV3_UART_29
LEGO_EV3_TOUCH = _ev3.LEGO_EV3_TOUCH
EV3_UART_33 = _ev3.EV3_UART_33
WEDO_MOTION = _ev3.WEDO_MOTION
WEDO_TILT = _ev3.WEDO_TILT
LEGO_POWER_STORAGE = _ev3.LEGO_POWER_STORAGE
LEGO_NXT_TOUCH = _ev3.LEGO_NXT_TOUCH
LEGO_NXT_LIGHT = _ev3.LEGO_NXT_LIGHT
LEGO_NXT_SOUND = _ev3.LEGO_NXT_SOUND
LEGO_NXT_US = _ev3.LEGO_NXT_US
MI_XG1300L = _ev3.MI_XG1300L
MS_ABSOLUTE_IMU = _ev3.MS_ABSOLUTE_IMU
MS_ANGLE = _ev3.MS_ANGLE
MS_LIGHT_ARRAY = _ev3.MS_LIGHT_ARRAY
MS_8CH_SERVO = _ev3.MS_8CH_SERVO
MS_NXT_TOUCH_MUX = _ev3.MS_NXT_TOUCH_MUX
SENSOR_TYPE__COUNT_ = _ev3.SENSOR_TYPE__COUNT_

def get_sensor_bin_data(*args):
  return _ev3.get_sensor_bin_data(*args)
get_sensor_bin_data = _ev3.get_sensor_bin_data

def set_sensor_bin_data(*args):
  return _ev3.set_sensor_bin_data(*args)
set_sensor_bin_data = _ev3.set_sensor_bin_data

def get_sensor_bin_data_format(*args):
  return _ev3.get_sensor_bin_data_format(*args)
get_sensor_bin_data_format = _ev3.get_sensor_bin_data_format

def set_sensor_command(*args):
  return _ev3.set_sensor_command(*args)
set_sensor_command = _ev3.set_sensor_command

def get_sensor_commands(*args):
  return _ev3.get_sensor_commands(*args)
get_sensor_commands = _ev3.get_sensor_commands

def get_sensor_dp(*args):
  return _ev3.get_sensor_dp(*args)
get_sensor_dp = _ev3.get_sensor_dp

def get_sensor_fw_version(*args):
  return _ev3.get_sensor_fw_version(*args)
get_sensor_fw_version = _ev3.get_sensor_fw_version

def get_sensor_address(*args):
  return _ev3.get_sensor_address(*args)
get_sensor_address = _ev3.get_sensor_address

def get_sensor_mode(*args):
  return _ev3.get_sensor_mode(*args)
get_sensor_mode = _ev3.get_sensor_mode

def set_sensor_mode(*args):
  return _ev3.set_sensor_mode(*args)
set_sensor_mode = _ev3.set_sensor_mode

def get_sensor_modes(*args):
  return _ev3.get_sensor_modes(*args)
get_sensor_modes = _ev3.get_sensor_modes

def get_sensor_name(*args):
  return _ev3.get_sensor_name(*args)
get_sensor_name = _ev3.get_sensor_name

def get_sensor_num_values(*args):
  return _ev3.get_sensor_num_values(*args)
get_sensor_num_values = _ev3.get_sensor_num_values

def get_sensor_poll_ms(*args):
  return _ev3.get_sensor_poll_ms(*args)
get_sensor_poll_ms = _ev3.get_sensor_poll_ms

def set_sensor_poll_ms(*args):
  return _ev3.set_sensor_poll_ms(*args)
set_sensor_poll_ms = _ev3.set_sensor_poll_ms

def get_sensor_port_name(*args):
  return _ev3.get_sensor_port_name(*args)
get_sensor_port_name = _ev3.get_sensor_port_name

def get_sensor_units(*args):
  return _ev3.get_sensor_units(*args)
get_sensor_units = _ev3.get_sensor_units

def get_sensor_value0(*args):
  return _ev3.get_sensor_value0(*args)
get_sensor_value0 = _ev3.get_sensor_value0

def get_sensor_value1(*args):
  return _ev3.get_sensor_value1(*args)
get_sensor_value1 = _ev3.get_sensor_value1

def get_sensor_value2(*args):
  return _ev3.get_sensor_value2(*args)
get_sensor_value2 = _ev3.get_sensor_value2

def get_sensor_value3(*args):
  return _ev3.get_sensor_value3(*args)
get_sensor_value3 = _ev3.get_sensor_value3

def get_sensor_value4(*args):
  return _ev3.get_sensor_value4(*args)
get_sensor_value4 = _ev3.get_sensor_value4

def get_sensor_value5(*args):
  return _ev3.get_sensor_value5(*args)
get_sensor_value5 = _ev3.get_sensor_value5

def get_sensor_value6(*args):
  return _ev3.get_sensor_value6(*args)
get_sensor_value6 = _ev3.get_sensor_value6

def get_sensor_value7(*args):
  return _ev3.get_sensor_value7(*args)
get_sensor_value7 = _ev3.get_sensor_value7

def get_sensor_value(*args):
  return _ev3.get_sensor_value(*args)
get_sensor_value = _ev3.get_sensor_value

def ev3_sensor_type(*args):
  return _ev3.ev3_sensor_type(*args)
ev3_sensor_type = _ev3.ev3_sensor_type

def get_sensor_type_inx(*args):
  return _ev3.get_sensor_type_inx(*args)
get_sensor_type_inx = _ev3.get_sensor_type_inx

def get_sensor_port_inx(*args):
  return _ev3.get_sensor_port_inx(*args)
get_sensor_port_inx = _ev3.get_sensor_port_inx

def ev3_sensor_desc(*args):
  return _ev3.ev3_sensor_desc(*args)
ev3_sensor_desc = _ev3.ev3_sensor_desc

def ev3_sensor_desc_type_inx(*args):
  return _ev3.ev3_sensor_desc_type_inx(*args)
ev3_sensor_desc_type_inx = _ev3.ev3_sensor_desc_type_inx

def ev3_sensor_desc_port(*args):
  return _ev3.ev3_sensor_desc_port(*args)
ev3_sensor_desc_port = _ev3.ev3_sensor_desc_port

def ev3_sensor_desc_extport(*args):
  return _ev3.ev3_sensor_desc_extport(*args)
ev3_sensor_desc_extport = _ev3.ev3_sensor_desc_extport

def ev3_sensor_desc_addr(*args):
  return _ev3.ev3_sensor_desc_addr(*args)
ev3_sensor_desc_addr = _ev3.ev3_sensor_desc_addr

def ev3_search_sensor(*args):
  return _ev3.ev3_search_sensor(*args)
ev3_search_sensor = _ev3.ev3_search_sensor

def ev3_search_sensor_plugged_in(*args):
  return _ev3.ev3_search_sensor_plugged_in(*args)
ev3_search_sensor_plugged_in = _ev3.ev3_search_sensor_plugged_in

def ev3_sensor_init():
  return _ev3.ev3_sensor_init()
ev3_sensor_init = _ev3.ev3_sensor_init
TACHO_DIR = _ev3.TACHO_DIR
class EV3_TACHO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EV3_TACHO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EV3_TACHO, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type_inx"] = _ev3.EV3_TACHO_type_inx_set
    __swig_getmethods__["type_inx"] = _ev3.EV3_TACHO_type_inx_get
    if _newclass:type_inx = _swig_property(_ev3.EV3_TACHO_type_inx_get, _ev3.EV3_TACHO_type_inx_set)
    __swig_setmethods__["port"] = _ev3.EV3_TACHO_port_set
    __swig_getmethods__["port"] = _ev3.EV3_TACHO_port_get
    if _newclass:port = _swig_property(_ev3.EV3_TACHO_port_get, _ev3.EV3_TACHO_port_set)
    __swig_setmethods__["extport"] = _ev3.EV3_TACHO_extport_set
    __swig_getmethods__["extport"] = _ev3.EV3_TACHO_extport_get
    if _newclass:extport = _swig_property(_ev3.EV3_TACHO_extport_get, _ev3.EV3_TACHO_extport_set)
    def __init__(self): 
        this = _ev3.new_EV3_TACHO()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ev3.delete_EV3_TACHO
    __del__ = lambda self : None;
EV3_TACHO_swigregister = _ev3.EV3_TACHO_swigregister
EV3_TACHO_swigregister(EV3_TACHO)

TACHO_DESC__LIMIT_ = _ev3.TACHO_DESC__LIMIT_
TACHO__NONE_ = _ev3.TACHO__NONE_
TACHO_TYPE__NONE_ = _ev3.TACHO_TYPE__NONE_
TACHO = _ev3.TACHO
MINITACHO = _ev3.MINITACHO
TACHO_TYPE__COUNT_ = _ev3.TACHO_TYPE__COUNT_

def get_tacho_duty_cycle(*args):
  return _ev3.get_tacho_duty_cycle(*args)
get_tacho_duty_cycle = _ev3.get_tacho_duty_cycle

def get_tacho_duty_cycle_sp(*args):
  return _ev3.get_tacho_duty_cycle_sp(*args)
get_tacho_duty_cycle_sp = _ev3.get_tacho_duty_cycle_sp

def set_tacho_duty_cycle_sp(*args):
  return _ev3.set_tacho_duty_cycle_sp(*args)
set_tacho_duty_cycle_sp = _ev3.set_tacho_duty_cycle_sp

def get_tacho_polarity_mode(*args):
  return _ev3.get_tacho_polarity_mode(*args)
get_tacho_polarity_mode = _ev3.get_tacho_polarity_mode

def get_tacho_port_name(*args):
  return _ev3.get_tacho_port_name(*args)
get_tacho_port_name = _ev3.get_tacho_port_name

def get_tacho_position(*args):
  return _ev3.get_tacho_position(*args)
get_tacho_position = _ev3.get_tacho_position

def set_tacho_position(*args):
  return _ev3.set_tacho_position(*args)
set_tacho_position = _ev3.set_tacho_position

def get_tacho_position_mode(*args):
  return _ev3.get_tacho_position_mode(*args)
get_tacho_position_mode = _ev3.get_tacho_position_mode

def set_tacho_position_mode(*args):
  return _ev3.set_tacho_position_mode(*args)
set_tacho_position_mode = _ev3.set_tacho_position_mode

def get_tacho_position_sp(*args):
  return _ev3.get_tacho_position_sp(*args)
get_tacho_position_sp = _ev3.get_tacho_position_sp

def set_tacho_position_sp(*args):
  return _ev3.set_tacho_position_sp(*args)
set_tacho_position_sp = _ev3.set_tacho_position_sp

def get_tacho_pulses_per_second(*args):
  return _ev3.get_tacho_pulses_per_second(*args)
get_tacho_pulses_per_second = _ev3.get_tacho_pulses_per_second

def get_tacho_pulses_per_second_sp(*args):
  return _ev3.get_tacho_pulses_per_second_sp(*args)
get_tacho_pulses_per_second_sp = _ev3.get_tacho_pulses_per_second_sp

def set_tacho_pulses_per_second_sp(*args):
  return _ev3.set_tacho_pulses_per_second_sp(*args)
set_tacho_pulses_per_second_sp = _ev3.set_tacho_pulses_per_second_sp

def get_tacho_ramp_down_sp(*args):
  return _ev3.get_tacho_ramp_down_sp(*args)
get_tacho_ramp_down_sp = _ev3.get_tacho_ramp_down_sp

def set_tacho_ramp_down_sp(*args):
  return _ev3.set_tacho_ramp_down_sp(*args)
set_tacho_ramp_down_sp = _ev3.set_tacho_ramp_down_sp

def get_tacho_ramp_up_sp(*args):
  return _ev3.get_tacho_ramp_up_sp(*args)
get_tacho_ramp_up_sp = _ev3.get_tacho_ramp_up_sp

def set_tacho_ramp_up_sp(*args):
  return _ev3.set_tacho_ramp_up_sp(*args)
set_tacho_ramp_up_sp = _ev3.set_tacho_ramp_up_sp

def get_tacho_regulation_mode(*args):
  return _ev3.get_tacho_regulation_mode(*args)
get_tacho_regulation_mode = _ev3.get_tacho_regulation_mode

def set_tacho_regulation_mode(*args):
  return _ev3.set_tacho_regulation_mode(*args)
set_tacho_regulation_mode = _ev3.set_tacho_regulation_mode

def set_tacho_reset(*args):
  return _ev3.set_tacho_reset(*args)
set_tacho_reset = _ev3.set_tacho_reset

def get_tacho_run(*args):
  return _ev3.get_tacho_run(*args)
get_tacho_run = _ev3.get_tacho_run

def set_tacho_run(*args):
  return _ev3.set_tacho_run(*args)
set_tacho_run = _ev3.set_tacho_run

def get_tacho_run_mode(*args):
  return _ev3.get_tacho_run_mode(*args)
get_tacho_run_mode = _ev3.get_tacho_run_mode

def set_tacho_run_mode(*args):
  return _ev3.set_tacho_run_mode(*args)
set_tacho_run_mode = _ev3.set_tacho_run_mode

def get_tacho_speed_regulation_D(*args):
  return _ev3.get_tacho_speed_regulation_D(*args)
get_tacho_speed_regulation_D = _ev3.get_tacho_speed_regulation_D

def set_tacho_speed_regulation_D(*args):
  return _ev3.set_tacho_speed_regulation_D(*args)
set_tacho_speed_regulation_D = _ev3.set_tacho_speed_regulation_D

def get_tacho_speed_regulation_I(*args):
  return _ev3.get_tacho_speed_regulation_I(*args)
get_tacho_speed_regulation_I = _ev3.get_tacho_speed_regulation_I

def set_tacho_speed_regulation_I(*args):
  return _ev3.set_tacho_speed_regulation_I(*args)
set_tacho_speed_regulation_I = _ev3.set_tacho_speed_regulation_I

def get_tacho_speed_regulation_K(*args):
  return _ev3.get_tacho_speed_regulation_K(*args)
get_tacho_speed_regulation_K = _ev3.get_tacho_speed_regulation_K

def set_tacho_speed_regulation_K(*args):
  return _ev3.set_tacho_speed_regulation_K(*args)
set_tacho_speed_regulation_K = _ev3.set_tacho_speed_regulation_K

def get_tacho_speed_regulation_P(*args):
  return _ev3.get_tacho_speed_regulation_P(*args)
get_tacho_speed_regulation_P = _ev3.get_tacho_speed_regulation_P

def set_tacho_speed_regulation_P(*args):
  return _ev3.set_tacho_speed_regulation_P(*args)
set_tacho_speed_regulation_P = _ev3.set_tacho_speed_regulation_P

def get_tacho_state(*args):
  return _ev3.get_tacho_state(*args)
get_tacho_state = _ev3.get_tacho_state

def get_tacho_stop_mode(*args):
  return _ev3.get_tacho_stop_mode(*args)
get_tacho_stop_mode = _ev3.get_tacho_stop_mode

def set_tacho_stop_mode(*args):
  return _ev3.set_tacho_stop_mode(*args)
set_tacho_stop_mode = _ev3.set_tacho_stop_mode

def get_tacho_stop_modes(*args):
  return _ev3.get_tacho_stop_modes(*args)
get_tacho_stop_modes = _ev3.get_tacho_stop_modes

def get_tacho_time_sp(*args):
  return _ev3.get_tacho_time_sp(*args)
get_tacho_time_sp = _ev3.get_tacho_time_sp

def set_tacho_time_sp(*args):
  return _ev3.set_tacho_time_sp(*args)
set_tacho_time_sp = _ev3.set_tacho_time_sp

def get_tacho_type(*args):
  return _ev3.get_tacho_type(*args)
get_tacho_type = _ev3.get_tacho_type

def ev3_tacho_type(*args):
  return _ev3.ev3_tacho_type(*args)
ev3_tacho_type = _ev3.ev3_tacho_type

def get_tacho_type_inx(*args):
  return _ev3.get_tacho_type_inx(*args)
get_tacho_type_inx = _ev3.get_tacho_type_inx

def get_tacho_port_inx(*args):
  return _ev3.get_tacho_port_inx(*args)
get_tacho_port_inx = _ev3.get_tacho_port_inx

def ev3_tacho_desc(*args):
  return _ev3.ev3_tacho_desc(*args)
ev3_tacho_desc = _ev3.ev3_tacho_desc

def ev3_tacho_desc_type_inx(*args):
  return _ev3.ev3_tacho_desc_type_inx(*args)
ev3_tacho_desc_type_inx = _ev3.ev3_tacho_desc_type_inx

def ev3_tacho_desc_port(*args):
  return _ev3.ev3_tacho_desc_port(*args)
ev3_tacho_desc_port = _ev3.ev3_tacho_desc_port

def ev3_tacho_desc_extport(*args):
  return _ev3.ev3_tacho_desc_extport(*args)
ev3_tacho_desc_extport = _ev3.ev3_tacho_desc_extport

def ev3_search_tacho(*args):
  return _ev3.ev3_search_tacho(*args)
ev3_search_tacho = _ev3.ev3_search_tacho

def ev3_search_tacho_plugged_in(*args):
  return _ev3.ev3_search_tacho_plugged_in(*args)
ev3_search_tacho_plugged_in = _ev3.ev3_search_tacho_plugged_in

def ev3_tacho_init():
  return _ev3.ev3_tacho_init()
ev3_tacho_init = _ev3.ev3_tacho_init
DC_DIR = _ev3.DC_DIR
class EV3_DC(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EV3_DC, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EV3_DC, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type_inx"] = _ev3.EV3_DC_type_inx_set
    __swig_getmethods__["type_inx"] = _ev3.EV3_DC_type_inx_get
    if _newclass:type_inx = _swig_property(_ev3.EV3_DC_type_inx_get, _ev3.EV3_DC_type_inx_set)
    __swig_setmethods__["port"] = _ev3.EV3_DC_port_set
    __swig_getmethods__["port"] = _ev3.EV3_DC_port_get
    if _newclass:port = _swig_property(_ev3.EV3_DC_port_get, _ev3.EV3_DC_port_set)
    __swig_setmethods__["extport"] = _ev3.EV3_DC_extport_set
    __swig_getmethods__["extport"] = _ev3.EV3_DC_extport_get
    if _newclass:extport = _swig_property(_ev3.EV3_DC_extport_get, _ev3.EV3_DC_extport_set)
    def __init__(self): 
        this = _ev3.new_EV3_DC()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ev3.delete_EV3_DC
    __del__ = lambda self : None;
EV3_DC_swigregister = _ev3.EV3_DC_swigregister
EV3_DC_swigregister(EV3_DC)

DC_DESC__LIMIT_ = _ev3.DC_DESC__LIMIT_
DC__NONE_ = _ev3.DC__NONE_
DC_TYPE__NONE_ = _ev3.DC_TYPE__NONE_
RCX_MOTOR = _ev3.RCX_MOTOR
DC_TYPE__COUNT_ = _ev3.DC_TYPE__COUNT_

def get_dc_command(*args):
  return _ev3.get_dc_command(*args)
get_dc_command = _ev3.get_dc_command

def set_dc_command(*args):
  return _ev3.set_dc_command(*args)
set_dc_command = _ev3.set_dc_command

def get_dc_commands(*args):
  return _ev3.get_dc_commands(*args)
get_dc_commands = _ev3.get_dc_commands

def get_dc_duty_cycle(*args):
  return _ev3.get_dc_duty_cycle(*args)
get_dc_duty_cycle = _ev3.get_dc_duty_cycle

def get_dc_duty_cycle_sp(*args):
  return _ev3.get_dc_duty_cycle_sp(*args)
get_dc_duty_cycle_sp = _ev3.get_dc_duty_cycle_sp

def set_dc_duty_cycle_sp(*args):
  return _ev3.set_dc_duty_cycle_sp(*args)
set_dc_duty_cycle_sp = _ev3.set_dc_duty_cycle_sp

def get_dc_name(*args):
  return _ev3.get_dc_name(*args)
get_dc_name = _ev3.get_dc_name

def get_dc_polarity(*args):
  return _ev3.get_dc_polarity(*args)
get_dc_polarity = _ev3.get_dc_polarity

def set_dc_polarity(*args):
  return _ev3.set_dc_polarity(*args)
set_dc_polarity = _ev3.set_dc_polarity

def get_dc_port_name(*args):
  return _ev3.get_dc_port_name(*args)
get_dc_port_name = _ev3.get_dc_port_name

def get_dc_ramp_down_ms(*args):
  return _ev3.get_dc_ramp_down_ms(*args)
get_dc_ramp_down_ms = _ev3.get_dc_ramp_down_ms

def set_dc_ramp_down_ms(*args):
  return _ev3.set_dc_ramp_down_ms(*args)
set_dc_ramp_down_ms = _ev3.set_dc_ramp_down_ms

def get_dc_ramp_up_ms(*args):
  return _ev3.get_dc_ramp_up_ms(*args)
get_dc_ramp_up_ms = _ev3.get_dc_ramp_up_ms

def set_dc_ramp_up_ms(*args):
  return _ev3.set_dc_ramp_up_ms(*args)
set_dc_ramp_up_ms = _ev3.set_dc_ramp_up_ms

def ev3_dc_type(*args):
  return _ev3.ev3_dc_type(*args)
ev3_dc_type = _ev3.ev3_dc_type

def get_dc_type_inx(*args):
  return _ev3.get_dc_type_inx(*args)
get_dc_type_inx = _ev3.get_dc_type_inx

def get_dc_port_inx(*args):
  return _ev3.get_dc_port_inx(*args)
get_dc_port_inx = _ev3.get_dc_port_inx

def ev3_dc_desc(*args):
  return _ev3.ev3_dc_desc(*args)
ev3_dc_desc = _ev3.ev3_dc_desc

def ev3_dc_desc_type_inx(*args):
  return _ev3.ev3_dc_desc_type_inx(*args)
ev3_dc_desc_type_inx = _ev3.ev3_dc_desc_type_inx

def ev3_dc_desc_port(*args):
  return _ev3.ev3_dc_desc_port(*args)
ev3_dc_desc_port = _ev3.ev3_dc_desc_port

def ev3_dc_desc_extport(*args):
  return _ev3.ev3_dc_desc_extport(*args)
ev3_dc_desc_extport = _ev3.ev3_dc_desc_extport

def ev3_search_dc(*args):
  return _ev3.ev3_search_dc(*args)
ev3_search_dc = _ev3.ev3_search_dc

def ev3_search_dc_plugged_in(*args):
  return _ev3.ev3_search_dc_plugged_in(*args)
ev3_search_dc_plugged_in = _ev3.ev3_search_dc_plugged_in

def ev3_dc_init():
  return _ev3.ev3_dc_init()
ev3_dc_init = _ev3.ev3_dc_init
SERVO_DIR = _ev3.SERVO_DIR
class EV3_SERVO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EV3_SERVO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EV3_SERVO, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type_inx"] = _ev3.EV3_SERVO_type_inx_set
    __swig_getmethods__["type_inx"] = _ev3.EV3_SERVO_type_inx_get
    if _newclass:type_inx = _swig_property(_ev3.EV3_SERVO_type_inx_get, _ev3.EV3_SERVO_type_inx_set)
    __swig_setmethods__["port"] = _ev3.EV3_SERVO_port_set
    __swig_getmethods__["port"] = _ev3.EV3_SERVO_port_get
    if _newclass:port = _swig_property(_ev3.EV3_SERVO_port_get, _ev3.EV3_SERVO_port_set)
    __swig_setmethods__["extport"] = _ev3.EV3_SERVO_extport_set
    __swig_getmethods__["extport"] = _ev3.EV3_SERVO_extport_get
    if _newclass:extport = _swig_property(_ev3.EV3_SERVO_extport_get, _ev3.EV3_SERVO_extport_set)
    __swig_setmethods__["addr"] = _ev3.EV3_SERVO_addr_set
    __swig_getmethods__["addr"] = _ev3.EV3_SERVO_addr_get
    if _newclass:addr = _swig_property(_ev3.EV3_SERVO_addr_get, _ev3.EV3_SERVO_addr_set)
    def __init__(self): 
        this = _ev3.new_EV3_SERVO()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ev3.delete_EV3_SERVO
    __del__ = lambda self : None;
EV3_SERVO_swigregister = _ev3.EV3_SERVO_swigregister
EV3_SERVO_swigregister(EV3_SERVO)

SERVO_DESC__LIMIT_ = _ev3.SERVO_DESC__LIMIT_
SERVO__NONE_ = _ev3.SERVO__NONE_
SERVO_TYPE__NONE_ = _ev3.SERVO_TYPE__NONE_
SERVO_MOTOR = _ev3.SERVO_MOTOR
SERVO_TYPE__COUNT_ = _ev3.SERVO_TYPE__COUNT_

def get_servo_command(*args):
  return _ev3.get_servo_command(*args)
get_servo_command = _ev3.get_servo_command

def set_servo_command(*args):
  return _ev3.set_servo_command(*args)
set_servo_command = _ev3.set_servo_command

def get_servo_max_pulse_ms(*args):
  return _ev3.get_servo_max_pulse_ms(*args)
get_servo_max_pulse_ms = _ev3.get_servo_max_pulse_ms

def set_servo_max_pulse_ms(*args):
  return _ev3.set_servo_max_pulse_ms(*args)
set_servo_max_pulse_ms = _ev3.set_servo_max_pulse_ms

def get_servo_mid_pulse_ms(*args):
  return _ev3.get_servo_mid_pulse_ms(*args)
get_servo_mid_pulse_ms = _ev3.get_servo_mid_pulse_ms

def set_servo_mid_pulse_ms(*args):
  return _ev3.set_servo_mid_pulse_ms(*args)
set_servo_mid_pulse_ms = _ev3.set_servo_mid_pulse_ms

def get_servo_min_pulse_ms(*args):
  return _ev3.get_servo_min_pulse_ms(*args)
get_servo_min_pulse_ms = _ev3.get_servo_min_pulse_ms

def set_servo_min_pulse_ms(*args):
  return _ev3.set_servo_min_pulse_ms(*args)
set_servo_min_pulse_ms = _ev3.set_servo_min_pulse_ms

def get_servo_name(*args):
  return _ev3.get_servo_name(*args)
get_servo_name = _ev3.get_servo_name

def get_servo_polarity(*args):
  return _ev3.get_servo_polarity(*args)
get_servo_polarity = _ev3.get_servo_polarity

def set_servo_polarity(*args):
  return _ev3.set_servo_polarity(*args)
set_servo_polarity = _ev3.set_servo_polarity

def get_servo_port_name(*args):
  return _ev3.get_servo_port_name(*args)
get_servo_port_name = _ev3.get_servo_port_name

def get_servo_position(*args):
  return _ev3.get_servo_position(*args)
get_servo_position = _ev3.get_servo_position

def set_servo_position(*args):
  return _ev3.set_servo_position(*args)
set_servo_position = _ev3.set_servo_position

def get_servo_rate(*args):
  return _ev3.get_servo_rate(*args)
get_servo_rate = _ev3.get_servo_rate

def set_servo_rate(*args):
  return _ev3.set_servo_rate(*args)
set_servo_rate = _ev3.set_servo_rate

def ev3_servo_type(*args):
  return _ev3.ev3_servo_type(*args)
ev3_servo_type = _ev3.ev3_servo_type

def get_servo_type_inx(*args):
  return _ev3.get_servo_type_inx(*args)
get_servo_type_inx = _ev3.get_servo_type_inx

def get_servo_port_inx(*args):
  return _ev3.get_servo_port_inx(*args)
get_servo_port_inx = _ev3.get_servo_port_inx

def ev3_servo_desc(*args):
  return _ev3.ev3_servo_desc(*args)
ev3_servo_desc = _ev3.ev3_servo_desc

def ev3_servo_desc_type_inx(*args):
  return _ev3.ev3_servo_desc_type_inx(*args)
ev3_servo_desc_type_inx = _ev3.ev3_servo_desc_type_inx

def ev3_servo_desc_port(*args):
  return _ev3.ev3_servo_desc_port(*args)
ev3_servo_desc_port = _ev3.ev3_servo_desc_port

def ev3_servo_desc_extport(*args):
  return _ev3.ev3_servo_desc_extport(*args)
ev3_servo_desc_extport = _ev3.ev3_servo_desc_extport

def ev3_servo_desc_addr(*args):
  return _ev3.ev3_servo_desc_addr(*args)
ev3_servo_desc_addr = _ev3.ev3_servo_desc_addr

def ev3_search_servo(*args):
  return _ev3.ev3_search_servo(*args)
ev3_search_servo = _ev3.ev3_search_servo

def ev3_search_servo_plugged_in(*args):
  return _ev3.ev3_search_servo_plugged_in(*args)
ev3_search_servo_plugged_in = _ev3.ev3_search_servo_plugged_in

def ev3_servo_init():
  return _ev3.ev3_servo_init()
ev3_servo_init = _ev3.ev3_servo_init

def get_servo_address(*args):
  return _ev3.get_servo_address(*args)
get_servo_address = _ev3.get_servo_address

def ev3_servo_port_name(*args):
  return _ev3.ev3_servo_port_name(*args)
ev3_servo_port_name = _ev3.ev3_servo_port_name
NXT_ANALOG_HOST_DIR = _ev3.NXT_ANALOG_HOST_DIR

def get_nxt_analog_host_device_type(*args):
  return _ev3.get_nxt_analog_host_device_type(*args)
get_nxt_analog_host_device_type = _ev3.get_nxt_analog_host_device_type

def get_nxt_analog_host_port_name(*args):
  return _ev3.get_nxt_analog_host_port_name(*args)
get_nxt_analog_host_port_name = _ev3.get_nxt_analog_host_port_name

def set_nxt_analog_host_set_sensor(*args):
  return _ev3.set_nxt_analog_host_set_sensor(*args)
set_nxt_analog_host_set_sensor = _ev3.set_nxt_analog_host_set_sensor
# This file is compatible with both classic and new-style classes.


