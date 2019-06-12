print(
    '''
    |+++++++++++++++++++++++++++++++|
    |        ESK8 CALCULATOR        |
    |    Enter part specs to get    | 
    |  performance estimates of an  |
    | eskate board using a brushless|
    |             motor             |
    |+++++++++++++++++++++++++++++++|
    '''
);
print(
    '''
    |+++++++++++++++++++++++++++++++|
    |         Battery Specs         |
    |+++++++++++++++++++++++++++++++|
'''
);
cell_rated_voltage = 3.7;
cell_max_voltage = 4.2; #volts
cell_capacity = input("Cell Capacity (mAh) : ");
C_rating = input("C rating : ");
burst_C_rating = input("Burst C rating : ");
S = input("number of cells in series( S number ) : ");
P = input("Number of cells in parallel : ");

rated_pack_voltage = S * cell_rated_voltage;
max_pack_voltage = S * cell_max_voltage;
pack_capacity = P * cell_capacity;
discharge_current = (C_rating *cell_capacity)/1000;
watt_hours = (cell_capacity/1000) * max_pack_voltage;

print("Rated Pack Voltage : " , rated_pack_voltage);
print("Max Pack Voltage : ", max_pack_voltage);
print("Pack Capacity : " , pack_capacity);
print("Discharge Current : " , discharge_current);
print("Watt Hours : " , watt_hours);

print(
    '''
    |+++++++++++++++++++++++++++++++|
    |          Motor Calcs          |
    |having multiple motors will only|
    |increase board torque not speed|
    |so all further calculations are|
    |done assuming only one motor   |
    |+++++++++++++++++++++++++++++++|
'''
);

motor_max_power = input("Motor Max Power : ");
motor_max_current = input("Motor Max Current : ");
if motor_max_current > discharge_current:
    print("Battery discharge current is too small to support motor max current");
motor_max_voltage = input("motor max voltage : ");
if motor_max_voltage < max_pack_voltage:
    print("Voltage of the battery pack is too high for the motor");
motor_max_torque = input("motor max torque : ");
motor_KV = input("Motor KV : ");
motor_estimated_efficiency = 0.7; #basic constant
motor_rpm = rated_pack_voltage * motor_KV * motor_estimated_efficiency;
print("Motor RPM : " , motor_rpm);

print(
    '''
    |+++++++++++++++++++++++++++++++|
    |   Transmission Calculation    |
    |+++++++++++++++++++++++++++++++|
'''
);

wheel_diameter = input("Wheel Diameter : "); #bigger diameter = more speed - less torque, smaller diameter - vice vera but clearance is an issue
motor_pulley_teeth = input("Motor pulley teeth : ");
wheel_pulley_teeth = input("Wheel pulley teeth : ");
efficiency_of_transmission = 0.95;
gear_ratio = wheel_pulley_teeth / motor_pulley_teeth
wheel_speed = (motor_rpm / gear_ratio) * efficiency_of_transmission
board_speed = (wheel_speed / 60) * 3.1415 * (wheel_diameter/1000) *3.6;
battery_power = rated_pack_voltage * pack_capacity / 1000;
consumption_rate = 25; #Wh/m avg rate of power consumption for a single belt system
range = battery_power / consumption_rate * 1.60934;
print("Gear Ratio : ", gear_ratio)
print("Wheel Speed (RPM) : ", wheel_speed)
print("Board Speed (Km/hr) : ", board_speed)
print("Battery power (watt hours) : ", battery_power)
print("Range (in Km) : ", range)