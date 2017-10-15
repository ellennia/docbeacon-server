# DocBeacons

DocBeacons are intended to be Bluetooth Low-Energy (BLE) devices that broadcast the intended use and purpose behind objects and spaces. They are designed to be used with mobile apps that allow users to quickly see the locations and purposes of their physical environments.

This quickly allows people to find out WHY things are arranged the way they are, as well as how to optimally use a device or environment. DocBeacons are designed to be a direct analogue to the traditional 'piece of paper' or manual, however, they are have more in common with the Unix manpage than the stack of papers.

For starters, a DocBeacon is always glued a device. You don't have to worry about the location of the manual, even in a hectic production environment. It's there. It's in the device. Even if the manual is megabytes long. Unlike manuals, DocBeacons can be flashed and update by permissioned users, and can store old revisions in the manner of a wiki.

Another perk, and one I think is important, is discovery. DocBeacons enable to spontaneously learn new things about one's environment and the methodology behind it. We all get trapped in our filter bubbles, and may miss things about our surroundings. DocBeacons hint at you objects of interest.

One of the major inspirations behind DocBeacons is seeing the innefficiencies in many production environments, where employees move into an environment and have to be told every little detail about the env by their managers and supervisors. These workers, looking around, and trying to do their jobs the best they can, may be flooded with myriad questions, more than anyone has the time to answer for them. DocBeacons allow these questions to be sated at the worker's pace.

One may also find DocBeacons moderately redundant to things such as wikis, but they do have distinct advantages from older computer technologies as well. DocBeacons are inherently decentralized. In fact, an alterntive way to implement this concept would be to have some sort of centralized wiki, coupling physical coordinates with text files. However, to accurately track the object's location, they would somehow have to collect their GPS location and transmit it back to the wiki.

DocBeacons should optimally be extremely cheap to mass produce.

# The DocBeacon software.
Being an effort meant to improve the world's understanding of their environments, Python was chosen in part because it is such a human readable language. One of the main goals of the project is to produce a codebase that is heavily documented and easily understandable, possible even to non-programmers.

At the moment, it is written around the normal Bluetooth protocol, not Bluetooth Low-Energy, as specified above. The reason for this is that I do not have a perfect understanding of how exactly I would use BLE from Python, and I would rather create a prototype of the logic of the software before I mess around with the details of the hardware protocol.

# The development
DocBeacon is developed by Ellen Hebert. @homeslashellen ellenhebert@protonmail.com
