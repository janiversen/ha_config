
@state_trigger("sensor.power_meter")
def calculate_casa_consumption():
    task.unique("calculate_casa_consumption")
    #input_number.casa_consumption = sensor.production - sensor.power_meter
