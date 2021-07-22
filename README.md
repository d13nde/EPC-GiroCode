# EPC-GiroCode

Generate a PNG image-file holding a QR-Code formated as EPC-QR-Code for scanning with banking apps (aka GiroCode)  
For a detailed description of EPC-QR-Code see: [EPC-QR-Code on Wikipedia](https://de.wikipedia.org/wiki/EPC-QR-Code)

**Version: 1.2 - 20210720 by d13n**
### Changelog
    V 1.0 first functional version
    V 1.1 added uml2ascii function to convert german umlauts
    V 1.2 shorten epc code strings to max allowed length and use absolute number for ammount

### Sample QR-Code
The command:  
`epc-giro-qrgen.py -b BFSWDE33BER -r 'Wikimedia Foerdergesellschaft' -i DE33100205000001194700 -a 123.45 -p 'Spende fuer Wikipedia' epcqr-test.png`  
generates this QR-Code:  
![Sample EPC-QR-Code](epcqr-test.png)

### Usage
```
epc-giro-qrgen.py [-h] [-V] [-v]
  -b BIC -r RECEIVER -i IBAN -a AMOUNT -p PURPOSE
  [--border BORDER] [--size SIZE] [--fg_color FG_COLOR] [--bg_color BG_COLOR]
  output_file
```

### Help
```
Generate EPC-/Giro-QR-Code and write to image file.

positional arguments:
  output_file           Filename for output image.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -v, --verbose         Give some output while working.
  -b BIC, --bic BIC     BIC (Business Identifier Code) for the financial institution of receiver.
  -r RECEIVER, --receiver RECEIVER
                        Name of the receiver for the transfer.
  -i IBAN, --iban IBAN  IBAN (International Bank Account Number) of receiver.
  -a AMOUNT, --amount AMOUNT
                        Amount of money to transfer.
  -p PURPOSE, --purpose PURPOSE
                        Pupose of bank transaction.
  --border BORDER       Amount of white pixels around qr-code, default is 4.
  --size SIZE           Size of code-boxes in pixels, default is 10.
  --fg_color FG_COLOR   Set foreground-color of image (default black)
  --bg_color BG_COLOR   Set background-color of image (default white)
```

