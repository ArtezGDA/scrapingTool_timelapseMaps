# Explanation python script about the dataset in combination with coordinates

In the python script you can specify which data set you use in combination of the place by the use of coordinates. On that basis, you run the script in the terminal, which stores the file in Google Drive, which is linked to your Earth engine account. In short; there is a way to scrape the data and get a visual outcome, this data is then saved as an .tiff file in your google drive. 

You can use different landsat (dataset) to get different outcomes. Every data set is specific in use (think about: year, location, data etc.).

```
import ee
ee.Initialize()

landsat = ee.Image(‘LANDSAT/LC8_L1T_TOA/LC81230322014135LGN00’).select([‘B4’, ‘B3’, ‘B2’]);



llx = 116.2621
lly = 39.8412
urx = 116.4849
ury = 40.01236
geometry = [[llx,lly], [llx,ury], [urx,ury], [urx,lly]]

task_config = {
    ‘description’: ‘imageToDriveExample’,
    ‘scale’: 30,
    ‘region’: geometry
    }

task = ee.batch.Export.image(landsat, ‘exportExample2’, task_config)

task.start()
```

Where it gets saved:
![Google Drive](images/googledrive.png)

Example of what gets exported:
![Example of exporting](images/example.jpg) 