# CSV Geocode

Wrapper script to allow you to read in a CSV with Locations and
generate a new CSV containing longitude and latitude details. 

# Requirements

You need to have the googlemaps module installed and an api key for
Google Maps.

pip install googlemaps

# Usage

export GOOGLE_API_KEY=<your api key>

If you have a column called Location in your CSV, that will be read 
automatically other wise you can specify a value with -k

./csv-geocode.py -c in.csv -o out.csv -k OtherLocationTitle

 
