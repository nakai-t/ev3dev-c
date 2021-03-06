# -*- coding: utf-8 -*-
#pylint: skip-file

from time import sleep
import sys
from ev3dev import *

if __name__ == '__main__':
    if ev3_init() < 1: sys.exit( 1 )

    print '*** ( EV3 ) Hello! ***'

    port = OUTPUT_B
    print 'Set mode of the EV3 output port...'
    set_output_mode_inx( port, OUTPUT_RCX_MOTOR )
    ok, state = get_output_state( port, 256 )
    if ok:
        print '%s: %s' % ( ev3_output_name( port ), state )

    ev3_dc_init()

    print 'Found DC motors:'
    for i in range( DC_DESC__LIMIT_ ):
        type_inx = ev3_dc_desc_type_inx( i )
        if type_inx != DC_TYPE__NONE_:
            print '  type =', ev3_dc_type( type_inx )
            print '  port =', ev3_port_name( ev3_dc_desc_port( i ), ev3_dc_desc_extport( i ))

    ok, sn = ev3_search_dc( RCX_MOTOR )
    if ok:
        print 'DC motor is found, run for 5 sec...'
        set_dc_ramp_up_ms( sn, 2000 )
        set_dc_duty_cycle( sn, 100 )
        set_dc_command( sn, 'run' )
        ok, cmd = get_dc_command( sn, 256 )
        if ok:
            print 'command:', cmd
        sleep( 5.0 )
        set_dc_command( sn, 'coast' )
        ok, cmd = get_dc_command( sn, 256 )
        if ok:
            print 'command:', cmd
    else:
        print 'DC motor is NOT found'

    print 'Reset mode of the EV3 output port...'
    set_output_mode_inx( port, OUTPUT_AUTO )
    ok, state = get_output_state( port, 256 )
    if ok:
        print '%s: %s' % ( ev3_output_name( port ), state )

    ev3_uninit()
    print '*** ( EV3 ) Bye! ***'
