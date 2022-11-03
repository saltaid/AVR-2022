from bell.avr.mqtt.client import MQTTModule
from bell.avr import utils
from bell.avr.utils import timing
from bell.avr.mqtt.payloads import(
    AvrFcmVelocityPayload,
    AvrPcmSetBaseColorPayload,
    AvrApriltagsVisiblePayload,
    AvrPcmSetTempColorPayload,
    AvrPcmSetServoOpenClosePayload,
)
import random

from loguru import logger
import time
class Sandbox(MQTTModule):
    bruh = 0
    def __init__(self) -> None:
        super().__init__()
        self.topic_map = {"avr/fcm/velocity": self.show_velocity}
        self.topic_map = {"avr/apriltags/visible": self.show_april_tag_detected}
        # NICK : print these topic_maps to understand the messages you're recieving
        #       
        #self.topic_map = {"avr/pcm/set_temp_color": self.show_balls}
    def show_april_tag_detected(self, payload: AvrApriltagsVisiblePayload) -> None:
        self.send_message(
            "avr/pcm/set_base_color",
            {"wrgb": (0, 0, 0, 0)}
        )
        apriltagList = payload["tags"]
        for _ in range(3):
            logger.debug("before wait")
            self.flash_lights()
            logger.debug("After wait")
        #self.open_servo(2)
    def show_velocity(self, payload: AvrFcmVelocityPayload) -> None:
        vx = payload["vX"]
        vy = payload["vY"]
        vz = payload["vZ"]
        v_ms = (vx, vy, vz)
        logger.debug(f"Velocity information: {v_ms} m/s")


    #def show_balls(self, payload: AvrPcmSetTempColorPayload) -> None:
     #   self.lights_on

    def open_servo(self, channel) -> None:
        pass
        #self.send_message(
         #   "avr/pcm/set_servo_open_close",
          #  {"servo": channel, "action": "open"}
        #)
    def flash_lights(self) -> None:
        
        #for i in range(3):
        self.bruh = self.bruh + 1
        logger.debug("flash_lights()")
        logger.debug(self.bruh)
        self.send_message(
            "avr/pcm/set_temp_color",
            {"wrgb": (0, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}
        )
        
#        self.send_message(
#            "avr/pcm/set_temp_color",
#            {"wrgb": (0, 0, 255, 0)}
#        )
#        
#        self.send_message(
#            "avr/pcm/set_temp_color",
#            {"wrgb": (0, 0, 0, 255)}
#        )



if __name__ == "__main__":
    box = Sandbox()
    box.run()
