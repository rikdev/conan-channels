#include <channels/channel.h>
#include <channels/transmitter.h>
#include <iostream>

int main()
{
	channels::transmitter<channels::channel<const char*>> transmitter;
	channels::connection connection =
		transmitter.get_channel().connect([](const char* const str){ std::cout << str; });
	transmitter("Test application successfully ran\n");
}
