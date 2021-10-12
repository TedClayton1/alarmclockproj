class AlarmClock:
    def _init_(self):
        self.current_time = '2:26pm'
        self.power =[True ]         
        self.alarm_time = '3:00am'


    def set_current_time(self):
        self.curren_time = input('Please set the current time')
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
