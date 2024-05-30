import utime
import bluetooth
from ble_advertising import advertising_payload
from machine import TouchPad, Pin,PWM,I2C
from MX1508 import *
from micropython import const
from tcs34725 import *
import uasyncio as asio
import time
from neopixel import NeoPixel

#33

an_grab = 12
an1 = 138
serv180 = PWM(Pin(18, Pin.OUT))
serv180.freq(50)
serv180.duty(0)
start = 0

serv360 = PWM(Pin(5, Pin.OUT))
serv360.freq(50)
serv360.duty(0)


i2c_bus = I2C(0, sda=Pin(21), scl=Pin(22))
tcs = TCS34725(i2c_bus)
tcs.gain(4)#gain must be 1, 4, 16 or 60
tcs.integration_time(80)
NUM_OF_LED = 1
np = NeoPixel(Pin(19), NUM_OF_LED)

color=['Cyan','Black','Yellow','Navy','Orange','Green','Red']
col_id=0
check1='!B01611'
debug=1

sp = 800

motorPL = MX1508(13, 12)
motorPP = MX1508(14, 27)
motorZL = MX1508(16, 4)
motorZP = MX1508(15, 2)

motorPL.stop()
motorPP.stop()
motorZL.stop()


def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max - out_min) / (in_max-in_min) + out_min)
def servo(pin, angle):
    pin.duty(map(angle, 0, 180, 20, 120))


servo(serv180, an_grab)
servo(serv360, an1)

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

_FLAG_WRITE = const(0x0008)
_FLAG_NOTIFY = const(0x0010)

_UART_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
_UART_TX = (
    bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"),
    _FLAG_NOTIFY,
)
_UART_RX = ( 
    bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"),
    _FLAG_WRITE,
)
_UART_servICE = (
    _UART_UUID,
    (_UART_TX, _UART_RX),
)

# org.bluetooth.characteristic.gap.appearance.xml
_ADV_APPEARANCE_GENERIC_COMPUTER = const(128)


class BLEUART:
    def __init__(self, ble, name="OXOTA", rxbuf=100):
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        ((self._tx_handle, self._rx_handle),) = self._ble.gatts_register_services((_UART_servICE,))
        # Increase the size of the rx buffer and enable append mode.
        self._ble.gatts_set_buffer(self._rx_handle, rxbuf, True)
        self._connections = set()
        self._rx_buffer = bytearray()
        self._handler = None
        # Optionally add services=[_UART_UUID], but this is likely to make the payload too large.
        self._payload = advertising_payload(name=name, appearance=_ADV_APPEARANCE_GENERIC_COMPUTER)
        self._advertise()

    def irq(self, handler):
        self._handler = handler

    def _irq(self, event, data):
        # Track connections so we can send notifications.
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            if conn_handle in self._connections:
                self._connections.remove(conn_handle)
            # Start advertising again to allow a new connection.
            self._advertise()
        elif event == _IRQ_GATTS_WRITE:
            conn_handle, value_handle = data
            if conn_handle in self._connections and value_handle == self._rx_handle:
                self._rx_buffer += self._ble.gatts_read(self._rx_handle)
                if self._handler:
                    self._handler()

    def any(self):
        return len(self._rx_buffer)

    def read(self, sz=None):
        if not sz:
            sz = len(self._rx_buffer)
        result = self._rx_buffer[0:sz]
        self._rx_buffer = self._rx_buffer[sz:]
        return result

    def write(self, data):
        for conn_handle in self._connections:
            self._ble.gatts_notify(conn_handle, self._tx_handle, data)

    def close(self):
        for conn_handle in self._connections:
            self._ble.gap_disconnect(conn_handle)
        self._connections.clear()

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)


    
def on_rx():
    global check1
    check1=uart.read().decode().strip()


ble = bluetooth.BLE()
uart = BLEUART(ble)
    

