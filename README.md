# tesmart_kvm_python
PoC Python script to interact with the TESmart 8-port KVM over IP.

Based on the shell version [here](https://github.com/bbeaudoin/bash/tree/master/tesmart).

## Installation

Requires Python 3 and that you have a TESmart switch that's connected to the network at its default address.  The simplest way to allow the connection to be established is to setup an IP address on your local interface that is on the same subnet as the TESmart device.  See the TESmart documentation for more information.

These instructions assume that you have correct permissions to execute the Python script and that it exists in your path.

## Execution

### Help!

`kvmctl.py -h`

### Working with the switch

#### Check the current port

`kvmctl.py get`

#### Set the switch to a specific port

Port 3:

`kvmctl.py set -p 3`

### Configuring the switch

#### Changing the piezo alert (buzzer)

Mute:

`kvmctl.py mute`

Unmute:

`kvmctl.py unmute`

#### Scan mode

Enable auto scan mode:

`kvmctl.py autoscan`

Disable auto scan mode:

`kvmctl.py noautoscan`

## Contributing

Please create an issue on GitHub for the project.  Pull requests are welcome.

## Credits

[bbeaudoin](https://github.com/bbeaudoin/bash/tree/master/tesmart)'s shell implementation did most of the work here, including but not limited to contacting the vendor and getting API documentation. This project ported the project to Python in an attempt to overcome the limitations of the shell and in order to eventually port it to the PiKVM `kvmd` project.  This project will remain for those who aren't using PiKVM or for reference.
