#!/usr/bin/python3
# EPC- / Giro-QR-Code generator
# generate image file holding a QR-Code formated as EPC-/GiroCode for scanning with banking apps
# see: https://de.wikipedia.org/wiki/EPC-QR-Code
#
# Version: 1.2 - 20210720 by d13n
# Changelog:
#            V 1.0 first functional version
#            V 1.1 added uml2ascii function to convert german umlauts
#            V 1.2 shorten epc code strings to max allowed length and use absolute number for ammount
#
# usage: epc-giro-qrgen.py [-h] [-V] [-v]
#                          -b BIC -r RECEIVER -i IBAN -a AMOUNT -p PURPOSE
#                          [--border BORDER] [--size BOX_SIZE] [--fg_color FG_COLOR] [--bg_color BG_COLOR]
#                          output_file


import sys
import qrcode
from pathlib import Path

# replace german umlauts
def uml2ascii(str):
    uml_dict = {
        'Ä': 'Ae',
        'ä': 'ae',
        'Ö': 'Oe',
        'ö': 'oe',
        'Ü': 'Ue',
        'ü': 'ue',
        'ß': 'ss',
    }

    for u in uml_dict.keys():
        str = str.replace(u, uml_dict[u])

    return str

# generate ect/giro-code from input parameters
def epcqrgen(bic, receiver, iban, amount, purpose, output_file, size=4, border=10, fg_color='black', bg_color='white'):
    # first lines are static
    qrdata = 'BCD\n001\n2\nSCT\n'
    # data lines
    qrdata += bic[:11] + '\n'
    qrdata += uml2ascii(receiver[:70]) + '\n'
    qrdata += iban[:34] + '\n'
    qrdata += 'EUR' + str(abs(amount)) + '\n'
    qrdata += '\n\n' + uml2ascii(purpose[:140]) + '\n'

    if verbose:
        print('QR-Data:')
        print(qrdata)

    # generate the qr-code...
    qr = qrcode.QRCode(
        box_size = size,
        border = border
    )
    qr.add_data(qrdata)
    qr.make(fit = True)

    try:
        img = qr.make_image(fill_color = fg_color, back_color = bg_color)
    except Exception as e:
        print(e)
        parser.errror('Error creating img from qr-data.')

    try:
        img.save(output_file)
        if verbose:
            print('QR-Code image written to file: ' + output_file)
            print('Mission completed.')
    except Exception as e:
        print(e)
        parser.error('Could not write image to file: ' + output_file)

# main
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate EPC-/Giro-QR-Code and write to image file.')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.2')
    parser.add_argument('-v', '--verbose', help='Give some output while working.', action='store_true')

    # input
    parser.add_argument(
        '-b', '--bic',
        required = True,
        help = 'BIC (Business Identifier Code) for the financial institution of receiver.')
    parser.add_argument(
        '-r', '--receiver',
        required = True,
        help = 'Name of the receiver for the transfer.')
    parser.add_argument(
        '-i', '--iban',
        required = True,
        help = 'IBAN (International Bank Account Number) of receiver.')
    parser.add_argument(
        '-a', '--amount',
        required = True,
        type = float,
        help = 'Amount of money to transfer.')
    parser.add_argument(
        '-p', '--purpose',
        required = True,
        help = 'Pupose of bank transaction.')

    # output
    parser.add_argument('output_file', help='Filename for output image.')

    # params for qrcode module
    parser.add_argument(
        '--border',
        dest = 'border',
        type = int,
        help = 'Amount of white pixels around qr-code, default is 4.',
        default = 4)
    parser.add_argument(
        '--size',
        type =int,
        help='Size of code-boxes in pixels, default is 10.',
        default=10)
    parser.add_argument(
        '--fg_color',
        help='Set foreground-color of image (default black)',
        default='black')
    parser.add_argument(
        '--bg_color',
        help='Set background-color of image (default white)',
        default='white')

    # parse arguments
    args = parser.parse_args()
    verbose = args.verbose

    if verbose:
        parser.print_usage()
        print(args)

    epcqrgen(bic=args.bic, receiver=args.receiver, iban=args.iban, amount=args.amount, purpose=args.purpose,
             output_file=args.output_file,
             size=args.size, border=args.border, fg_color=args.fg_color, bg_color=args.bg_color)

    if verbose:
        print('Main-Mission completed.')
