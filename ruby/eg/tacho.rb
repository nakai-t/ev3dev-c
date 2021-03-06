# -*- coding: utf-8 -*-

#FIXME: not the best way to import the library
$LOAD_PATH << if ENV[ 'OS' ] == 'Windows_NT' then '../mingw' else '..' end
require 'ev3'
include Ev3

if __FILE__ == $0
  puts "EV3_BRICK = #{EV3_BRICK}"

  if EV3_BRICK == 0
    # Disable auto-detection of the brick (you have to set the correct address below)
    Ev3.brick_addr = '192.168.0.244'
  end
  if ev3_init() == -1 then exit( 1 ) end

  if EV3_BRICK == 0
    puts "The EV3 brick auto-detection is DISABLED, waiting #{Ev3.brick_addr} online..."
    $stdout.flush
  end

  while ev3_tacho_init() < 1 do sleep( 1.0 ) end

  puts '*** ( EV3 ) Hello! ***'

  puts 'Found tacho motors:'
  TACHO_DESC__LIMIT_.times do |i|
    type_inx = ev3_tacho_desc_type_inx( i )
    if type_inx != TACHO_TYPE__NONE_
      _type = ev3_tacho_type( type_inx )
      puts "  type = #{_type}"
      port_name = ev3_port_name( ev3_tacho_desc_port( i ), ev3_tacho_desc_extport( i ))
      puts "  port = #{port_name}"
    end
  end
  ok, sn = ev3_search_tacho( MINITACHO )
  if ok
    puts 'MINITACHO motor is found, run for 5 sec...'
    set_tacho_regulation_mode( sn, 'off' )
    set_tacho_run_mode( sn, 'time' )
    set_tacho_stop_mode( sn, 'brake' )
    set_tacho_duty_cycle_sp( sn, 100 )
    set_tacho_time_sp( sn, 5000 )
    set_tacho_ramp_up_sp( sn, 2000 )
    set_tacho_ramp_down_sp( sn, 2000 )
    set_tacho_run( sn, true )
  else
    puts 'MINITACHO motor is NOT found'
  end
  ev3_uninit()
  puts '*** ( EV3 ) Bye! ***'
end
