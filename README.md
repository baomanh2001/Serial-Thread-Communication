# Serial-Thread-Communication
Using Serial.Threaded with Python to communicate through UART.
## Description
To show the example of reading and sending message through UART using the Serial.threaded.ReaderThread() with a little of basic use.
## Getting Started
### Dependencies
* Python
* PySerial
## Executing program
* Modify Recieve Message:

Whenever recieve the message WITH "\r\n" IN THE END, handle_line() will be called.
Therefore, to process the action when recieve the message, we will code in here.
```
def handle_line(self, line):
```

* Modify Sending Message

When we send the message, we can change how the message encoded in the self.transport.write() with the encode way we want:
```
    def write_line(self, text):
        self.transport.write(text.encode(self.ENCODING, self.UNICODE_HANDLING))
```
* Config UART

We can config the port of Serial that fit with the setup.
After that, we need to start the thread for recieve message.
```
# Define Serial Communication
ser = serial.Serial('COM5', 9600, timeout=10)
# Define Serial Communication Thread
ThreadCom = serial.threaded.ReaderThread(ser, SerialCommunication)
# Start Thread
ThreadCom.start()
# Connect
transport, protocol = ThreadCom.connect()
```
* Send Message

To send message we will send the string in the protocol.write_line().
WARNING: It cannot be started continously.
```
protocol.write_line(f"X={make_string(valueX)},Y={make_string(valueY)},Z={make_string(valueZ)}")
```
#Normal Issue
* Cannot receive message
Missing the Terminator for the handle_line to run.
The message send back to the port need to be like this "asdasd \r\n".
REMEMBER to add "\r\n" in your message.


