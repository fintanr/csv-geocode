# CSV Geocode

Wrapper script to allow you to read in a CSV with Locations and
generate a new CSV containing longitude and latitude details.

## Requirements

Install [uv](https://docs.astral.sh/uv/) 0.13.6 and sync the locked
dependencies:

```sh
uv sync --locked
```

You also need a Google Maps API key.

## Usage

```sh
export GOOGLE_API_KEY=<your-api-key>
```

If you have a column called `Location` in your CSV, that will be read
automatically; otherwise, specify a different column with `-k`.

```sh
uv run --locked ./csv-geocode.py -c in.csv -o out.csv -k OtherLocationTitle
```
