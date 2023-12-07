import serial
import serial.threaded
class SerialCommunication(serial.threaded.LineReader):
    ENCODING = 'utf-8'
    UNICODE_HANDLING = 'replace'
    def handle_line(self, line):
        """
        You can code here what you want when recive a message
        Process when recive a message with "\r\n" in the end of the message
        REMEMBER: Message END with "\r\n"
        """
        print("Line received: {!r}".format(line))

    def write_line(self, text):
        """
        This is used to send messages which need to be a Unicode string 
        before sending ans also the newline is append.
        If you want to use a different encoding, modify the self.transport.write() call with the desired message.
        """
        self.transport.write(text.encode(self.ENCODING, self.UNICODE_HANDLING))
        print(text)


def make_string(data):
    """
    Convert an integer to a string with a specific format.
    Parameters:
        data (int): The input integer.
    Returns:
        str: The converted string.
    Description:
        This function takes an integer as input and converts it to a string with a specific format.\n
        If the input integer is positive and less than 10, the function adds five leading zeros to the string. \n
        If the input integer is positive and less than 100, the function adds four leading zeros to the string. \n
        If the input integer is positive and less than 1000, the function adds three leading zeros to the string. \n
        If the input integer is positive and less than 10000, the function adds two leading zeros to the string. \n
        If the input integer is positive and less than 100000, the function adds one leading zero to the string. \n
        If the input integer is negative, the function takes the absolute value, adds a negative sign, and adds leading zeros based on the same rules as for positive integers. 
    Example:
        >>> make_string(123)
        '00123'
        >>> make_string(-456)
        '-00456'
    """
    string_back = ""
    if data >= 0:
        if data < 10:
            string_back = "00000" + str(data)
        elif data < 100:
            string_back = "0000" + str(data)
        elif data < 1000:
            string_back = "000" + str(data)
        elif data < 10000:
            string_back = "00" + str(data)
        elif data < 100000:
            string_back = "0" + str(data)
    else:
        data = abs(data)
        if data < 10:
            string_back = "-0000" + str(data)
        elif data < 100:
            string_back = "-000" + str(data)
        elif data < 1000:
            string_back = "-00" + str(data)
        elif data < 10000:
            string_back = "-0" + str(data)
        elif data < 100000:
            string_back = "-" + str(data)
    return string_back

# Define Serial Communication
ser = serial.Serial('COM5', 9600, timeout=10)
# Define Serial Communication Thread
ThreadCom = serial.threaded.ReaderThread(ser, SerialCommunication)
# Start Thread
ThreadCom.start()
# Connect
transport, protocol = ThreadCom.connect()
valueX, valueY, valueZ = 1100, -1200, 0
#To Send the message
# protocol.write_line(Msg)
while True:
    # Press a key to send a message
    if(input()):
        # CANNOT write message continuosly in the loop
        protocol.write_line(f"X={make_string(valueX)},Y={make_string(valueY)},Z={make_string(valueZ)}")
    
