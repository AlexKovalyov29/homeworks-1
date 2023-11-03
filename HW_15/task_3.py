"""                             Task 3
                            TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
if the channel N or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
'''
CHANNELS = ["BBC", "Discovery", "TV1000"]
 class TVController:
pass
 controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.exists(4) == "No"
controller.exists("BBC") == "Yes"
'''"""
class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_number = 1

    def first_channel(self):
        self.current_channel_number = 1
        return self.channels[0]

    def last_channel(self):
        self.current_channel_number = len(self.channels)
        return self.channels[-1]

    def turn_channel(self, N):
        self.current_channel_number = N
        return self.channels[N-1]

    def next_channel(self):
        self.current_channel_number += 1
        if self.current_channel_number > len(self.channels):
            self.current_channel_number = 1
        return self.channels[self.current_channel_number-1]

    def previous_channel(self):
        self.current_channel_number -= 1
        if self.current_channel_number < 1:
            self.current_channel_number = len(self.channels)
        return self.channels[self.current_channel_number-1]

    def current_channel(self):
        return self.channels[self.current_channel_number-1]

    def exists(self, N):
        if isinstance(N, str):
            return "Yes" if N in self.channels else "No"
        elif isinstance(N, int):
            return "Yes" if 1 <= N <= len(self.channels) else "No"
CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.exists(4))
print(controller.exists("BBC"))

# СТРУКТУРА ПОДСМОТРЕНА :(