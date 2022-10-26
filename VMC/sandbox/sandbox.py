from bell.avr.mqtt.client import MQTTModule
from bell.avr import utils
from bell.avr.mqtt.payloads import(
    AvrFcmVelocityPayload,
    AvrPcmSetBaseColorPayload,
    AvrApriltagsVisiblePayload,
    AvrPcmSetTempColorPayload,
    AvrPcmSetServoOpenClosePayload,
)

from loguru import logger
class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        self.topic_map = {"avr/fcm/velocity": self.show_velocity}
        self.topic_map = {"avr/apriltags/visible": self.show_april_tag_detected}
        #self.topic_map = {"avr/pcm/set_temp_color": self.show_balls}
    def show_april_tag_detected(self, payload: AvrApriltagsVisiblePayload) -> None:
        apriltagList = payload["tags"]
        self.flash_lights()
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
        for i in range(3):
            self.send_message(
                "avr/pcm/set_temp_color",
                {"wrgb": (255, 255, 0, 0), "time": 1}
            )
            self.send_message(
                "avr/pcm/set_temp_color",
                {"wrgb": (0, 0, 0, 0), "time": 1}
            )

if __name__ == "__main__":
    box = Sandbox()
    box.run()
