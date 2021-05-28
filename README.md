# Spoken To Written
This is a Python library which can convert a paragraph of spoken english to written english.
For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.

## Installation:
No extra installation required but make sure that you have updated pip3 to the latest version before installing spoken_to_written.
You can install the module using Python Package Index using the below command.
>>python3 setup.py install

## Usage:
from spoken_to_written import spoken_to_written<br><br>
spoken_to_written.spoken_2_written('this is a demo paragraph which checks our library examples are triple two followed by ninety dollars followed by five p m')<br><br>
Output: this is a demo paragraph which checks our library examples are 222 followed by 90$ followed by 5 pm<br><br>

## Future Work:
* If the paragraph contains a money figure e.g. fourty one thousand then we may convert it to numbers as 41000.<br>
* Handling punctuation rules.<br>

<div id="upgrade"></div>

## How to Upgrade:
To add new rule to conversion just add conversion rules in conversion_rules.py file.
* If you want to add new key value pair in existing rule type, you can do this by just adding key-value pair on that particular dictinory. For this above change no need to change any code in main spoken_to_written.py file.
* If you want to define new rule type you can add it but for this we need to make changes to spoken_to_written.py file.
