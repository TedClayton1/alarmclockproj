# #As a developer, I want the AlarmClock class to have a method to set (or change) 
# the current time and print to the console the current time.

# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.

# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.

# As a developer, I want to import the AlarmClock class into main.py so I can 
# instantiate it as a new AlarmClock object and call methods on it.




class AlarmClock:
    def _init_(self):
        self.current_time = '2:26pm'
        self.power =[True ]         
        self.alarm_time = '3:00am'


    def set_current_time(self):
        self.current_time = input('Please set the current time')
        print(self.current_time)

    def set_power_on(self):
        self.power = True
        print(self.power)

    def set_power_off(self):
        self.power = False
        print(self.power)

    def set_alarm_time(self):
        self.alarm_time = input("Set the current alarm time")
        print(self.alarm.time)
