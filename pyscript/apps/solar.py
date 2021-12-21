
###############
# Configuration
###############
POWER_METER = "sensor.power_meter"
PRODUCTION = "sensor.production"
CONSUMPTION = "sensor.casa_consumo"



#######################
# Calculate consumption
#######################
@state_trigger(f"{POWER_METER} != '9999'")
def calculate_consumption(value=None):
    load = int(state.get(PRODUCTION)) - int(value)
    state.set("sensor.casa_consumo", value=load)




CONF_APPS = "apps"
CONF_SOLAR = "solar"
CONF_POWER_METER = "power_meter"
CONF_ENTITY_ID = "entity_id"
CONF_BOILER = "boiler"
CONF_START_TIME = "start_time"
CONF_STOP_TIME = "stop_time"
CONF_CONDITIONS = "conditions"


########
# Boiler
########
def boiler_control(do_start, entity_boiler, conditions):
    pass


##########
# Startup
##########
@time_trigger('startup')
def load():
    if CONF_SOLAR not in pyscript.config[CONF_APPS]:
        return
    solar = pyscript.config[CONF_APPS][CONF_SOLAR]
    entity_power_meter = solar[CONF_POWER_METER][CONF_ENTITY_ID]
    
    log.debug(f"JAN main -> called")

    # Check for boiler
#    entity_boiler = solar[CONF_BOILER][CONF_ENTITY_ID]

#    @time_trigger(f"once({solar[CONF_BOILER][CONF_START_TIME]})")
#    def inner_helper_boiler_start():
#       boiler_control(True, entity_boiler, solar[CONF_BOILER][CONDITIONS])

#    @time_trigger(f"once({solar[CONF_BOILER][CONF_STOP_TIME]})")
#    def inner_helper_boiler_stop():
#       boiler_control(False, entity_boiler, solar[CONF_BOILER][CONDITIONS])



#  consumers:
#    - entity_id: "switch.onvis_s3eu_519a30"
#      load: 2200
#    - entity_id: "switch.onvis_s3eu_51c26c"
#      load: 1000
#  optimizer:
#    entity_id: "switch.optimizer"
#    cut_off_load: 100
#    minimum_switch_time: 60
#    load_app('calc_conditional_avg', register_calc_conditional_avg)
