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
