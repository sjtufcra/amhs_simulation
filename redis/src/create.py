import time
import random
class Car:
    def __init__(self,id,**kwargs):
        default_values = {
            '@type': "com.alibaba.fastjson2.JSONObject",
            'current_speed': self.generate_val(5000),
            'last_time': "2024-06-18 14:02:04",
            'location': "0",
            'oht_id': id,
            'oht_ip': "128.168.11.147",
            'oht_status_alarm_set': "0",
            'oht_status_err_set': "0",
            'oht_status_idle': "0",
            'oht_status_is_have_foup': "0",
            'oht_status_local_control': "0",
            'oht_status_manual_control': self.generate_val(),
            'oht_status_move_enable': self.generate_val(),
            'oht_status_online_control': self.generate_val(),
            'oht_status_pausing': self.generate_val(),
            'oht_status_prohibit': self.generate_val(),
            'oht_status_quhuoxing': self.generate_val(),
            'position': self.generate_val(71300000),
            'rfid_read_error': "0",
            'the_rfid_foup': "",
        }
        default_values.update(kwargs)
        for key, value in default_values.items():
            setattr(self, key, value)
        self.set_last_time()

    def to_json(self):
        return self.__dict__
    
    def __str__(self):
        return str(self.__dict__)
    
    def set_last_time(self, last_time=None):
        if last_time is None:
            last_time = time.time()
        self.last_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_time))

    def generate_val(self,length=1):
        return str(random.randint(0,length))

