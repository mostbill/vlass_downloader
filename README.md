#Function

This code helps to download the VLASS(Very Large Array Sky Survey) images as fits files. The size and epochs (default: all three epochs) can be selected.

#Usage

Feed a csv file to the python and run for example:

```python
python imview.py -ra raj2000 -dec dej2000 -source_name name -img_path /your/path/to/fits/storage -csv_path /your/path/to/csv/file
```

#Disclaimer
This code is now heavily based on qso_toolbox by J.-T. Schindler
