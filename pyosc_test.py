import ui
from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client

toggle1 = 0

def main():	
	while True:
		slider1 = v['slider1'].value * 128
		client.send_message('/pythonista/slider1',slider1)
		
		v['playstop'].action = buttontap
		
		sleep(0.03)
		
def buttontap(sender):
	global toggle1
	
	if toggle1 == 0:
		toggle1 = 1
		client.send_message('/pythonista/toggle1',toggle1)
		
	elif toggle1 == 1:
		toggle1 = 0
		client.send_message('/pythonista/toggle1',toggle1)
		
if __name__ == '__main__':
	client = udp_client.SimpleUDPClient('xxx.xxx.xxx.x',0000)
	
	v = ui.load_view()	
	v.present('sheet',hide_title_bar=True)
	
	main()