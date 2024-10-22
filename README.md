# Hack49-Smart-Trash-Bin

BIN-E strives to reduce recycling contamination and the amount of recyclable material sent to landfills through an AI powered trash sorting algorithm.

When waste items are put into the recycling bin, the entire batch of material becomes unrecyclable. According to the Environmental Protection Agency (EPA), nearly 60% of recyclable materials in the US are sent to landfills or incinerators yearly. This translates to around 22 million tons of recyclable materials being disposed of improperly every year.

BIN-E offers a cheap and easily implementable solution to this issue by using AI to sort trash, eliminating the possibility of human error. Users dispose of trash normally into the top section of BIN-E, where sorting occurs. A camera and Python OpenCV is used to capture the waste item, which is then identified using a custom trained YOLOv8 dataset. The item is then checked with an external database and sorted as either recyclable or non-recyclable. If the item is not found in the database, or the system is unable to recognize the item, it is automatically classified as non-recyclable to ensure there is no chance of recycling contamination. A servo-motor connected through an Arduino Uno is then instructed to rotate clockwise or counterclockwise in order to place the waste item into the correct bin.

BIN-E is also able to collect data on a user's waste types for each day, and return a waste score for the week. This feature encourages users to work towards achieving sustainable waste management goals!

Materials used:
- Arduino Uno
- Servo 9g SG90 motor

Module installs:
- opencv-python
- supervision
- ultralytics
- pyfirmata

BIN-E is assembled using the following CAD model:
https://cad.onshape.com/documents/3694aab9c71c20256204b78c/w/182cf645799b08a3082ab427/e/62302c27af1291cdd11432ea?renderMode=0&uiState=6717b3a449efe818c4f42009
