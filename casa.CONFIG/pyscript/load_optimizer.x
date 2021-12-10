
@state_trigger("sensor.power_meter != '9999'")
def calculate_casa_consumption(value=None):
    load = int(state.get("sensor.production")) - int(value)
    state.set("sensor.virtual_casa_consumo", value=load)
