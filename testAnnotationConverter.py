import unittest
import json
from annotation_converter import kognicFormat, openLabelFormat, convert

class AnnotationConverterTests(unittest.TestCase):

    def test_GetBboxFromEpbb(self):
        ''' Validate conversion from extreme point to 2D bounding box. '''
        self.assertEqual(convert.get_bbox_from_epbb(10., 5., 20., 10.), [7.5, 15., 5., 10.])

    def test_KognicFormatSelfCheck(self):
        ''' Validate object representation preserves integrity of data. '''
        with open('input/kognic_1.json', 'r') as kognicData:
            kognicDataDict = json.loads(kognicData.read())
            kognicObjectRepresentation = kognicFormat.KognicAnnotation(**kognicDataDict)
            kognicRepresentationJson = json.dumps(kognicObjectRepresentation.dict(by_alias = True, exclude_none = True))
            self.assertEqual(kognicRepresentationJson, json.dumps(kognicDataDict))

    def test_OpenLabelFormatSelfCheck(self):
        ''' Validate object representation preserves integrity of data. '''
        with open('input/open_label_1.json', 'r') as openLabelData:
            openLabelDataDict = json.loads(openLabelData.read())
            openLabelObjectRepresentation = openLabelFormat.OpenLabelAnnotation(**openLabelDataDict)
            openLabelRepresentationJson = json.dumps(openLabelObjectRepresentation.dict(by_alias = True, exclude_none = True))
            self.assertEqual(openLabelRepresentationJson, json.dumps(openLabelDataDict))

    def test_ConvertKognicToOpenLabelFormat(self):
        ''' Validate conversion from Kognic format to Open Label format. '''
        with open('input/kognic_1.json', 'r') as kognicData, open('input/open_label_1.json', 'r') as openLabelData:
            kognicDataDict = json.loads(kognicData.read())
            openLabelDataConverted = convert.convert(kognicFormat.KognicAnnotation(**kognicDataDict))
            openLabelDataDict = json.loads(openLabelData.read())
            self.assertEqual(openLabelDataConverted, openLabelDataDict)

if __name__ == '__main__':
    unittest.main()