async def color_det():
    global col_id
    await asio.sleep_ms(0)
    rgb=tcs.read(1)
    r,g,b=rgb[0],rgb[1],rgb[2]
    h,s,v=rgb_to_hsv(r,g,b)
    if (h>340)or(h<10):
        col_id=6
        np[0] = (255,0,0)
    if 10<h<60:
        col_id=4
        np[0] = (255,128,0)
    if 60<h<120:
        col_id=2
        np[0] = (255,255,51)
    if 120<h<180:
        col_id=5
        np[0] = (0,255,0)
    if 180<h<240:
        if v>130:
            col_id=0
            np[0] = (51,255,255)
        if 30<v<40:
            col_id=3
            np[0] = (0,0,153)
        if v<30:
            col_id=1
            np[0] = (0,0,0)
    np[0] = (250, 100, 150)
    np.write()
    await send_color(20)
    if debug:
        print('Color is {}. R:{} G:{} B:{} H:{:.0f} S:{:.0f} V:{:.0f}'.format(color[col_id],r,g,b,h,s,v))
                
async def send_color(int_ms):     
    while True:
        try:
            while True:
                uart.write(color[col_id]+"\n")
                await asio.sleep_ms(int_ms)
        except KeyboardInterrupt:
            pass

   
def serv180Control(an_grab):
    global start
    #await asio.sleep_ms(0)
    if(utime.ticks_us() - start >= 8000):
        servo(serv180, an_grab)
        start = utime.ticks_us()

def serv360Control(an_grab):
    global start
    #await asio.sleep_ms(0)
    if(utime.ticks_us() - start >= 8000):
        servo(serv360, an_grab)
        start = utime.ticks_us()

async def motor_control(int_ms):
    global an_grab, an1, sp
        
    while 1:
        await asio.sleep_ms(int_ms)
        
        if check1[2] == '5' and check1[3] == "1":
            sp = 800
            motorPL.forward(sp)
            motorPP.forward(sp)
            motorZL.forward(sp)
            motorZP.forward(sp)       
        if check1[2] == '5' and check1[3] == "0":
            motorPL.stop()
            motorPP.stop()
            motorZL.stop()
            motorZP.stop()
            
            
        if check1[2] == '6' and check1[3] == "1":
            sp = 800
            motorPL.reverse(sp)
            motorPP.reverse(sp)
            motorZL.reverse(sp)
            motorZP.reverse(sp)   
        if check1[2] == '6' and check1[3] == "0":
            motorPL.stop()
            motorPP.stop()
            motorZL.stop()
            motorZP.stop()
            
        if check1[2] == '8' and check1[3] == "1":
            sp = 450
            motorPL.forward(sp)
            motorPP.reverse(sp)
            motorZL.forward(sp)
            motorZP.reverse(sp)
        if check1[2] == '8' and check1[3] == "0":
            motorPL.stop()
            motorPP.stop()
            motorZL.stop()
            motorZP.stop()

        if check1[2] == '7' and check1[3] == "1":
            sp = 450
            motorPP.forward(sp)
            motorPL.reverse(sp)
            motorZP.forward(sp)
            motorZL.reverse(sp)
        if check1[2] == '7' and check1[3] == "0":
            motorPL.stop()
            motorPP.stop()
            motorZL.stop()
            motorZP.stop()
            
        if check1[2] == '3' and check1[3]=='1':
            if (an_grab + 3) < 181:
                an_grab += 3
                serv180Control(an_grab)
        if check1[2] == '4' and check1[3]=='1':
            if (an_grab - 3) > -1:
                an_grab -= 3
                serv180Control(an_grab)
        
        if check1[2] == '1' and check1[3]=='0':
            if (an1 + 1) < 137:
                an1 += 1
                serv360Control(an1)

        if check1[2] == '1' and check1[3]=='1':
            if (an1 - 3) > 25:
                an1 -= 3
                serv360Control(an1)
            
        if check1[2] == '2' and check1[3]=='1':
            await color_det()

            
def send_color(int_ms):
    try:
        uart.write(color[col_id]+"\n")
        await asio.sleep_ms(int_ms)
    except KeyboardInterrupt:
        pass
    
    
uart.irq(handler=on_rx)
uart.close()
loop = asio.get_event_loop()
loop.create_task(motor_control(20))
#loop.create_task(send_color(100))
loop.create_task(color_det())
loop.run_forever()