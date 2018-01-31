#!/usr/bin/python
#
# csv-geocode.py
#
# @fintanr, Jan 31 2018.
# Create a CSV file containing latitude and longitude values for
# a list of locations
#
# requires an api key for googlemaps
#

import os, csv, json, argparse, googlemaps

print_blanks = False
our_key = "Not Set"
our_infile = "in.csv"
csv_key = "Location"
our_outfile = "out.csv"

def extract_loc_details(gmapref, address):
    # for our purposes we only care about the longitude
    # and latitude, so we discard everything else
    geocode_result = gmapref.geocode(address)

    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']

    return(lat, lng)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csvfile', help='Input CSV File', required=True)
    parser.add_argument('-o', '--outfile', help='Output CSV File', required=True)
    parser.add_argument('-k', '--key', help='Key/Column name in CSV, defaults to Location')
    parser.add_argument('-b', '--blanks', help='Print blank lines in output')

    args = parser.parse_args()

    our_infile = args.csvfile
    our_outfile = args.outfile

    if args.key:
        csv_key = args.key

    if args.blanks:
        print_blanks = True

    if ( os.getenv('GOOGLE_API_KEY') is not None):
        our_key = os.getenv('GOOGLE_API_KEY')
    else:
        print "Please set GOOGLE_API_KEY"
        exit(1)

    try:
        gmaps = googlemaps.Client(our_key)
    except Exception as e:
        print(e)

    with open(our_outfile, 'w') as outfile:
        fieldnames = ['Location', 'Lat', 'Lon']
        writer = csv.DictWriter(outfile, fieldnames)
        writer.writeheader()
        with open(our_infile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if ( row[csv_key] == "" ):
                    if ( print_blanks ):
                        writer.writerow({'Location': '', 'Lat': '', 'Lon': ''})
                else:
                    ( lat, lon) = extract_loc_details(gmaps, row[csv_key])
                    writer.writerow({'Location': row[csv_key], 'Lat': lat, 'Lon': lon})


